# Project Structure

This document describes the directory structure of the **Network Security ML Pipeline** and explains the responsibility of every major folder and file in the repository.

The project follows a modular architecture where each directory has a single responsibility, making the codebase easier to maintain, extend, and test.

---

# Repository Structure

```text
Network-Security-Log-Triage-Agent/

│
├── .github/
├── .venv/
├── data/
├── data_schema/
├── docs/
├── logs/
├── models/
├── networksecurity/
├── notebooks/
├── templates/
│
├── app.py
├── main.py
├── Dockerfile
├── pyproject.toml
├── requirements.txt
├── setup.py
├── README.md
└── .env
```

---

# Root Directory

The root directory contains project configuration, documentation, application entry points, and deployment files.

| File | Purpose |
|------|----------|
| app.py | FastAPI application for training and prediction |
| main.py | Standalone entry point for running the training pipeline |
| Dockerfile | Container configuration |
| pyproject.toml | Modern Python package configuration |
| requirements.txt | Python dependencies |
| setup.py | Package installation script (legacy compatibility) |
| README.md | Repository overview |
| .env | Environment variables |

---

# networksecurity/

This is the main Python package of the project.

All Machine Learning logic is implemented inside this directory.

```text
networksecurity/

├── cloud/
├── components/
├── constant/
├── entity/
├── exception/
├── logging/
├── pipeline/
└── utils/
```

---

# components/

The **components** package contains the core Machine Learning pipeline stages.

Each component performs one independent task.

```text
components/

data_ingestion.py

data_validation.py

data_transformation.py

model_trainer.py
```

Responsibilities:

- Data Ingestion
- Data Validation
- Data Transformation
- Model Training

Every component:

- Receives configuration
- Performs one task
- Produces an artifact

---

# entity/

The entity package contains structured objects used throughout the pipeline.

```text
entity/

artifact_entity.py

config_entity.py
```

These files define:

## Configuration Objects

Examples:

- TrainingPipelineConfig
- DataIngestionConfig
- DataValidationConfig
- DataTransformationConfig
- ModelTrainerConfig

Configuration objects store settings required by each pipeline stage.

---

## Artifact Objects

Examples:

- DataIngestionArtifact
- DataValidationArtifact
- DataTransformationArtifact
- ModelTrainerArtifact

Artifacts allow one pipeline stage to pass structured outputs to the next stage.

---

# pipeline/

This package contains the orchestration logic.

```text
pipeline/

training_pipeline.py
```

The Training Pipeline coordinates the complete workflow:

```text
Data Ingestion
        ↓
Data Validation
        ↓
Data Transformation
        ↓
Model Training
```

Instead of placing orchestration inside `main.py`, it is encapsulated in a dedicated pipeline class.

---

# utils/

The utilities package contains reusable helper functions shared across multiple components.

```text
utils/

main_utils/

ml_utils/
```

---

## utils/main_utils/

Contains general-purpose helper functions.

Examples:

- YAML reading/writing
- Pickle serialization
- NumPy save/load
- Model evaluation
- Utility functions

These functions are independent of any specific pipeline stage.

---

## utils/ml_utils/

Contains Machine Learning-specific utilities.

```text
metric/

model/
```

### metric/

Classification metric calculation.

Example:

- Precision
- Recall
- F1 Score

---

### model/

Contains the custom `NetworkModel` wrapper.

This combines:

```text
Preprocessor

+

Trained Model
```

into a single inference object.

---

# constant/

Contains project-wide constants.

```text
constant/

training_pipeline/
```

Examples include:

- Dataset names
- Directory names
- Target column
- File names
- Model trainer parameters
- Pipeline configuration

Centralizing constants prevents hardcoded values throughout the project.

---

# cloud/

Contains cloud-related functionality.

Current implementation:

- AWS S3 synchronization

Responsibilities:

- Upload artifacts
- Upload trained models

This layer is optional and mainly used for cloud deployment.

---

# logging/

Contains the centralized logging configuration.

Instead of using

```python
print()
```

the project uses structured logging.

Benefits:

- Better debugging
- Centralized logs
- Production readiness

---

# exception/

Contains custom exception handling.

Instead of exposing raw Python exceptions,

the project wraps errors inside

```text
NetworkSecurityException
```

This provides consistent error reporting throughout the application.

---

# data/

The data directory stores all datasets used during development and training.

```text
data/

raw/

processed/

interim/

external/

logs/

vector_store/
```

---

## raw/

Original datasets.

These should never be modified.

---

## interim/

Temporary datasets created during preprocessing.

---

## processed/

Datasets ready for Machine Learning.

---

## external/

External datasets obtained from third-party sources.

---

## logs/

Reserved for security log datasets.

Currently unused but intended for future development.

---

## vector_store/

Reserved for vector databases used by Retrieval-Augmented Generation (RAG).

Currently empty.

This directory will become important during the Log Triage Agent phase.

---

# data_schema/

Contains dataset schemas.

```text
schema.yaml
```

The schema defines:

- Expected columns
- Dataset structure

Used during Data Validation.

---

# models/

Stores trained models.

Examples:

```text
model.pkl

preprocessor.pkl

network_model.pkl
```

These files are loaded during inference.

---

# logs/

Stores application log files generated during execution.

Typical contents include:

- Training logs
- Prediction logs
- Error logs

---

