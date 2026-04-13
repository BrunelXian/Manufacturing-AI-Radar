import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

import arxiv


QUERY_LIST = [
    {
        "label": "additive manufacturing machine learning",
        "query": 'all:"additive manufacturing" AND all:"machine learning"',
    },
    {
        "label": "LPBF machine learning",
        "query": '(all:"LPBF" OR all:"laser powder bed fusion") AND all:"machine learning"',
    },
    {
        "label": "LDED machine learning",
        "query": '(all:"LDED" OR all:"directed energy deposition") AND all:"machine learning"',
    },
    {
        "label": "welding machine learning",
        "query": 'all:"welding" AND all:"machine learning"',
    },
    {
        "label": "manufacturing reinforcement learning",
        "query": 'all:"manufacturing" AND all:"reinforcement learning"',
    },
    {
        "label": "process monitoring machine learning",
        "query": 'all:"process monitoring" AND all:"machine learning"',
    },
    {
        "label": "digital twin manufacturing AI",
        "query": 'all:"digital twin" AND all:"manufacturing"',
    },
    {
        "label": "defect detection manufacturing deep learning",
        "query": 'all:"defect detection" AND all:"manufacturing"',
    },
]

RELEVANCE_TERMS = [
    "manufacturing",
    "additive",
    "welding",
    "machining",
    "industrial",
    "process monitoring",
    "production",
    "laser powder bed fusion",
    "lpbf",
    "directed energy deposition",
    "lded",
    "waam",
]

DEFAULT_CHECKPOINT = {
    "last_query": QUERY_LIST[0]["label"],
    "last_query_index": 0,
    "last_index": 0,
    "last_run_time": None,
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def append_log(log_path: Path, message: str) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{utc_now()}] {message}\n")


def is_relevant(result: arxiv.Result) -> bool:
    haystack = " ".join(
        [
            result.title or "",
            result.summary or "",
            " ".join(result.categories or []),
        ]
    ).lower()
    return any(term in haystack for term in RELEVANCE_TERMS)


def normalise_paper(result: arxiv.Result, query_source: str) -> Dict[str, object]:
    authors = [author.name for author in result.authors]
    published = result.published
    paper_id = result.get_short_id()
    return {
        "title": result.title.strip(),
        "authors": authors,
        "year": published.year if published else None,
        "arxiv_id": paper_id,
        "abstract": " ".join(result.summary.split()),
        "url": result.entry_id,
        "categories": list(result.categories or []),
        "query_source": query_source,
    }


def build_index(records: List[Dict[str, object]]) -> Dict[str, Dict[str, object]]:
    return {record["arxiv_id"]: record for record in records if "arxiv_id" in record}


def scan_batch(
    client: arxiv.Client,
    query_label: str,
    query_string: str,
    start_index: int,
    batch_size: int,
    existing_index: Dict[str, Dict[str, object]],
    log_path: Path,
) -> Tuple[List[Dict[str, object]], int, int]:
    search = arxiv.Search(
        query=query_string,
        max_results=batch_size,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )
    results = client.results(search, offset=start_index)

    new_records: List[Dict[str, object]] = []
    seen_count = 0

    for result in results:
        seen_count += 1
        if not is_relevant(result):
            continue
        record = normalise_paper(result, query_label)
        arxiv_id = record["arxiv_id"]
        if arxiv_id in existing_index:
            continue
        existing_index[arxiv_id] = record
        new_records.append(record)

    append_log(
        log_path,
        f"query='{query_label}' start_index={start_index} seen={seen_count} new={len(new_records)}",
    )
    return new_records, seen_count, len(new_records)


def run_once(
    papers_path: Path,
    checkpoint_path: Path,
    log_path: Path,
    batch_size: int,
) -> None:
    checkpoint = load_json(checkpoint_path, DEFAULT_CHECKPOINT.copy())
    papers = load_json(papers_path, [])
    if not isinstance(papers, list):
        papers = []
    existing_index = build_index(papers)

    query_index = int(checkpoint.get("last_query_index", 0)) % len(QUERY_LIST)
    start_index = int(checkpoint.get("last_index", 0))
    query_entry = QUERY_LIST[query_index]
    query_label = query_entry["label"]
    query_string = query_entry["query"]

    client = arxiv.Client(page_size=batch_size, delay_seconds=3.0, num_retries=3)
    append_log(log_path, f"batch-start query='{query_label}' index={start_index}")

    new_records, seen_count, new_count = scan_batch(
        client=client,
        query_label=query_label,
        query_string=query_string,
        start_index=start_index,
        batch_size=batch_size,
        existing_index=existing_index,
        log_path=log_path,
    )

    if new_records:
        papers.extend(new_records)
        papers.sort(key=lambda item: (item.get("year") or 0, item.get("arxiv_id") or ""), reverse=True)
        write_json(papers_path, papers)

    next_query_index = query_index
    next_index = start_index + seen_count
    if seen_count < batch_size:
        next_query_index = (query_index + 1) % len(QUERY_LIST)
        next_index = 0

    checkpoint_payload = {
        "last_query": QUERY_LIST[next_query_index]["label"],
        "last_query_index": next_query_index,
        "last_index": next_index,
        "last_run_time": utc_now(),
    }
    write_json(checkpoint_path, checkpoint_payload)
    append_log(
        log_path,
        f"checkpoint-saved next_query='{checkpoint_payload['last_query']}' next_index={next_index} papers_total={len(papers)}",
    )

    print(
        json.dumps(
            {
                "query": query_label,
                "start_index": start_index,
                "seen_count": seen_count,
                "new_count": new_count,
                "papers_total": len(papers),
                "next_query": checkpoint_payload["last_query"],
                "next_index": next_index,
            },
            ensure_ascii=False,
        )
    )


def ensure_files(papers_path: Path, checkpoint_path: Path, log_path: Path) -> None:
    if not papers_path.exists():
        write_json(papers_path, [])
    if not checkpoint_path.exists():
        write_json(checkpoint_path, DEFAULT_CHECKPOINT)
    if not log_path.exists():
        append_log(log_path, "scan-log-created")


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan arXiv for AI-for-manufacturing papers.")
    parser.add_argument("--batch-size", type=int, default=20, help="Number of arXiv records to scan per batch.")
    parser.add_argument("--loop", action="store_true", help="Run continuously.")
    parser.add_argument("--sleep-seconds", type=int, default=60, help="Sleep interval between loop iterations.")
    parser.add_argument("--max-cycles", type=int, default=0, help="Optional maximum cycles for loop mode. 0 means infinite.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    data_dir = repo_root / "data"
    papers_path = data_dir / "papers.json"
    checkpoint_path = data_dir / "checkpoint.json"
    log_path = data_dir / "scan_log.txt"

    ensure_files(papers_path, checkpoint_path, log_path)

    cycle = 0
    while True:
        try:
            run_once(
                papers_path=papers_path,
                checkpoint_path=checkpoint_path,
                log_path=log_path,
                batch_size=args.batch_size,
            )
        except Exception as exc:
            append_log(log_path, f"error type={type(exc).__name__} detail={exc}")
            print(f"scanner-error: {type(exc).__name__}: {exc}")
            time.sleep(min(args.sleep_seconds, 30))

        if not args.loop:
            break

        cycle += 1
        if args.max_cycles and cycle >= args.max_cycles:
            break

        append_log(log_path, f"sleep seconds={args.sleep_seconds}")
        time.sleep(args.sleep_seconds)


if __name__ == "__main__":
    main()
