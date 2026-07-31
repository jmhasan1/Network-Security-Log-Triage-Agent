# Architecture Overview

This document provides a high-level overview of the architecture used in the **Network Security ML Pipeline**.

The project is designed using a modular, layered architecture where each component has a single responsibility. Instead of implementing the entire Machine Learning workflow in a single script or notebook, the pipeline is divided into independent stages that communicate through well-defined configuration and artifact objects.

This design improves maintainability, scalability, testability, and extensibility while following software engineering best practices.

---

# High-Level Architecture

The complete workflow is illustrated below.

```text
                    Raw Dataset (MongoDB)
                             │
                             ▼
                  Data Ingestion Component
                             │
                             ▼
                  Data Validation Component
                             │
                             ▼
                Data Transformation Component
                             │
                             ▼
                  Model Training Component
                             │
                             ▼
                   Trained NetworkModel
                             │
                             ▼
                     FastAPI Inference API
                             │
                             ▼
                        Predictions
```

Each stage performs exactly one task and passes its output to the next stage using structured artifact objects.

---

# Layered Architecture

The project follows a layered architecture.

```text
                    Application Layer
                (main.py / app.py)
                         │
                         ▼
                Training Pipeline Layer
                         │
                         ▼
                Component Layer
                         │
                         ▼
         Configuration & Artifact Layer
                         │
                         ▼
            Utility & Infrastructure Layer
                         │
                         ▼
             Database / File System / MLflow
```

Each layer has a clearly defined responsibility.

---

# Architecture Layers

## 1. Application Layer

**Purpose**

Acts as the entry point for the application.

Current files:

```text
main.py
app.py
```

Responsibilities:

- Start the training pipeline
- Launch the FastAPI application
- Expose API endpoints
- Coordinate user interactions

Business logic is intentionally kept out of this layer.

---

## 2. Training Pipeline Layer

**Purpose**

Orchestrates the complete Machine Learning workflow.

Current file:

```text
pipeline/
    training_pipeline.py
```

Responsibilities:

- Execute pipeline stages in order
- Pass artifacts between components
- Manage execution flow
- Coordinate optional cloud synchronization

The Training Pipeline does not implement Machine Learning logic itself; it coordinates specialized components.

---

## 3. Component Layer

**Purpose**

Contains the core business logic of the project.

```text
components/

├── data_ingestion.py
├── data_validation.py
├── data_transformation.py
└── model_trainer.py
```

Each component performs one independent task.

| Component | Responsibility |
|----------|----------------|
| Data Ingestion | Load data from MongoDB and prepare train/test datasets |
| Data Validation | Validate schema and detect dataset drift |
| Data Transformation | Preprocess features and generate model-ready data |
| Model Trainer | Train, evaluate, and save Machine Learning models |

Each component receives configuration objects as input and returns artifact objects as output.

---

## 4. Configuration Layer

Configuration objects define how each pipeline stage should execute.

Examples:

```text
TrainingPipelineConfig

DataIngestionConfig

DataValidationConfig

DataTransformationConfig

ModelTrainerConfig
```

Configuration objects contain information such as:

- File paths
- Dataset names
- Output directories
- Thresholds
- Hyperparameters
- Pipeline settings

Separating configuration from implementation makes the system easier to maintain and extend.

---

## 5. Artifact Layer

Artifacts represent the output of each pipeline stage.

Example execution flow:

```text
Data Ingestion
        │
        ▼
DataIngestionArtifact
        │
        ▼
Data Validation
        │
        ▼
DataValidationArtifact
        │
        ▼
Data Transformation
        │
        ▼
DataTransformationArtifact
        │
        ▼
Model Training
```

Artifacts ensure that components remain loosely coupled while sharing only the information required by the next stage.

---

## 6. Utility Layer

The utility layer contains reusable helper functions shared throughout the project.

Examples include:

