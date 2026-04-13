# Nightly Worklog

## 2026-04-14 01:59 +08:00

### What Was Done

- inspected the repository state
- confirmed that the repository contained only a single `README.md`
- identified the main gap as missing structure rather than missing polish
- rebuilt the repository into a research-navigation layout
- rewrote `README.md` to clarify scope, positioning, and maintenance logic
- created foundational documents in `docs/`
- created first-wave radar domain pages in `radar/`
- created roadmap and maintenance guidance
- added placeholder guidance files for `notes/`, `refs/`, and `assets/`
- normalized terminology to keep spelling and naming consistent across the repository

### Why

The initial repository state was too thin to function as a public-facing research project. A stronger first milestone required stable structure, consistent document roles, and enough topic depth that new contributors can understand how to extend the project.

### Issues Encountered

- the repository was not present locally as a Git working copy, so work proceeded as direct file creation inside the local project folder
- the original structure existed only conceptually in the README, so architectural decisions had to be made from scratch

### Decisions Made

- kept the top-level structure shallow to reduce maintenance cost
- treated the repository as a knowledge system rather than a codebase
- used English-first documentation for consistency and wider reach
- separated stable framework docs from topic-specific radar pages

### Next Steps

- expand `modelling.md` and `digital-twin.md` with more cross-links after the first public version settles
- add structured reference files for representative papers by domain
- add tool and dataset maps once topic boundaries are stable

## 2026-04-14 02:20 +08:00

### What Was Done

- created domain-specific `refs/` pages for future curated paper mapping
- created reusable literature note templates under `notes/`
- implemented `scripts/literature_scanner.py` for arXiv scanning
- added `data/papers.json`, `data/checkpoint.json`, and `data/scan_log.txt`
- documented scanner behavior in `docs/literature_scanning.md`
- refined arXiv query syntax to use fielded boolean search rather than loose natural-language matching
- ran multiple scanning batches and populated the initial paper store
- started a background scanner process to continue unattended collection
- added internal links across `README`, `refs`, `notes`, `docs`, and key radar pages

### Why

The repository needed a bridge between high-level radar structure and a growing evidence base. The scanner provides that bridge by collecting broad candidate literature automatically, while the `refs/` and `notes/` structure keeps later curation disciplined.

### Issues Encountered

- the first query style was too loose for arXiv and returned mostly unrelated papers
- this was corrected by switching to fielded boolean queries such as `all:"additive manufacturing" AND all:"machine learning"`

### Decisions Made

- keep filtering broad enough to collect candidate papers, but strong enough to reject obviously unrelated records
- separate raw harvested metadata in `data/` from curated knowledge pages in `refs/`
- use templates in `notes/` as the intermediate layer between automated scan output and repository synthesis

### What Remains

- review scanner output quality over longer unattended runs
- decide whether to add domain tagging or confidence scoring to scanned papers
- begin promoting representative papers from `data/papers.json` into curated `refs/` entries
