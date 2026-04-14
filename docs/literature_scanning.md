# Literature Scanning

## Purpose

This repository includes an automated literature scanner to collect candidate arXiv papers relevant to AI in manufacturing.

The goal is not to auto-curate the final radar directly. The scanner is the raw-intake layer of a broader daily pipeline that gathers structured metadata, keeps progress checkpoints, and supports later screening, tagging, queueing, and manual curation into `refs/` and `notes/`.

## Script Location

- [scripts/literature_scanner.py](../scripts/literature_scanner.py)

## What The Scanner Does

The scanner:

- queries arXiv with multiple manufacturing-AI search phrases
- retrieves paper metadata
- stores raw intake records in `data/raw_papers.json`
- saves scan progress in `data/checkpoint.json`
- appends operational logs to `data/scan_log.txt`

## Query Set

The initial query set includes:

- `additive manufacturing machine learning`
- `LPBF machine learning`
- `LDED machine learning`
- `welding machine learning`
- `manufacturing reinforcement learning`
- `process monitoring machine learning`
- `digital twin manufacturing AI`
- `defect detection manufacturing deep learning`

These can be expanded later as domain coverage becomes more precise.

## Stored Data

Each paper record in `data/raw_papers.json` contains:

- `id`
- `source`
- `title`
- `authors`
- `year`
- `abstract`
- `url`
- `categories`
- `query_source`
- `date_discovered`
- `dedup_key`

## Checkpointing

The checkpoint file records:

- `last_query`
- `last_query_index`
- `last_index`
- `last_run_time`

This allows the scanner to resume from the last unfinished query position rather than starting over every time.

## Running The Scanner

Run one batch:

```bash
python scripts/literature_scanner.py
```

Run continuously:

```bash
python scripts/literature_scanner.py
```

## How Results Should Be Used

The scanner output is intentionally broad. Candidate papers from `data/raw_papers.json` should later be:

1. normalized and deduplicated
2. screened for relevance
3. tagged into preliminary domains
4. placed into `data/curated_queue.json`
5. summarized with `notes/paper-note-template.md`
6. promoted into curated domain reference pages under `refs/`

Relevant repository destinations:

- [refs/README.md](../refs/README.md)
- [notes/paper-note-template.md](../notes/paper-note-template.md)
- [notes/domain-scan-template.md](../notes/domain-scan-template.md)
- [daily_pipeline.md](daily_pipeline.md)

## Current Limitations

- the system currently targets arXiv only
- daily screening and tagging are still rule-based
- final curation still requires human review

## Next Planned Improvements

- stronger query grouping by radar domain
- richer queue prioritization
- optional LLM-assisted triage after the rule-based stage
- better handoff from curated queue into `refs/`
