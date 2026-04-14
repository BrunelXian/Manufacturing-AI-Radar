import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List

from utils import data_dir, ensure_directory, load_json, today_utc, write_json


PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
STATUS_EXCLUDE = {"curated", "rejected"}
MAX_BATCH_SIZE = 8

REVIEW_NOTES = {
    "refs/additive-manufacturing.md": "Best place to absorb process-intelligence papers that connect sensing, modelling, and quality logic in LPBF, DED, or WAAM-like settings.",
    "refs/monitoring.md": "Useful for strengthening observability coverage, especially when a paper improves state estimation, sensor fusion, or deployment realism.",
    "refs/defect-detection.md": "Worth reviewing when a paper ties defect identification back to manufacturing quality logic rather than generic surface inspection.",
    "refs/modelling.md": "Important for physically meaningful process-response models, surrogates, and thermal or microstructure prediction work.",
    "refs/control.md": "Reserve for papers that clearly change the process or support real-time intervention rather than passive prediction.",
    "refs/reinforcement-learning.md": "Use for manufacturing-specific sequential decision papers, especially when the action design is process-aware.",
    "refs/digital-twin.md": "Keep selective and technical. Prioritize twin architectures that meaningfully connect sensing, modelling, and decision support.",
    "refs/README.md": "Use only when a paper improves repository-wide framing rather than one specific domain page.",
}


def safe_name_from_refs(target: str) -> str:
    return Path(target).stem


def queue_sort_key(item: Dict[str, Any]) -> tuple[Any, ...]:
    return (
        PRIORITY_ORDER.get(item.get("batch_priority", "low"), 99),
        -(item.get("relevance_score") or 0),
        -(item.get("year") or 0),
        item.get("title") or "",
    )


