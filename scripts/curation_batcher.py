import argparse
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List

from utils import data_dir, ensure_directory, load_json, today_utc, write_json


PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
STATUS_EXCLUDE = {"curated", "rejected"}
MAX_BATCH_SIZE = 8
MIN_BATCH_SIZE = 3


def safe_name_from_refs(target: str) -> str:
    name = Path(target).stem
    return name


def queue_sort_key(item: Dict[str, Any]):
    return (
        PRIORITY_ORDER.get(item.get("batch_priority", "low"), 99),
        -(item.get("relevance_score") or 0),
        -(item.get("year") or 0),
        item.get("title") or "",
    )


def select_batch(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    ordered = sorted(items, key=queue_sort_key)
    return ordered[:MAX_BATCH_SIZE]


def build_markdown(day: str, grouped_batches: Dict[str, List[Dict[str, Any]]], deferred_items: List[Dict[str, Any]]) -> str:
    lines = [
        f"# Curation Batches - {day}",
        "",
        "This file is the daily handoff view from the curated queue into reviewable curation batches.",
        "",
    ]

    for priority in ["high", "medium", "low"]:
        lines.append(f"## {priority.title()} Priority Batches")
        lines.append("")
        has_any = False
        for target, items in sorted(grouped_batches.items()):
            batch_items = [item for item in items if item.get("batch_priority") == priority]
            if not batch_items:
                continue
            has_any = True
            lines.append(f"### {target}")
            lines.append("")
            lines.append(f"- Target refs page: `{target}`")
            lines.append(f"- Suggested batch size: {len(batch_items)}")
            lines.append("")
            for item in batch_items:
                lines.append(
                    f"- {item['title']} ({item.get('year')}) [score={item.get('relevance_score')}] "
                    f"status={item.get('curation_status')} "
                    f"primary={item.get('primary_domain_tag')}"
                )
            lines.append("")
        if not has_any:
            lines.append("- None")
            lines.append("")

    lines.append("## Deferred Items")
    lines.append("")
    if deferred_items:
        for item in deferred_items:
            lines.append(
                f"- {item['title']} -> {item.get('suggested_target_refs_file')} "
                f"[priority={item.get('batch_priority')}, status={item.get('curation_status')}]"
            )
    else:
        lines.append("- None")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate daily curation batches from the curated queue.")
    parser.add_argument("--day", default=today_utc(), help="UTC day in YYYY-MM-DD format")
    args = parser.parse_args()

    queue = load_json(data_dir() / "curated_queue.json", [])
    if not isinstance(queue, list):
        queue = []

    active_items = [item for item in queue if item.get("curation_status", "queued") not in STATUS_EXCLUDE]
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    deferred_items: List[Dict[str, Any]] = []

    for item in active_items:
        target = item.get("suggested_target_refs_file", "refs/README.md")
        if item.get("curation_status") == "deferred":
            deferred_items.append(item)
            continue
        grouped[target].append(item)

    batches_dir = data_dir() / "curation_batches"
    ensure_directory(batches_dir)

    output_grouped: Dict[str, List[Dict[str, Any]]] = {}
    for target, items in grouped.items():
        batch_items = select_batch(items)
        output_grouped[target] = batch_items
        filename = f"{args.day}-{safe_name_from_refs(target)}.json"
        payload = {
            "day": args.day,
            "target_refs_file": target,
            "batch_size": len(batch_items),
            "items": batch_items,
        }
        write_json(batches_dir / filename, payload)

    summary_path = batches_dir / f"{args.day}-priority.md"
    summary_path.write_text(build_markdown(args.day, output_grouped, deferred_items), encoding="utf-8")
    print(f"curation_batches={len(output_grouped)} summary={summary_path.name}")


if __name__ == "__main__":
    main()
