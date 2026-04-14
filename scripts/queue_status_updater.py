import argparse
from pathlib import Path
from typing import Any, Dict, List, Optional

from utils import data_dir, load_json, utc_now, write_json


VALID_STATUSES = {"queued", "batched", "curated", "deferred", "rejected"}


def load_batch_items(batch_path: Path) -> List[str]:
    payload = load_json(batch_path, {})
    if isinstance(payload, dict) and "items" in payload:
        return [item.get("id") for item in payload.get("items", []) if item.get("id")]
    return []


def update_record(record: Dict[str, Any], new_status: str, note: Optional[str]) -> Dict[str, Any]:
    updated = dict(record)
    updated["curation_status"] = new_status
    updated["status_updated_at"] = utc_now()
    updated["status_note"] = note
    updated["last_reviewed_date"] = updated["status_updated_at"][:10]
    return updated


def build_history_entry(record_id: str, previous_status: str, new_status: str, note: Optional[str]) -> Dict[str, Any]:
    return {
        "id": record_id,
        "previous_status": previous_status,
        "new_status": new_status,
        "updated_at": utc_now(),
        "note": note,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Update curation status for queue items.")
    parser.add_argument("--id", action="append", dest="ids", default=[], help="Queue item id to update. Can be provided multiple times.")
    parser.add_argument("--batch-file", help="Path to a curation batch JSON file.")
    parser.add_argument("--status", required=True, choices=sorted(VALID_STATUSES), help="New curation status.")
    parser.add_argument("--note", help="Optional short note for the status update.")
    args = parser.parse_args()

    target_ids = list(args.ids)
    if args.batch_file:
        target_ids.extend(load_batch_items(Path(args.batch_file)))
    target_ids = sorted(set(target_ids))

    if not target_ids:
        raise SystemExit("No queue item ids provided. Use --id or --batch-file.")

    queue_path = data_dir() / "curated_queue.json"
    history_path = data_dir() / "curation_history.json"

    queue = load_json(queue_path, [])
    history = load_json(history_path, [])
    if not isinstance(queue, list):
        queue = []
    if not isinstance(history, list):
        history = []

    updated_count = 0
    new_queue: List[Dict[str, Any]] = []
    for record in queue:
        record_id = record.get("id")
        if record_id not in target_ids:
            new_queue.append(record)
            continue

        previous_status = record.get("curation_status", "queued")
        updated_record = update_record(record, args.status, args.note)
        new_queue.append(updated_record)
        history.append(build_history_entry(record_id, previous_status, args.status, args.note))
        updated_count += 1

    write_json(queue_path, new_queue)
    write_json(history_path, history)
    print(f"updated_queue_items={updated_count}")


if __name__ == "__main__":
    main()
