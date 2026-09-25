# Notebooks

This directory contains the development, validation, and engineering notebooks for the **Network Security Log Triage Agent** project.

These notebooks are **not exploratory notebooks**. Each notebook serves as a reproducible engineering artifact that validates a specific component of the project before changes are integrated into the production codebase.

## Objectives

The notebooks are designed to:

* Validate individual pipeline components independently.
* Prototype new features before modifying production code.
* Document engineering decisions and implementation details.
* Provide reproducible experiments for future development.
* Serve as technical documentation for contributors and reviewers.

## Development Workflow

Every new feature follows the same engineering workflow:

```text
Notebook
    ↓
Prototype
    ↓
Production Code
    ↓
Testing
    ↓
Documentation
    ↓
Git Commit
```

No production feature should be implemented directly without first being validated in a notebook.

## Notebook Structure

Each notebook follows a common template containing:

1. Title & Metadata
2. Objectives
3. Background
4. Architecture Overview
5. Environment & Configuration
6. Implementation
7. Validation
8. Engineering Notes
9. Summary
10. Next Steps

Maintaining a consistent structure improves readability, reproducibility, and long-term maintainability.

## Notebook Index

| Notebook | Purpose | Status as of 2026-09-25 |
|---|---|---|
| `01_data_ingestion.ipynb` | Ingestion workflow and data-source inspection | Existing notebook; restoration/hardening planned in Phase 5 |
| `02_data_validation.ipynb` | Validation workflow | Phase 4 target; current contract and implementation audit pending |
| `03_exploratory_data_analysis.ipynb`–`12_end_to_end_pipeline_test.ipynb` | EDA, transformation, feature engineering, training, evaluation, tracking, inference, and pipeline testing | Present in repository; some are scaffolds and are to be restored when directly required by their roadmap phase |
| `13_reproducibility_experiment.ipynb` | Dataset and split/preprocessing repeatability baseline | Phase 2 complete |
| `14_duplicate_leakage_experiment.ipynb` | Duplicate overlap and random-row leakage investigation | Phase 3A complete |
| `15_conflicting_label_investigation.ipynb` | Conflicting labels among feature-identical rows | Phase 3B complete |
| `16_evaluation_protocol_comparison.ipynb` | Compare evaluation protocols and group encodings | Phase 3C comparison complete; historical artifact retained |
| `17_evaluation_protocol_freeze.ipynb` | Freeze deterministic feature-group-aware primary evaluation protocol | Phase 3C complete |

Machine-readable experiment outputs are stored under `notebooks/evaluation/`. Summary and interpretation are documented in `docs/14_Reproducibility_and_Dataset_Integrity.md` through `docs/17_Evaluation_Protocol_Freeze.md`.

Notebooks 13–17 are experimental records. They do not imply that every corresponding capability has been integrated into production pipeline code.

## Notebook Categories (Planned)

### Foundation

* 00 Project Setup

### Machine Learning Pipeline

* Data Ingestion
* Data Validation
* Exploratory Data Analysis
* Feature Engineering
* Data Transformation
* Model Training
* Model Evaluation
* Prediction Pipeline

### Retrieval-Augmented Generation (Future)

* Data Preparation
* Embeddings
* Vector Database
* Retrieval Pipeline

### Agentic AI (Future)

* Agent Workflow
* Tool Integration
* Memory
* End-to-End Log Triage

## Engineering Principles

Every notebook should be:

* Reproducible
* Modular
* Well documented
* Production-aligned
* Independently executable
* Suitable for publication in this repository

The notebooks are intended to evolve alongside the production code and should always reflect the current implementation.
