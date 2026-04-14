# Daily Literature Pipeline

## Purpose

`Manufacturing-AI-Radar` now includes a daily literature pipeline that separates paper intake from curation.

The pipeline is designed to support stable daily accumulation of manufacturing-AI papers without polluting curated knowledge pages. Its role is to gather, normalize, screen, tag, and queue promising papers for later human or LLM-assisted curation into `refs/`.

## Pipeline Stages

### 1. Raw Intake

Source-of-truth file:

- `data/raw_papers.json`

The scanner queries arXiv and appends normalized raw records into the raw intake layer. These entries preserve discovery metadata such as source, query source, discovery time, and a deduplication key.

### 2. Normalization and Deduplication

Script:

- `scripts/paper_normalizer.py`

This stage standardizes titles, authors, year values, source fields, and deduplication keys. It also merges duplicate papers discovered through multiple search queries.

### 3. Rule-Based Screening

Source-of-truth file:

- `data/screened_papers.json`

Script:

- `scripts/paper_screener.py`

This stage applies lightweight rule-based screening. It is intentionally broad, but it tries to reject clearly irrelevant papers and downweight generic industrial AI papers that do not contribute much to process intelligence.

Screening metadata includes:

- `relevance_score`
- `screening_reason`
- `accepted_or_rejected`
- `screened_at`

### 4. Preliminary Tagging

Script:

- `scripts/tag_assigner.py`

This stage adds lightweight rule-based tags:

- `domain_tags`
- `process_tags`
- `method_tags`

It also builds the curated queue.

### 5. Curated Queue

Source-of-truth file:

- `data/curated_queue.json`

This file contains only the strongest screened candidates for future manual or LLM-assisted curation. It is intentionally stricter than the screening layer.

Each queue entry includes:

- `relevance_score`
- `why_selected`
- `suggested_target_refs_file`
- `curation_note`

### 6. Daily Digest

Source-of-truth directory:

- `data/digests/`

Script:

- `scripts/daily_digest.py`

The digest summarizes the daily paper flow:

- raw papers discovered
- accepted papers after screening
- domain distribution
- queue additions
- top high-priority papers

Both JSON and Markdown digests are generated per day.

## File Responsibilities

- `data/raw_papers.json`: raw but normalized intake layer
- `data/screened_papers.json`: screened and tagged research pool
- `data/curated_queue.json`: shortlist for future curation
- `data/checkpoint.json`: scan state for safe resume
- `data/scan_log.txt`: scanner operational log
- `data/digests/YYYY-MM-DD.json`: machine-readable daily digest
- `data/digests/YYYY-MM-DD.md`: human-readable daily digest

## Checkpointing

Checkpointing currently applies to the scan layer.

`data/checkpoint.json` records:

- `last_query`
- `last_query_index`
- `last_index`
- `last_run_time`

This allows the scanner to resume safely without rescanning the same offset range unnecessarily.

## Deduplication Logic

Deduplication is based on a stable key derived from:

- normalized title
- year
- first author

When the same paper appears under multiple search queries, normalization merges:

- authors
- categories
- query sources

This keeps raw intake broad while preventing query-level duplication from polluting later stages.

## Screening Rules

The current screener is intentionally lightweight and rule-based.

It uses:

- manufacturing keywords
- process-specific terms
- AI-method terms
- exclusion terms for obviously irrelevant topics

This is not a final relevance classifier. It is a pragmatic first-pass filter that keeps the pipeline stable and interpretable.

## What Remains Manual

The following should remain human-led for now:

- writing curated entries into `refs/`
- deciding which papers are genuinely representative
- drawing strong cross-domain conclusions
- resolving ambiguous scope cases between monitoring, modelling, control, and digital twin

## Where Future LLM Usage Should Be Inserted

Potential future LLM insertion points:

1. after rule-based screening, to refine queue prioritization
2. after tagging, to draft structured curation notes
3. before `refs/` handoff, to suggest concise summaries for human review

LLMs should not replace the raw intake, deduplication, or checkpointing layers.

## Running The Pipeline Locally

Run a scan batch:

```bash
python scripts/literature_scanner.py --batch-size 20
```

Then run the daily processing stages:

```bash
python scripts/paper_normalizer.py
python scripts/paper_screener.py
python scripts/tag_assigner.py
python scripts/daily_digest.py
```

## GitHub Actions

Two workflows are included:

- `.github/workflows/scan_daily.yml`
- `.github/workflows/screen_daily.yml`

They are designed for public GitHub Actions execution first. If the repository later needs heavier scanning cadence, longer-running jobs, or private data access, the same pipeline can be moved to a self-hosted runner without changing the data-layer structure.
