# Maintenance Guide

## Purpose

This document describes how to maintain `Manufacturing-AI-Radar` as a living repository.

## Maintenance Objectives

- keep the repository structure coherent
- expand coverage without losing taxonomy clarity
- ensure topic pages remain comparable
- gradually connect topics to papers, tools, datasets, and industrial use cases

## Recurring Maintenance Tasks

### Weekly

- review whether any radar page needs clarification or expansion
- capture emerging topics or trends in `notes/`
- identify candidate papers, tools, or datasets for later curation

### Monthly

- promote mature notes into stable documents
- update roadmap progress
- review taxonomy boundaries if new topics are causing overlap
- remove stale placeholders or low-value duplicate content

### Quarterly

- reassess core radar domains
- improve cross-linking between pages
- review whether new industrial themes deserve dedicated topic pages
- evaluate whether lightweight automation should be added for literature scanning

## How To Add New Themes

When a new manufacturing AI theme emerges:

1. Decide whether it belongs inside an existing domain.
2. If not, create a new radar page with the standard structure.
3. Update `README.md` and `docs/taxonomy.md` if the addition changes the repository map.
4. Record the change in the worklog if it affects repository architecture.

## How To Add Representative Papers

The preferred future workflow is:

1. capture candidates in `notes/`
2. group by domain and task
3. promote only representative items into structured reference pages

## Updating Without Drift

The repository should resist three common failure modes:

- becoming a generic AI list
- becoming a disconnected note archive
- becoming too detailed in some domains while others remain undefined
