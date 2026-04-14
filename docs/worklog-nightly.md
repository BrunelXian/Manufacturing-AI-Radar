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

## 2026-04-14 02:45 +08:00

### What Was Done

- reviewed the initial `data/papers.json` pool and shortlisted papers for the first curated mapping pass
- upgraded `refs/additive-manufacturing.md` from a template into a curated domain page with representative entries
- upgraded `refs/monitoring.md` into a curated page focused on observability, soft sensing, and deployable monitoring
- upgraded `refs/control.md` into a selective page centered on MPC, surrogate-enabled decision-making, and control-adjacent enabling work
- upgraded `refs/reinforcement-learning.md` into a curated page that distinguishes process-level RL from operations-level RL

### Why

The repository had already reached the raw collection stage, but it still needed interpretation. Curated `refs/` pages are the first real step from harvested metadata toward a usable research map.

### Papers Selected

- additive manufacturing papers were selected when they connected LPBF or DED process physics, multimodal sensing, defect reasoning, or material-response modelling
- monitoring papers were selected when they improved process observability, interpretability, or deployment realism
- control papers were selected conservatively because the current pool has few genuine closed-loop manufacturing papers
- reinforcement learning papers were selected when they represented either process-level decision-making, robotic manufacturing skills, or clearly manufacturing-specific sequential decisions

### What Was Excluded

- generic industrial anomaly-detection or defect-vision papers with weak process-intelligence relevance
- broad digital-twin or survey-style papers that were too high-level for first-pass curation
- scheduling papers that did not add much beyond standard operations framing
- additive-manufacturing papers that looked interesting but were still too far from process intelligence or quality reasoning

### Current Judgement

- additive manufacturing is already strong enough for a meaningful first curated map
- monitoring is usable but still skewed toward process-industry style papers and LPBF
- control remains the thinnest high-value area in the current pool
- reinforcement learning is presently stronger in scheduling and robotic tasks than in direct process control

### Next Steps

- promote the next strongest papers into `refs/defect-detection.md` and `refs/modelling.md`
- add light cross-links from radar pages to the newly curated references
- keep the scanner running in the background, but focus manual effort on curation rather than raw volume
