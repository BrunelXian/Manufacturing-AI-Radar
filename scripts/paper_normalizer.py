from pathlib import Path
from typing import Any, Dict, List

from utils import (
    build_dedup_key,
    data_dir,
    load_json,
    merge_paper_records,
    normalize_author_name,
    normalize_title,
    normalize_whitespace,
    utc_now,
    write_json,
)


def normalize_record(record: Dict[str, Any]) -> Dict[str, Any]:
    authors = [normalize_author_name(author) for author in record.get("authors") or [] if normalize_author_name(author)]
    title = normalize_whitespace(record.get("title", ""))
    abstract = normalize_whitespace(record.get("abstract", ""))
    year = record.get("year")
    try:
        year = int(year) if year is not None else None
    except (TypeError, ValueError):
        year = None

    source = normalize_whitespace(record.get("source", "arxiv")).lower()
    query_sources = record.get("query_sources") or [record.get("query_source", "unknown")]

    normalized = {
        "id": record.get("id"),
        "source": source,
        "source_id": record.get("source_id"),
        "title": title,
        "normalized_title": normalize_title(title),
        "authors": authors,
        "year": year,
        "abstract": abstract,
        "url": normalize_whitespace(record.get("url", "")),
        "categories": sorted(set(record.get("categories") or [])),
        "query_source": record.get("query_source", query_sources[0] if query_sources else "unknown"),
        "query_sources": sorted(set(query_sources)),
        "date_discovered": record.get("date_discovered") or utc_now(),
        "dedup_key": record.get("dedup_key") or build_dedup_key(title, year, authors),
    }
    return normalized


def main() -> None:
    raw_path = data_dir() / "raw_papers.json"
    records = load_json(raw_path, [])
    if not isinstance(records, list):
        records = []

    normalized_records: List[Dict[str, Any]] = [normalize_record(record) for record in records]
    merged_records = merge_paper_records(normalized_records)
    write_json(raw_path, merged_records)
    print(f"normalized_records={len(merged_records)}")


if __name__ == "__main__":
    main()
