# Manufacturing-AI-Radar
<h1 align="center">Manufacturing-AI-Radar</h1>

<p align="center"><strong>A structured research map for Artificial Intelligence in Manufacturing</strong></p>
<p align="center"><strong>Manufacturing-AI-Radar organizes the technical landscape of AI for manufacturing across processes, sensing, modelling, control, and industrial deployment.</strong></p>

[![Project Type](https://img.shields.io/badge/project-research%20radar-blue)](#)
[![Focus](https://img.shields.io/badge/focus-AI%20for%20Manufacturing-important)](#)
[![Scope](https://img.shields.io/badge/scope-processes%2C%20control%2C%20digital%20twin-success)](#)

Manufacturing-AI-Radar is a structured research navigation project for AI in manufacturing.

It is designed to map how artificial intelligence is used across manufacturing processes, system architectures, and industrial decision loops. Rather than acting as a generic paper list, the repository aims to become a maintainable knowledge map that helps readers understand where AI is being applied, why it matters, and how technical directions relate to one another.

## Project Overview

Artificial intelligence is becoming increasingly important in manufacturing, but the landscape remains fragmented across additive manufacturing, process monitoring, quality inspection, control engineering, robotics, digital twins, and industrial software.

This repository organizes that landscape so researchers, engineers, and students can quickly understand:

- what problems AI is solving in manufacturing
- which methods are used in which contexts
- how sensing, prediction, control, and deployment connect
- where meaningful research and implementation opportunities remain open

## Why This Repository

Most existing AI repositories fall into one of three patterns:

- broad AI resource collections with little manufacturing context
- paper lists organized by method rather than industrial problem
- personal notes that are difficult to extend systematically

Manufacturing-AI-Radar takes a different approach. It treats AI for manufacturing as a structured technical landscape with interacting layers:

- physical processes
- sensing and data acquisition
- monitoring and diagnosis
- modelling and prediction
- optimisation and control
- industrial deployment

This makes the repository more useful as a long-term research map than as a static reading list.

## Scope

The first development stage focuses on:

- Additive Manufacturing
- Process Monitoring
- Defect Detection
- Process Modelling
- Closed-loop Control
- Reinforcement Learning for Manufacturing
- Digital Twin and Intelligent Manufacturing

The scope is intentionally centered on AI that interacts with physical manufacturing systems, including process physics, sensor streams, production decisions, and industrial deployment constraints.

Out of scope for now:

- generic AI tutorials without manufacturing grounding
- pure software engineering AI workflows
- broad digitization topics with no clear AI component

## Repository Structure

```text
Manufacturing-AI-Radar/
+-- README.md
+-- docs/
|   +-- architecture.md
|   +-- taxonomy.md
|   +-- contribution_guide.md
|   +-- maintenance.md
|   +-- literature_scanning.md
|   +-- daily_pipeline.md
|   `-- worklog-nightly.md
+-- radar/
|   +-- additive-manufacturing.md
|   +-- monitoring.md
|   +-- defect-detection.md
|   +-- modelling.md
|   +-- control.md
|   +-- reinforcement-learning.md
|   `-- digital-twin.md
+-- notes/
|   +-- README.md
|   +-- paper-note-template.md
|   +-- domain-scan-template.md
|   `-- weekly-scan-template.md
+-- refs/
|   +-- README.md
|   +-- additive-manufacturing.md
|   +-- monitoring.md
|   +-- defect-detection.md
|   +-- modelling.md
|   +-- control.md
|   +-- reinforcement-learning.md
|   `-- digital-twin.md
+-- roadmap/
|   `-- roadmap.md
+-- scripts/
|   +-- literature_scanner.py
|   +-- paper_normalizer.py
|   +-- paper_screener.py
|   +-- tag_assigner.py
|   +-- daily_digest.py
|   +-- curation_batcher.py
|   +-- queue_status_updater.py
|   `-- utils.py
+-- data/
|   +-- raw_papers.json
|   +-- screened_papers.json
|   +-- curated_queue.json
|   +-- checkpoint.json
|   +-- scan_log.txt
|   +-- curation_batches/
|   +-- curation_history.json
|   `-- digests/
`-- assets/
    `-- README.md
```

## Core Radar Domains

### Additive Manufacturing

AI methods for process understanding, quality prediction, parameter selection, in-situ monitoring, defect prevention, and adaptive control in systems such as `LPBF`, `DED`, and `WAAM`.

### Process Monitoring

Techniques for observing manufacturing states from thermal, optical, acoustic, vibration, and multimodal sensor data.

### Defect Detection

Methods for detecting, segmenting, or predicting defects during production or post-process inspection, with attention to industrial interpretability.

### Process Modelling

Data-driven and hybrid models that estimate process behavior, quality outcomes, uncertainty, and state evolution.

### Closed-loop Control

AI-assisted control systems that adapt parameters during manufacturing in response to observed or predicted process conditions.

### Reinforcement Learning for Manufacturing

Sequential decision-making methods for process control, robotics, and adaptive optimisation under uncertainty.

### Digital Twin and Intelligent Manufacturing

Integrated virtual-physical system views that connect sensing, modelling, prediction, simulation, optimisation, and decision support.

Core pages:

- [docs/taxonomy.md](docs/taxonomy.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/literature_scanning.md](docs/literature_scanning.md)
- [docs/daily_pipeline.md](docs/daily_pipeline.md)
- [radar/additive-manufacturing.md](radar/additive-manufacturing.md)
- [radar/monitoring.md](radar/monitoring.md)
- [radar/defect-detection.md](radar/defect-detection.md)
- [radar/modelling.md](radar/modelling.md)
- [radar/control.md](radar/control.md)
- [radar/reinforcement-learning.md](radar/reinforcement-learning.md)
- [radar/digital-twin.md](radar/digital-twin.md)
- [refs/README.md](refs/README.md)
- [notes/README.md](notes/README.md)

## Planned Development

The roadmap is staged so the repository remains useful throughout its growth:

- `V0.1`: foundational structure, taxonomy, and core topic pages
- `V0.2`: broader topic coverage and better cross-linking
- `V0.3`: mapping of representative papers, tools, and datasets
- `V0.4`: lightweight recurring update workflows
- `V1.0`: stable and extensible Manufacturing AI Radar

Detailed milestones are tracked in [roadmap/roadmap.md](roadmap/roadmap.md).

## Contribution and Maintenance Logic

This repository evolves in layers:

1. Define stable taxonomy and domain boundaries.
2. Build topic pages that explain each part of the field.
3. Add representative literature, tools, datasets, and industrial examples.
4. Establish lightweight recurring maintenance.

Contributors should prefer structured additions over unorganized accumulation. New content should clearly state:

- which manufacturing context it belongs to
- which problem type it addresses
- which methods it uses
- whether it is research-oriented, tool-oriented, or deployment-oriented

Maintenance guidance is documented in [docs/contribution_guide.md](docs/contribution_guide.md) and [docs/maintenance.md](docs/maintenance.md).

Automated literature harvesting is documented in [docs/literature_scanning.md](docs/literature_scanning.md), and the full daily intake-to-curation pipeline is documented in [docs/daily_pipeline.md](docs/daily_pipeline.md).

## Audience

This repository is primarily for:

- researchers working on AI applications in manufacturing
- engineers exploring industrial AI use cases
- students entering smart manufacturing and intelligent production research
- practitioners looking for a structured overview of the field

## Language

The main repository content is maintained in English for broad accessibility. Chinese navigation notes may be added later where useful, but the core structure remains English-first.
