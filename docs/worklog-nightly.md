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

## 2026-04-14 03:05 +08:00

### What Was Done

- upgraded `refs/defect-detection.md` from a template into a curated page focused on process-relevant defect work
- upgraded `refs/modelling.md` into a curated page with an explicit scope boundary for process modelling
- selected additive-manufacturing and weld-related defect papers over generic industrial visual anomaly papers
- defined modelling to include process-response, thermal, melt-pool, surrogate, and process-to-property models while excluding generic scheduling or policy papers

### Why

These two domains were the next highest-value additions because they connect the repository's raw literature pool back to manufacturing quality logic and physically meaningful process understanding.

### Papers Selected

- defect-detection selections favored pore detection, LPBF defect reasoning, weld characterization, and non-contact or physics-aware inspection
- modelling selections favored thermal-field surrogates, physics-informed LPBF and DED models, melt-pool predictors, long-horizon temperature-field models, and process-to-property models

### What Was Excluded

- generic industrial anomaly-detection papers with weak process context
- pure dataset or benchmark papers without enough manufacturing-process insight for first-pass curation
- materials or simulation papers that lacked a clear manufacturing-process interpretation
- optimisation or RL papers whose main contribution was policy search rather than process modelling

### Scope Decisions

- `defect-detection.md` was kept focused on technically meaningful quality reasoning, not just surface-image classification
- `modelling.md` was defined around modelling process behavior and process-relevant outcomes, not around all manufacturing-related prediction tasks

### Current Judgement

- defect detection is now meaningful but still stronger in post-process and inspection-side work than in true in-situ detection
- modelling is now one of the clearer sections of the repository, but still heavily biased toward additive manufacturing
- the weakest remaining curated reference gap is now digital twin as a truly technical, non-generic section

### Next Steps

- add cross-links from radar pages into the newly curated `refs/` pages
- improve `refs/digital-twin.md` with selective curation rather than broad survey accumulation
- decide whether `refs/README.md` should start listing the strongest current curated pages more explicitly

## 2026-04-14 08:40 +08:00

### What Was Done

- refactored the literature system from a single scanner into a daily multi-stage pipeline
- added `scripts/utils.py` as the shared schema and rule utility layer
- refactored `scripts/literature_scanner.py` so it writes only to `data/raw_papers.json`
- added `paper_normalizer.py`, `paper_screener.py`, `tag_assigner.py`, and `daily_digest.py`
- created `data/raw_papers.json`, `data/screened_papers.json`, `data/curated_queue.json`, and `data/digests/`
- added GitHub Actions workflows for daily scanning and daily screening
- added `docs/daily_pipeline.md`
- locally validated the full flow from raw intake to digest generation

### Why The Data Layers Were Separated

- raw intake must remain broad and recoverable
- screening must be rule-based and reproducible without touching raw source data
- the curated queue must stay much smaller than the screened pool
- curated refs pages should only receive intentional manual or assisted handoff, never direct scanner output

### Screening Rules Used

- positive scoring uses manufacturing terms, process-relevant terms, and AI-method terms
- negative scoring uses lightweight exclusion terms for obviously weak-fit topics
- acceptance requires both manufacturing relevance and AI relevance, not just one of them
- queueing is stricter than screening so the daily shortlist does not flood review

### Design Choices

- raw ingestion and curated knowledge were kept strictly separate
- deduplication is based on normalized title, year, and first author rather than on query origin
- domain tagging stays rule-based for now, but queue handoff now prefers a primary domain instead of scattering one paper across many refs targets
- GitHub workflows only commit when tracked pipeline outputs actually change
- `screened_at` and `queued_at` are preserved when paper status is unchanged, reducing noisy workflow commits
- daily digests are skipped on days with no new activity unless a digest already exists for that date

### Where Future LLM Usage Should Be Inserted

- after rule-based screening, to refine ranking inside the curated queue
- after tagging, to generate structured curation notes
- before `refs/` handoff, to draft candidate summaries for human review

