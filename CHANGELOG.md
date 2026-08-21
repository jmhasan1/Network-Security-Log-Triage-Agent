# Changelog

All notable changes to the Network Security Log Triage Agent are documented here.

The project follows semantic versioning for project releases.

## [Unreleased]

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