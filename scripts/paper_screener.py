from typing import Any, Dict, List, Optional

from utils import (
    AI_METHOD_TERMS,
    EXCLUSION_TERMS,
    MANUFACTURING_TERMS,
    PROCESS_PRIORITY_TERMS,
    data_dir,
    load_json,
    reason_text,
    score_keyword_hits,
    utc_now,
    write_json,
)


def screen_record(record: Dict[str, Any], previous: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    text = f"{record.get('title', '')} {record.get('abstract', '')}".lower()
    manufacturing_hits = score_keyword_hits(text, MANUFACTURING_TERMS)
    process_hits = score_keyword_hits(text, PROCESS_PRIORITY_TERMS)
    ai_hits = score_keyword_hits(text, AI_METHOD_TERMS)
    exclusion_hits = score_keyword_hits(text, EXCLUSION_TERMS)

    score = manufacturing_hits * 2 + process_hits * 2 + ai_hits - exclusion_hits * 3
    accepted = manufacturing_hits > 0 and ai_hits > 0 and score >= 4

    reasons: List[str] = []
    if manufacturing_hits:
        reasons.append(f"manufacturing_hits={manufacturing_hits}")
    if process_hits:
        reasons.append(f"process_hits={process_hits}")
    if ai_hits:
        reasons.append(f"ai_hits={ai_hits}")
    if exclusion_hits:
        reasons.append(f"exclusion_hits={exclusion_hits}")
    if not accepted:
        reasons.append("rejected_by_rule_threshold")

    screened = dict(record)
    screened.update(
        {
            "relevance_score": score,
            "accepted_or_rejected": "accepted" if accepted else "rejected",
            "screening_reason": reason_text(reasons),
        }
    )
    if previous and previous.get("relevance_score") == score and previous.get("accepted_or_rejected") == screened["accepted_or_rejected"] and previous.get("screening_reason") == screened["screening_reason"]:
        screened["screened_at"] = previous.get("screened_at")
    else:
        screened["screened_at"] = utc_now()
    return screened


def main() -> None:
    raw_records = load_json(data_dir() / "raw_papers.json", [])
    previous_screened = load_json(data_dir() / "screened_papers.json", [])
    if not isinstance(raw_records, list):
        raw_records = []
    if not isinstance(previous_screened, list):
        previous_screened = []

    previous_by_key = {record.get("dedup_key"): record for record in previous_screened if record.get("dedup_key")}

    screened_records = [screen_record(record, previous_by_key.get(record.get("dedup_key"))) for record in raw_records]
    screened_records.sort(key=lambda item: (item.get("relevance_score") or 0, item.get("year") or 0, item.get("title") or ""), reverse=True)
    write_json(data_dir() / "screened_papers.json", screened_records)
    accepted_count = sum(1 for record in screened_records if record.get("accepted_or_rejected") == "accepted")
    print(f"screened_records={len(screened_records)} accepted={accepted_count}")


if __name__ == "__main__":
    main()
