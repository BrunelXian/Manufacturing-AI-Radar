from typing import Any, Dict, List

from utils import CURATION_TARGETS, DOMAIN_TAG_RULES, METHOD_TAG_RULES, PROCESS_TAG_RULES, data_dir, load_json, utc_now, write_json


PRIORITY_ORDER = [
    "defect-detection",
    "modelling",
    "control",
    "reinforcement-learning",
    "monitoring",
    "additive-manufacturing",
    "digital-twin",
]


def tag_scores(text: str, mapping: Dict[str, List[str]]) -> Dict[str, int]:
    lowered = text.lower()
    scores: Dict[str, int] = {}
    for tag, terms in mapping.items():
        hit_count = sum(1 for term in terms if term in lowered)
        if hit_count:
            scores[tag] = hit_count
    return scores


def assign_tags(record: Dict[str, Any]) -> Dict[str, Any]:
    text = f"{record.get('title', '')} {record.get('abstract', '')}".lower()
    enriched = dict(record)
    domain_scores = tag_scores(text, DOMAIN_TAG_RULES)
    process_scores = tag_scores(text, PROCESS_TAG_RULES)
    method_scores = tag_scores(text, METHOD_TAG_RULES)
    enriched["domain_tags"] = sorted(domain_scores.keys())
    enriched["process_tags"] = sorted(process_scores.keys())
    enriched["method_tags"] = sorted(method_scores.keys())
    enriched["domain_tag_scores"] = domain_scores
    enriched["process_tag_scores"] = process_scores
    enriched["method_tag_scores"] = method_scores
    return enriched


def pick_primary_domain(domain_scores: Dict[str, int]) -> str:
    if not domain_scores:
        return ""
    return sorted(domain_scores.items(), key=lambda item: (-item[1], PRIORITY_ORDER.index(item[0]) if item[0] in PRIORITY_ORDER else 999, item[0]))[0][0]


def pick_target_file(domain_tags: List[str], domain_scores: Dict[str, int]) -> str:
    primary = pick_primary_domain(domain_scores)
    if primary:
        return CURATION_TARGETS.get(primary, "refs/README.md")
    for tag in PRIORITY_ORDER:
        if tag in domain_tags:
            return CURATION_TARGETS[tag]
    return "refs/README.md"


def build_queue_entry(record: Dict[str, Any]) -> Dict[str, Any]:
    domain_tags = record.get("domain_tags") or []
    domain_scores = record.get("domain_tag_scores") or {}
    process_tags = record.get("process_tags") or []
    method_tags = record.get("method_tags") or []
    reasons = []
    if domain_tags:
        reasons.append(f"domain_tags={','.join(domain_tags)}")
    if process_tags:
        reasons.append(f"process_tags={','.join(process_tags)}")
    if method_tags:
        reasons.append(f"method_tags={','.join(method_tags)}")

    score = record.get("relevance_score") or 0
    if score >= 18:
        batch_priority = "high"
    elif score >= 13:
        batch_priority = "medium"
    else:
        batch_priority = "low"

    return {
        "id": record.get("id"),
        "title": record.get("title"),
        "source": record.get("source"),
        "year": record.get("year"),
        "url": record.get("url"),
        "primary_domain_tag": pick_primary_domain(domain_scores),
        "domain_tags": domain_tags,
        "process_tags": process_tags,
        "method_tags": method_tags,
        "relevance_score": record.get("relevance_score"),
        "why_selected": "; ".join(reasons),
        "batch_priority": batch_priority,
        "batch_reason": "High process relevance and fit for an existing curated refs page.",
        "curation_status": "queued",
        "last_reviewed_date": None,
        "suggested_target_refs_file": pick_target_file(domain_tags, domain_scores),
        "curation_note": "Review for process relevance, summarize method, and decide whether to promote into curated refs.",
    }


def should_queue(record: Dict[str, Any]) -> bool:
    if record.get("accepted_or_rejected") != "accepted":
        return False
    score = record.get("relevance_score") or 0
    domain_tags = record.get("domain_tags") or []
    process_tags = record.get("process_tags") or []
    domain_scores = record.get("domain_tag_scores") or {}
    high_value_domains = {"additive-manufacturing", "monitoring", "defect-detection", "modelling", "control", "reinforcement-learning", "digital-twin"}
    high_value_processes = {"lpbf", "ded", "welding", "machining", "bioprinting", "assembly"}
    return score >= 10 and bool(set(domain_tags) & high_value_domains or set(process_tags) & high_value_processes) and bool(domain_scores)


def main() -> None:
    screened_path = data_dir() / "screened_papers.json"
    screened_records = load_json(screened_path, [])
    previous_queue = load_json(data_dir() / "curated_queue.json", [])
    if not isinstance(screened_records, list):
        screened_records = []
    if not isinstance(previous_queue, list):
        previous_queue = []

    tagged_records = [assign_tags(record) for record in screened_records]
    write_json(screened_path, tagged_records)

    previous_by_id = {record.get("id"): record for record in previous_queue if record.get("id")}
    curated_queue = []
    for record in tagged_records:
        if not should_queue(record):
            continue
        queue_entry = build_queue_entry(record)
        previous = previous_by_id.get(queue_entry["id"])
        if previous and previous.get("relevance_score") == queue_entry["relevance_score"] and previous.get("suggested_target_refs_file") == queue_entry["suggested_target_refs_file"] and previous.get("primary_domain_tag") == queue_entry["primary_domain_tag"]:
            queue_entry["queued_at"] = previous.get("queued_at")
            queue_entry["curation_status"] = previous.get("curation_status", queue_entry["curation_status"])
            queue_entry["last_reviewed_date"] = previous.get("last_reviewed_date")
            queue_entry["batch_priority"] = previous.get("batch_priority", queue_entry["batch_priority"])
            queue_entry["batch_reason"] = previous.get("batch_reason", queue_entry["batch_reason"])
        else:
            queue_entry["queued_at"] = utc_now()
        curated_queue.append(queue_entry)
    curated_queue.sort(key=lambda item: (item.get("relevance_score") or 0, item.get("year") or 0, item.get("title") or ""), reverse=True)
    write_json(data_dir() / "curated_queue.json", curated_queue)
    print(f"tagged_records={len(tagged_records)} queue_entries={len(curated_queue)}")


if __name__ == "__main__":
    main()