### Remaining Weaknesses

- domain tagging is still approximate and intentionally conservative
- queue targeting still leans heavily toward additive manufacturing because the current pool is AM-heavy
- the current workflows are robust enough for public GitHub Actions, but longer-running or more frequent intake may later need a self-hosted runner

## 2026-04-14 08:55 +08:00

### What Was Done

- extended curated-queue entries with batch-oriented metadata
- added `scripts/curation_batcher.py`
- created a new `data/curation_batches/` handoff layer
- updated the screening workflow so daily runs now generate curation batches after digests
- updated README and pipeline documentation to explain the difference between queue and batches

### Why

The repository had a shortlist, but not yet a sustainable review interface. The queue was still too close to a backlog. Daily curation batches turn that backlog into manageable review packets tied to specific `refs/` pages.

### Design Choices

- the queue remains the standing reservoir of promising papers
- batches are generated fresh from the queue each day rather than replacing the queue
- batches are grouped by `suggested_target_refs_file` so the review flow maps directly onto the curated refs structure
- batch size is intentionally capped to keep daily review realistic
- this layer still avoids direct auto-writing into `refs/`

### What Remains Manual

- deciding which batched papers are strong enough to promote into curated refs
- writing the final editorial summary and limitations text in `refs/*.md`
- marking items as deferred, curated, or rejected after review

### Next Steps

- optionally add a lightweight script to update `curation_status` after review
- make `refs/README.md` point to the latest curation batch process
- refine primary-domain routing for papers that naturally sit between additive manufacturing, modelling, and monitoring

## 2026-04-14 09:05 +08:00

### What Was Done

- added `scripts/queue_status_updater.py`
- enabled direct queue status updates by paper id or by batch file
- added optional `data/curation_history.json` support for status transitions
- updated documentation to explain how items leave active review through `curated`, `deferred`, or `rejected`

### Why

The pipeline needed a lightweight decision layer after review. Without status updates, the same papers would continue to appear as active items, making the daily workflow noisy and unsustainable.

### Design Choices

- the updater only modifies queue and review-tracking layers
- raw intake, screened records, and curated refs pages remain untouched
- status transitions are recorded with timestamps and optional notes
- the CLI supports both single-item updates and batch-file updates to keep daily review practical

### How Deferred And Rejected Items Behave

- deferred items remain in the queue but can be separated from active review in later passes
- rejected items remain in the queue history but should be excluded from future active daily review
- curated items indicate that the handoff to `refs/` has already happened

### Next Steps

- optionally filter deferred items more explicitly in the curation batch summary
- add a tiny review helper later if the repository owner wants quicker batch triage from the command line

## 2026-04-14 13:18 +08:00

### What Was Done

- upgraded `refs/README.md` into a real curated references entry point instead of a placeholder
- rewrote `scripts/curation_batcher.py` so it now generates clearer batch metadata, better priority summaries, and a stable `data/curation_batches/latest.md`
- improved batch summaries to show review order, target refs page, priority mix, effort estimate, and expected output
- updated top-level README and `docs/daily_pipeline.md` so the daily review surface is part of the documented workflow

### Why

The pipeline was already operational, but daily use still required too much orientation. The repository needed a low-friction entry point that answers three questions immediately: what exists in the curated layer, what should be reviewed today, and where reviewed papers should likely be absorbed.

### Design Choices

- kept `refs/README.md` as the stable navigation and maintenance page for curated knowledge
- added `data/curation_batches/latest.md` as the stable day-to-day review surface
- kept the dated priority markdown as the fuller handoff view rather than replacing it
- improved readability without adding a dashboard or a new data layer

### Current Judgement

- the repository now has a much clearer handoff between automated intake and manual curation
- first-time daily use should now be significantly easier because the review order and target refs pages are surfaced directly
- the next remaining usability improvement would be a small helper for turning reviewed batch items into draft curation notes, but that can wait