def select_batch(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(items, key=queue_sort_key)[:MAX_BATCH_SIZE]


def highest_priority(items: List[Dict[str, Any]]) -> str:
    priorities = [item.get("batch_priority", "low") for item in items]
    return min(priorities, key=lambda value: PRIORITY_ORDER.get(value, 99))


def priority_mix(items: List[Dict[str, Any]]) -> str:
    counts = Counter(item.get("batch_priority", "low") for item in items)
    ordered_parts = []
    for priority in ["high", "medium", "low"]:
        count = counts.get(priority, 0)
        if count:
            ordered_parts.append(f"{count} {priority}")
    return ", ".join(ordered_parts) if ordered_parts else "none"


def estimate_effort(batch_size: int) -> str:
    if batch_size <= 2:
        return "light review, about 10-15 minutes"
    if batch_size <= 5:
        return "moderate review, about 20-30 minutes"
    return "focused review, about 30-45 minutes"


def expected_output(target: str, batch_size: int) -> str:
    if batch_size <= 2:
        return f"Decide quickly whether to absorb these papers into `{target}` or mark them deferred."
    return f"Promote 1-2 strong entries into `{target}` and record status updates for the remainder."


def batch_note(target: str) -> str:
    return REVIEW_NOTES.get(
        target,
        "Review for process relevance first, then decide whether the batch strengthens an existing curated refs page.",
    )


def build_batch_payload(day: str, target: str, items: List[Dict[str, Any]]) -> Dict[str, Any]:
    batch_items = select_batch(items)
    return {
        "day": day,
        "target_refs_file": target,
        "batch_size": len(batch_items),
        "highest_priority": highest_priority(batch_items),
        "priority_mix": priority_mix(batch_items),
        "batch_reason": batch_items[0].get("batch_reason") if batch_items else None,
        "review_note": batch_note(target),
        "estimated_effort": estimate_effort(len(batch_items)),
        "expected_output": expected_output(target, len(batch_items)),
        "items": batch_items,
    }


def sort_batches(batch_payloads: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(
        batch_payloads,
        key=lambda payload: (
            PRIORITY_ORDER.get(payload.get("highest_priority", "low"), 99),
            -max((item.get("relevance_score") or 0) for item in payload.get("items", [])),
            payload.get("target_refs_file") or "",
        ),
    )


def build_priority_markdown(day: str, batches: List[Dict[str, Any]], deferred_items: List[Dict[str, Any]]) -> str:
    lines = [
        f"# Curation Batches - {day}",
        "",
        "This file is the daily handoff view from the curated queue into reviewable curation batches.",
        "",
        "Workflow:",
        "`scan -> screen -> tag -> queue -> curation batches -> review decision -> status update -> curated refs update`",
        "",
    ]

    for priority in ["high", "medium", "low"]:
        priority_batches = [batch for batch in batches if batch.get("highest_priority") == priority]
        lines.append(f"## {priority.title()} Priority Batches")
        lines.append("")
        if not priority_batches:
            lines.append("- None")
            lines.append("")
            continue

        for batch in priority_batches:
            target = batch["target_refs_file"]
            batch_filename = f"{day}-{safe_name_from_refs(target)}.json"
            lines.append(f"### {batch['review_order']}. {target}")
            lines.append("")
            lines.append(f"- Target refs page: `{target}`")
            lines.append(f"- Batch file: `{batch_filename}`")
            lines.append(f"- Papers in batch: {batch['batch_size']}")
            lines.append(f"- Priority mix: {batch['priority_mix']}")
            lines.append(f"- Suggested review order: {batch['review_order']}")
            lines.append(f"- Why this batch matters: {batch['review_note']}")
            lines.append(f"- Estimated effort: {batch['estimated_effort']}")
            lines.append(f"- Expected output: {batch['expected_output']}")
            lines.append("- Candidate papers:")
            for item in batch["items"]:
                lines.append(
                    f"  - {item['title']} ({item.get('year')}) "
                    f"[score={item.get('relevance_score')}, status={item.get('curation_status')}]"
                )
            lines.append("")

    lines.append("## Deferred Items")
    lines.append("")
    if deferred_items:
        for item in sorted(deferred_items, key=queue_sort_key):
            lines.append(
                f"- {item['title']} -> {item.get('suggested_target_refs_file')} "
                f"[priority={item.get('batch_priority')}, last_reviewed={item.get('last_reviewed_date')}]"
            )
    else:
        lines.append("- None")
    lines.append("")
    return "\n".join(lines)


def build_latest_markdown(day: str, batches: List[Dict[str, Any]], deferred_items: List[Dict[str, Any]]) -> str:
    lines = [
        "# Today's Review Surface",
        "",
        f"- Latest generated day: `{day}`",
        f"- Primary summary: `{day}-priority.md`",
        "- Use this file as the first daily review entry point.",
        "",
        "## How To Use This Page",
        "",
        "1. Open the dated priority summary for fuller context.",
        "2. Review high-priority batches first and work down only if time remains.",
        "3. After review, update queue status and then promote the strongest papers into the target `refs/*.md` page.",
        "",
    ]

    for priority in ["high", "medium", "low"]:
        priority_batches = [batch for batch in batches if batch.get("highest_priority") == priority]
        lines.append(f"## {priority.title()} Priority Review")
        lines.append("")
        if not priority_batches:
            lines.append("- None")
            lines.append("")
            continue
        for batch in priority_batches:
            batch_filename = f"{day}-{safe_name_from_refs(batch['target_refs_file'])}.json"
            lines.append(
                f"- Review order {batch['review_order']}: `{batch['target_refs_file']}` "
                f"via `{batch_filename}`"
            )
            lines.append(
                f"  Papers={batch['batch_size']}; mix={batch['priority_mix']}; effort={batch['estimated_effort']}"
            )
            lines.append(f"  Why now: {batch['review_note']}")
        lines.append("")

    lines.append("## Deferred Items")
    lines.append("")
    if deferred_items:
        lines.append(f"- Deferred candidates currently tracked: {len(deferred_items)}")
        lines.append("  Revisit only after higher-priority batches have been cleared.")
    else:
        lines.append("- No deferred items are currently blocking the daily review surface.")
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

    batch_payloads = [build_batch_payload(args.day, target, items) for target, items in grouped.items()]
    ordered_batches = sort_batches(batch_payloads)

    for review_order, payload in enumerate(ordered_batches, start=1):
        payload["review_order"] = review_order
        filename = f"{args.day}-{safe_name_from_refs(payload['target_refs_file'])}.json"
        write_json(batches_dir / filename, payload)

    summary_path = batches_dir / f"{args.day}-priority.md"
    latest_path = batches_dir / "latest.md"
    summary_path.write_text(build_priority_markdown(args.day, ordered_batches, deferred_items), encoding="utf-8")
    latest_path.write_text(build_latest_markdown(args.day, ordered_batches, deferred_items), encoding="utf-8")
    print(f"curation_batches={len(ordered_batches)} summary={summary_path.name} latest={latest_path.name}")


if __name__ == "__main__":
    main()