# templates/

Contains HTML templates used by FastAPI.

Current template:

```text
table.html
```

This template renders prediction results as an HTML table.

The API converts prediction DataFrames into HTML and injects them into this template using Jinja2.

---

# notebooks/

Contains exploratory Jupyter notebooks.

Typical uses:

- Dataset exploration
- Feature engineering experiments
- Model prototyping

Notebook code should not contain production logic.

---

# docs/

Project documentation.

This directory explains:

- Architecture
- Components
- Setup
- Design decisions
- Future roadmap

The documentation is intended to help new contributors understand the project quickly.

---

# .github/

GitHub-specific configuration.

Examples:

- GitHub Actions
- CI/CD workflows
- Issue templates

---

# .venv/

Python virtual environment.

Generated automatically by `uv`.

Should not be committed to version control.

---

# Architectural Philosophy

The repository follows a layered architecture.

```text
Configuration
        │
        ▼
Components
        │
        ▼
Artifacts
        │
        ▼
Pipeline
        │
        ▼
API
```

Each layer has a clearly defined responsibility.

---

# Design Principles

The repository is organized around the following software engineering principles.

- Modular Design
- Separation of Concerns
- Single Responsibility Principle
- Configuration-Driven Development
- Artifact-Based Communication
- Pipeline Architecture
- Reusable Utilities

These principles improve maintainability, scalability, and readability.

---

---

# Future Expansion

This repository is designed to evolve beyond a traditional Machine Learning pipeline into an AI-powered **Network Security Log Triage Agent**.

As a result, several directories already exist (or have been planned) even though they are only partially used in the current implementation. These directories are intentionally included to provide a stable project structure and minimize future refactoring.

| Directory | Current Status | Planned Purpose |
|-----------|---------------|-----------------|
| `data/vector_store/` | Reserved (currently empty) | Store vector embeddings for Retrieval-Augmented Generation (RAG), including security documentation, MITRE ATT&CK knowledge, historical investigations, and threat intelligence. |
| `data/logs/` | Reserved | Store raw security logs collected from firewalls, SIEM platforms, Windows Event Logs, Linux audit logs, cloud audit logs, and other security telemetry sources. |
| `cloud/` | AWS S3 synchronization | Will evolve into a generalized cloud storage layer supporting artifact storage, model versioning, vector databases, and cloud-native deployment across providers. |
| `templates/` | HTML prediction table | Will evolve into a web-based Security Operations Center (SOC) dashboard for interactive investigation reports, alert visualization, reasoning traces, and analyst feedback. |

---

## Planned Repository Evolution

The current project focuses on a production-oriented Machine Learning pipeline.

```text
Current Repository

MongoDB
    │
    ▼
Data Ingestion
    │
    ▼
Data Validation
    │
    ▼
Data Transformation
    │
    ▼
Model Training
    │
    ▼
FastAPI Prediction
```

The long-term vision is to extend this pipeline into an intelligent AI investigation platform.

```text
Future Repository

Security Alerts
        │
        ▼
Log Ingestion
        │
        ▼
Log Validation
        │
        ▼
Feature Extraction
        │
        ▼
Machine Learning Classification
        │
        ▼
Retrieval-Augmented Generation (RAG)
        │
        ▼
LLM Reasoning
        │
        ▼
Investigation Agent
        │
        ▼
Security Report
        │
        ▼
Knowledge Base
```

---

## Why Create These Directories Early?

Maintaining a stable project structure from the beginning offers several advantages.

- **Consistent Architecture** — The repository structure remains stable as new features are added, reducing disruptive reorganizations.
- **Incremental Development** — New capabilities can be introduced into predefined locations without moving existing code.
- **Improved Maintainability** — Contributors can easily identify where future modules belong.
- **Reduced Refactoring** — Existing imports, documentation, and project organization remain largely unchanged as the system grows.
- **Clear Roadmap** — The directory structure communicates the intended evolution of the project and serves as living documentation of the architecture.

These directories should therefore be viewed as **planned architectural placeholders**, not unused or obsolete folders.

---

## Evolution Strategy

The development of this repository is planned in multiple phases.

### Phase 1 — Classical Machine Learning Pipeline *(Current)*

- MongoDB Data Ingestion
- Data Validation
- Data Transformation
- Model Training
- MLflow Experiment Tracking
- FastAPI Inference

### Phase 2 — Production ML Improvements

- Improved evaluation framework
- Enhanced preprocessing
- Better model versioning
- Cloud deployment enhancements
- Monitoring and observability

### Phase 3 — Network Security Log Triage Agent

- Security log ingestion
- Retrieval-Augmented Generation (RAG)
- Vector database integration
- LangGraph orchestration
- MCP tool integration
- Multi-agent reasoning
- Automated investigation reports

### Phase 4 — AI Security Platform

- Multi-source log correlation
- Threat intelligence integration
- Continuous learning
- Analyst feedback loop
- Human-in-the-loop workflows
- Scalable cloud deployment

---

The current Machine Learning pipeline should therefore be viewed as the **foundation layer** of a much larger AI-driven cybersecurity system. Rather than replacing the existing architecture, future development will build upon it by adding new capabilities while preserving the modular design established in this repository.

# Next Document

Continue with:

```text
03_Architecture_Overview.md
```

to understand how these folders interact to form the complete Machine Learning system.

