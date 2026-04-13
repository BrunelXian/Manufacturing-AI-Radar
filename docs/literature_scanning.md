# Literature Scanning

## Purpose

This repository includes an automated literature scanner to collect candidate arXiv papers relevant to AI in manufacturing.

The goal is not to auto-curate the final radar directly. The scanner is a harvesting layer that gathers structured metadata, keeps progress checkpoints, and supports future manual review into `refs/` and `notes/`.

## Script Location

- [scripts/literature_scanner.py](../scripts/literature_scanner.py)

## What The Scanner Does

The scanner:

- queries arXiv with multiple manufacturing-AI search phrases
- retrieves paper metadata
- applies a lightweight manufacturing relevance filter
- stores deduplicated paper records in `data/papers.json`
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

Each paper record in `data/papers.json` contains:

- `title`
- `authors`
- `year`
- `arxiv_id`
- `abstract`
- `url`
- `categories`
- `query_source`

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
python scripts/literature_scanner.py --loop
```

Run continuously with a shorter pause:

```bash
python scripts/literature_scanner.py --loop --sleep-seconds 30
```

## How Results Should Be Used

The scanner output is intentionally broad. Candidate papers from `data/papers.json` should later be:

1. screened for relevance
2. summarized with `notes/paper-note-template.md`
3. promoted into curated domain reference pages under `refs/`

Relevant repository destinations:

- [refs/README.md](../refs/README.md)
- [notes/paper-note-template.md](../notes/paper-note-template.md)
- [notes/domain-scan-template.md](../notes/domain-scan-template.md)

## Current Limitations

- filtering is intentionally simple and may admit false positives
- the system currently targets arXiv only
- final curation still requires human review

## Next Planned Improvements

- stronger query grouping by radar domain
- richer filtering and tagging
- paper export by domain into `refs/`
- optional scheduled or background execution support
