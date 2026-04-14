import argparse
from pathlib import Path
from typing import Any, Dict, List

from utils import data_dir, digest_counter, ensure_directory, load_json, today_utc, write_json


def filter_by_day(records: List[Dict[str, Any]], field: str, day: str) -> List[Dict[str, Any]]:
    return [record for record in records if str(record.get(field, "")).startswith(day)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a daily literature pipeline digest.")
    parser.add_argument("--day", default=today_utc(), help="UTC day in YYYY-MM-DD format")
    args = parser.parse_args()

    raw_records = load_json(data_dir() / "raw_papers.json", [])
    screened_records = load_json(data_dir() / "screened_papers.json", [])
    queue_records = load_json(data_dir() / "curated_queue.json", [])

    raw_today = filter_by_day(raw_records, "date_discovered", args.day)
    screened_today = filter_by_day(screened_records, "screened_at", args.day)
    accepted_today = [record for record in screened_today if record.get("accepted_or_rejected") == "accepted"]
    queued_today = filter_by_day(queue_records, "queued_at", args.day)

    domain_counts = digest_counter(tag for record in accepted_today for tag in (record.get("domain_tags") or []))
    top_queue = sorted(queued_today, key=lambda item: (item.get("relevance_score") or 0, item.get("year") or 0), reverse=True)[:10]

    digest = {
        "day": args.day,
        "raw_papers_discovered": len(raw_today),
        "new_unique_papers": len(raw_today),
        "accepted_after_screening": len(accepted_today),
        "added_to_curated_queue": len(queued_today),
        "top_domain_distributions": domain_counts,
        "top_high_priority_papers": [
            {
                "title": item.get("title"),
                "year": item.get("year"),
                "url": item.get("url"),
                "domain_tags": item.get("domain_tags"),
                "relevance_score": item.get("relevance_score"),
                "suggested_target_refs_file": item.get("suggested_target_refs_file"),
            }
            for item in top_queue
        ],
    }

    digest_dir = data_dir() / "digests"
    ensure_directory(digest_dir)
    json_path = digest_dir / f"{args.day}.json"
    md_path = digest_dir / f"{args.day}.md"
    if digest["raw_papers_discovered"] == 0 and digest["accepted_after_screening"] == 0 and digest["added_to_curated_queue"] == 0 and not json_path.exists():
        print("digest_skipped=no_daily_changes")
        return
    write_json(json_path, digest)

    md_lines = [
        f"# Daily Digest - {args.day}",
        "",
        f"- Raw papers discovered: {digest['raw_papers_discovered']}",
        f"- New unique papers: {digest['new_unique_papers']}",
        f"- Accepted after screening: {digest['accepted_after_screening']}",
        f"- Added to curated queue: {digest['added_to_curated_queue']}",
        "",
        "## Top Domain Distribution",
        "",
    ]
    for tag, count in sorted(domain_counts.items(), key=lambda item: item[1], reverse=True):
        md_lines.append(f"- {tag}: {count}")
    md_lines.extend(["", "## Top High-Priority Papers", ""])
    for item in digest["top_high_priority_papers"]:
        md_lines.append(f"- {item['title']} ({item['year']}) -> {item['suggested_target_refs_file']} [score={item['relevance_score']}]")
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    print(f"digest_generated={json_path.name}")


if __name__ == "__main__":
    main()
