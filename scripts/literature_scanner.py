import argparse
import json
import time
from pathlib import Path
from typing import Dict, List, Tuple

import arxiv

from utils import (
    ARXIV_QUERY_LIST,
    append_log,
    build_dedup_key,
    data_dir,
    extract_arxiv_base_id,
    load_json,
    merge_paper_records,
    repo_root,
    stable_source_id,
    utc_now,
    write_json,
)


DEFAULT_CHECKPOINT = {
    "last_query": ARXIV_QUERY_LIST[0]["label"],
    "last_query_index": 0,
    "last_index": 0,
    "last_run_time": None,
}


def normalize_raw_record(result: arxiv.Result, query_source: str) -> Dict[str, object]:
    authors = [author.name for author in result.authors]
    published = result.published
    short_id = result.get_short_id()
    base_id = extract_arxiv_base_id(short_id)
    return {
        "id": stable_source_id("arxiv", base_id),
        "source": "arxiv",
        "source_id": base_id,
        "title": " ".join(result.title.strip().split()),
        "authors": authors,
        "year": published.year if published else None,
        "abstract": " ".join((result.summary or "").split()),
        "url": result.entry_id,
        "categories": list(result.categories or []),
        "query_source": query_source,
        "query_sources": [query_source],
        "date_discovered": utc_now(),
        "dedup_key": build_dedup_key(result.title, published.year if published else None, authors),
    }


def migrate_legacy_papers(raw_path: Path, log_path: Path) -> None:
    legacy_path = raw_path.parent / "papers.json"
    current_raw = load_json(raw_path, [])
    raw_is_empty = not isinstance(current_raw, list) or len(current_raw) == 0
    if legacy_path.exists() and raw_is_empty:
        legacy_records = load_json(legacy_path, [])
        migrated_records: List[Dict[str, object]] = []
        for record in legacy_records:
            title = record.get("title", "")
            authors = record.get("authors") or []
            year = record.get("year")
            arxiv_id = extract_arxiv_base_id(record.get("arxiv_id", ""))
            query_source = record.get("query_source", "legacy-import")
            migrated_records.append(
                {
                    "id": stable_source_id("arxiv", arxiv_id or build_dedup_key(title, year, authors)[:12]),
                    "source": "arxiv",
                    "source_id": arxiv_id or None,
                    "title": title,
                    "authors": authors,
                    "year": year,
                    "abstract": record.get("abstract", ""),
                    "url": record.get("url", ""),
                    "categories": record.get("categories") or [],
                    "query_source": query_source,
                    "query_sources": [query_source],
                    "date_discovered": record.get("date_discovered") or utc_now(),
                    "dedup_key": build_dedup_key(title, year, authors),
                }
            )
        write_json(raw_path, merge_paper_records(migrated_records))
        append_log(log_path, f"migrated-legacy-papers count={len(migrated_records)}")


def ensure_files(raw_path: Path, checkpoint_path: Path, log_path: Path) -> None:
    if not raw_path.exists():
        write_json(raw_path, [])
    migrate_legacy_papers(raw_path, log_path)

    if not checkpoint_path.exists():
        write_json(checkpoint_path, DEFAULT_CHECKPOINT)
    if not log_path.exists():
        append_log(log_path, "scan-log-created")


def build_index(records: List[Dict[str, object]]) -> Dict[str, Dict[str, object]]:
    index: Dict[str, Dict[str, object]] = {}
    for record in records:
        if "dedup_key" in record:
            index[record["dedup_key"]] = record
    return index


def scan_batch(
    client: arxiv.Client,
    query_label: str,
    query_string: str,
    start_index: int,
    batch_size: int,
    existing_index: Dict[str, Dict[str, object]],
    log_path: Path,
) -> Tuple[List[Dict[str, object]], int]:
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
        record = normalize_raw_record(result, query_label)
        key = record["dedup_key"]
        if key in existing_index:
            existing = existing_index[key]
            merged_query_sources = sorted(set((existing.get("query_sources") or []) + [query_label]))
            existing["query_sources"] = merged_query_sources
            existing["query_source"] = existing.get("query_source") or query_label
            continue
        existing_index[key] = record
        new_records.append(record)

    append_log(log_path, f"raw-scan query='{query_label}' start_index={start_index} seen={seen_count} added={len(new_records)}")
    return new_records, seen_count


def run_once(raw_path: Path, checkpoint_path: Path, log_path: Path, batch_size: int) -> None:
    checkpoint = load_json(checkpoint_path, DEFAULT_CHECKPOINT.copy())
    raw_records = load_json(raw_path, [])
    if not isinstance(raw_records, list):
        raw_records = []

    raw_records = merge_paper_records(raw_records)
    existing_index = build_index(raw_records)

    query_index = int(checkpoint.get("last_query_index", 0)) % len(ARXIV_QUERY_LIST)
    start_index = int(checkpoint.get("last_index", 0))
    query_entry = ARXIV_QUERY_LIST[query_index]

    client = arxiv.Client(page_size=batch_size, delay_seconds=3.0, num_retries=3)
    append_log(log_path, f"batch-start query='{query_entry['label']}' index={start_index}")

    new_records, seen_count = scan_batch(
        client=client,
        query_label=query_entry["label"],
        query_string=query_entry["query"],
        start_index=start_index,
        batch_size=batch_size,
        existing_index=existing_index,
        log_path=log_path,
    )

    if new_records:
        raw_records.extend(new_records)
        raw_records = merge_paper_records(raw_records)
        write_json(raw_path, raw_records)

    next_query_index = query_index
    next_index = start_index + seen_count
    if seen_count < batch_size:
        next_query_index = (query_index + 1) % len(ARXIV_QUERY_LIST)
        next_index = 0

    checkpoint_payload = {
        "last_query": ARXIV_QUERY_LIST[next_query_index]["label"],
        "last_query_index": next_query_index,
        "last_index": next_index,
        "last_run_time": utc_now(),
    }
    write_json(checkpoint_path, checkpoint_payload)
    append_log(log_path, f"checkpoint-saved next_query='{checkpoint_payload['last_query']}' next_index={next_index} raw_total={len(raw_records)}")

    print(
        json.dumps(
            {
                "query": query_entry["label"],
                "start_index": start_index,
                "seen_count": seen_count,
                "new_raw_count": len(new_records),
                "raw_total": len(raw_records),
                "next_query": checkpoint_payload["last_query"],
                "next_index": next_index,
            },
            ensure_ascii=False,
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan arXiv into the raw manufacturing AI intake layer.")
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--loop", action="store_true")
    parser.add_argument("--sleep-seconds", type=int, default=60)
    parser.add_argument("--max-cycles", type=int, default=0)
    args = parser.parse_args()

    repo_root()
    raw_path = data_dir() / "raw_papers.json"
    checkpoint_path = data_dir() / "checkpoint.json"
    log_path = data_dir() / "scan_log.txt"

    ensure_files(raw_path, checkpoint_path, log_path)

    cycle = 0
    while True:
        try:
            run_once(raw_path, checkpoint_path, log_path, args.batch_size)
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
