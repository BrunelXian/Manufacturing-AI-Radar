# Curated References

`refs/` is the repository's curated literature layer.

It is where selected papers are turned into structured reference pages that help explain the field, not just collect titles. These pages sit downstream of the scanner, screener, queue, and daily batch system. Their job is to absorb the strongest papers into a stable research map.

## What Lives Here

The current `refs/` structure mixes two maturity levels:

- curated domain pages that already contain representative entries
- scaffold pages that still need deeper editorial build-out

Current pages:

- [additive-manufacturing.md](additive-manufacturing.md): Curated. Process-intelligence papers for LPBF, DED, WAAM, multimodal sensing, thermal reasoning, and quality inference.
- [monitoring.md](monitoring.md): Curated. Manufacturing process observability, soft sensing, interpretable monitoring, and deployable sensing pipelines.
- [defect-detection.md](defect-detection.md): Curated. Process-relevant defect identification, pore and crack reasoning, inspection workflows, and manufacturing quality interpretation.
- [modelling.md](modelling.md): Curated. Surrogate models, physics-informed process models, and process-response prediction with clear manufacturing grounding.
- [control.md](control.md): Curated. Closed-loop, MPC-adjacent, or intervention-oriented papers where AI influences manufacturing actions.
- [reinforcement-learning.md](reinforcement-learning.md): Curated. Sequential decision papers for manufacturing processes, robotic skills, and manufacturing-specific RL framing.
- [digital-twin.md](digital-twin.md): Early scaffold. Reserved for selective digital-twin papers that meaningfully connect sensing, modelling, and decision support.

## How Papers Reach `refs/`

The intended flow is:

`scan -> screen -> tag -> queue -> curation batches -> review decision -> curated refs update`

In practice:

1. `data/raw_papers.json` holds broad intake.
2. `data/screened_papers.json` keeps rule-based accepted records.
3. `data/curated_queue.json` holds the shortlist worth human review.
4. `data/curation_batches/latest.md` and the dated batch files tell you what to review today.
5. The best reviewed papers are promoted into the appropriate `refs/*.md` page.

`refs/README.md` is the stable navigation page for the curated knowledge layer. Daily batch summaries are temporary review surfaces for deciding what should be absorbed next.

## Editorial Standard

Papers should be included here only when they help the radar explain something meaningful about manufacturing AI.

Use these inclusion standards:

- clear manufacturing-process relevance, not just industrial branding
- useful technical signal for sensing, modelling, defect reasoning, control, or deployment
- enough specificity that the paper strengthens the knowledge map rather than broadening it noisily
- a natural fit with one target `refs/*.md` page

Avoid promoting papers when they are:

- generic industrial inspection with weak process context
- mostly methodological with little manufacturing grounding
- too broad, survey-like, or architectural to strengthen one curated page
- better treated as queue items until scope is clearer

## How To Maintain This Layer

When reviewing a daily batch:

1. Open [../data/curation_batches/latest.md](../data/curation_batches/latest.md).
2. Start with the highest-priority batch and open its target refs page.
3. Promote only the strongest items into structured curated entries.
4. Mark queue items as `curated`, `deferred`, or `rejected` after review.
5. Keep page scope boundaries clean. If a paper fits two domains, choose the page where it contributes the strongest explanation.

## Current Gaps And Priority Areas

The current curated layer is strongest in additive manufacturing, monitoring, defect detection, and modelling.

The next priority areas are:

- more technically selective digital-twin coverage
- stronger true in-situ defect-detection papers
- more genuine closed-loop control papers rather than control-adjacent modelling
- reinforcement-learning papers that operate at process level rather than only scheduling level
- better cross-links between additive-manufacturing, monitoring, modelling, and control entries

## Daily Review Entry Points

If you are reviewing the repository today, start here:

- [../data/curation_batches/latest.md](../data/curation_batches/latest.md)
- [../docs/daily_pipeline.md](../docs/daily_pipeline.md)

If you are updating long-lived curated knowledge, stay here in `refs/` and use the daily batch files only as intake support.
