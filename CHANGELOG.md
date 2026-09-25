# Changelog

All notable changes to the Network Security Log Triage Agent are documented here.

The project follows semantic versioning for project releases.

## [Unreleased]

### Engineering milestones completed since v0.1.0 (not a release)

- Phase 1: dependency security review and vulnerability remediation documented in `docs/13_Dependency_Security_and_Vulnerability_Remediation.md`.
- Phase 2: reproducibility experiment and dataset/split/preprocessing fingerprints recorded in Notebook 13 and `notebooks/evaluation/reproducibility_baseline.json`.
- Phase 3A: duplicate structure and random-row split overlap investigated in Notebook 14 and `duplicate_leakage_baseline.json`.
- Phase 3B: conflicting-label groups investigated in Notebook 15 and `conflicting_label_investigation.json`.
- Phase 3C: evaluation protocols compared in Notebook 16; deterministic feature-group-aware Protocol B frozen in Notebook 17 and `phase_3c_evaluation_protocol_comparison_freezed.json`.
- Added phase documentation `docs/14` through `docs/17` and updated notebook index.
- These milestones do not constitute a `v0.2.0` release; production integration and remaining roadmap phases are still in progress.

### Planned

- Harden data ingestion and validation
- Improve model training and evaluation
- Establish dataset versioning with DVC
- Extend MLflow experiment lineage
- Introduce MLflow Model Registry
- Validate end-to-end reproducibility

## [0.1.0] - 2026-08-21

### Added

- Established the modular Network Security ML pipeline foundation
- Migrated the application package to `src/network_security/`
- Added project documentation covering the existing ML pipeline
- Added baseline evaluation documentation
- Added `uv`-based environment management
- Added `pyproject.toml` project metadata
- Added `uv.lock` for dependency reproducibility
- Added `.python-version` for Python version specification
- Added schema configuration under `configs/schema/`
- Added the initial roadmap toward the Network Security Log Triage Agent

### Architecture

- Data ingestion
- Data validation
- Data transformation
- Model training
- Training pipeline orchestration
- FastAPI inference
- MLflow experiment tracking
- Docker support

## Upcoming Releases

### 0.2.x - Reproducible & Hardened ML Foundation

- Data quality improvements
- Stronger validation
- Improved preprocessing
- Model benchmarking
- Experiment lineage
- DVC dataset versioning
- MLflow Model Registry
- Reproducibility validation

### 0.3.x - Security Log Processing

### 0.4.x - RAG & Historical Incident Retrieval

### 0.5.x - LangGraph Investigation Agent

### 0.6.x - MCP Security Tools

### 0.7.x - Evaluation & Monitoring

### 0.8.x - Integrated Security Triage System

### 0.9.x - Release Candidate & Hardening

### 1.0.0 - Production-Oriented Network Security Log Triage Agent