- YAML operations
- Pickle serialization
- NumPy utilities
- Model evaluation
- Classification metrics
- Model wrappers

Centralizing shared functionality avoids code duplication.

---

## 7. Infrastructure Layer

The infrastructure layer manages communication with external systems.

Examples:

- MongoDB
- MLflow
- DagsHub
- File System
- Docker
- AWS S3

These services are isolated from the core Machine Learning logic, allowing infrastructure to change without affecting the pipeline.

---

# Pipeline Execution Flow

The current training workflow follows the sequence below.

```text
main.py
      │
      ▼
TrainingPipeline
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
NetworkModel
      │
      ▼
Saved Model
```

Each stage depends only on the artifact produced by the previous stage.

---

# Configuration Flow

Configuration is propagated from the top-level pipeline into each component.

```text
TrainingPipelineConfig
            │
            ▼
DataIngestionConfig
            │
            ▼
DataValidationConfig
            │
            ▼
DataTransformationConfig
            │
            ▼
ModelTrainerConfig
```

Each component receives only the configuration relevant to its own responsibilities.

---

# Artifact Flow

Artifacts are the communication mechanism between pipeline stages.

```text
DataIngestionArtifact
            │
            ▼
DataValidationArtifact
            │
            ▼
DataTransformationArtifact
            │
            ▼
ModelTrainerArtifact
```

This approach avoids tightly coupling components and makes each stage independently testable.

---

# FastAPI Inference Flow

The inference pipeline is separate from the training pipeline.

```text
User Uploads CSV
         │
         ▼
FastAPI Endpoint
         │
         ▼
Load Preprocessor
         │
         ▼
Load Trained Model
         │
         ▼
NetworkModel
         │
         ▼
Generate Predictions
         │
         ▼
HTML Response
```

Separating training and inference allows models to be trained independently of prediction requests.

---

# Software Design Patterns

The project incorporates several software engineering patterns.

| Pattern | Purpose |
|----------|---------|
| Pipeline Pattern | Organizes the ML workflow into sequential stages |
| Facade Pattern | The Training Pipeline provides a unified interface for executing all stages |
| Configuration Pattern | Centralizes runtime configuration |
| Artifact Pattern | Standardizes communication between components |
| Factory-like Configuration | Creates stage-specific configuration objects |
| Layered Architecture | Separates responsibilities into distinct layers |
| Dependency Injection | Components receive configuration instead of creating it internally |

These patterns improve modularity, maintainability, and extensibility.

---

# Design Principles

The architecture follows several core engineering principles.

- **Single Responsibility Principle (SRP)** – Each component has one well-defined responsibility.
- **Separation of Concerns** – Data ingestion, validation, transformation, training, and serving are isolated.
- **Loose Coupling** – Components communicate through artifacts rather than direct dependencies.
- **High Cohesion** – Related functionality is grouped together within each module.
- **Configuration-Driven Design** – Runtime behavior is controlled through configuration objects.
- **Reusability** – Shared functionality is centralized in utility modules.

---

# Why This Architecture?

Compared to a notebook-based implementation, this architecture offers several advantages.

| Traditional Notebook | This Project |
|----------------------|--------------|
| Monolithic code | Modular components |
| Hardcoded configuration | Configuration-driven |
| Shared variables | Structured artifacts |
| Difficult to test | Independently testable components |
| Difficult to scale | Easily extensible |
| Limited reusability | Reusable architecture |

This design is suitable for production-oriented Machine Learning systems where maintainability and scalability are important.

---

# Future Architecture

The current Machine Learning pipeline serves as the foundation for the planned **Network Security Log Triage Agent**.

The long-term architecture is expected to evolve as follows.

```text
Security Logs
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

The existing Machine Learning pipeline will become one component within a larger AI-driven security investigation system.

---

# Next Document

Continue with:

```text
04_Configuration_and_Artifacts.md
```

to understand how configuration objects and artifacts enable communication between pipeline stages.