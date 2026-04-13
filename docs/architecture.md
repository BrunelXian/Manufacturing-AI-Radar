# Repository Architecture

## Purpose

This document explains how `Manufacturing-AI-Radar` is organized and how each part of the repository should evolve.

The repository is structured as a research navigation system rather than a software package. Its primary output is organized knowledge, not executable code.

## Design Principles

- keep the top-level structure shallow and readable
- separate stable framework documents from evolving topic content
- make topic pages comparable through a shared writing pattern
- support future additions of references, tools, datasets, and update workflows
- avoid turning the repository into an unstructured note dump

## Structural Layers

### Framework Layer

The `docs/` directory defines how the repository works.

- `architecture.md`: repository design and content logic
- `taxonomy.md`: classification framework for AI in manufacturing
- `contribution_guide.md`: rules for extending the repository
- `maintenance.md`: recurring update and maintenance workflow
- `worklog-nightly.md`: implementation log for major working sessions

These documents should remain relatively stable and act as project infrastructure.

### Radar Layer

The `radar/` directory holds domain pages built with a consistent structure:

- what the domain covers
- why it matters
- typical tasks
- representative methods
- application scenarios
- key research questions
- future opportunity

This is the main knowledge layer of the repository.

### Reference Layer

The `refs/` directory will later organize representative papers, tools, datasets, and benchmark resources. It should not become a raw bibliography dump.

### Notes Layer

The `notes/` directory is reserved for exploratory notes, synthesis memos, and intermediate observations that are not yet mature enough for the main radar.

### Visual Layer

The `assets/` directory stores figures, diagrams, and future visual radar materials.

## Intended Growth Path

The repository should evolve in the following order:

1. stable structure
2. stable taxonomy
3. strong domain pages
4. representative references and tools
5. update workflows and automation support

## Content Quality Rules

- prefer concise explanation over exhaustive listing
- keep manufacturing context explicit
- distinguish sensing, prediction, control, and deployment clearly
- avoid duplicating concepts across multiple pages without purpose
- write for both technical researchers and applied industrial readers
