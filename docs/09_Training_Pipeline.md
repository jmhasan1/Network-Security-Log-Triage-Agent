# Training Pipeline

The **Training Pipeline** is the central orchestrator of the Network Security ML Pipeline.

Rather than implementing Machine Learning logic directly, it coordinates the execution of all pipeline components in the correct sequence, ensuring that each stage receives the required configuration and artifacts before execution.

The Training Pipeline acts as the backbone of the entire system by transforming independent components into a complete end-to-end Machine Learning workflow.

---

# Purpose

The primary objective of the Training Pipeline is to automate the complete Machine Learning workflow.

Instead of manually executing every stage independently, the pipeline performs the following operations sequentially:

- Data Ingestion
- Data Validation
- Data Transformation
- Model Training

The pipeline guarantees that each stage executes only after the successful completion of the previous stage.

---

# Responsibilities

The Training Pipeline is responsible for:

- Initializing pipeline configuration
- Creating component-specific configurations
- Executing each pipeline stage
- Passing artifacts between stages
- Managing execution order
- Handling pipeline-level exceptions
- Synchronizing artifacts (optional cloud storage)
- Returning the final ModelTrainerArtifact

Importantly, the pipeline does **not** contain Machine Learning algorithms or preprocessing logic. Those responsibilities remain inside their respective components.

---

# Pipeline Architecture

The overall execution flow is shown below.

```text
                 main.py / FastAPI
                        │
                        ▼
              TrainingPipeline
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
 Data Ingestion   Data Validation   Data Transformation
        │               │                │
        └───────────────┼────────────────┘
                        ▼
               Model Training
                        │
                        ▼
               ModelTrainerArtifact
```

The Training Pipeline coordinates the execution but delegates the actual work to specialized components.

---

# Inputs

The pipeline begins by creating a **TrainingPipelineConfig** object.

This master configuration contains the information required to initialize every component in the workflow.

The pipeline itself does not require user input beyond the project configuration and environment variables.

---

# Outputs

The final output of the Training Pipeline is a **ModelTrainerArtifact**, which contains:

| Artifact | Description |
|----------|-------------|
| Trained Model Path | Serialized NetworkModel |
| Training Metrics | Performance on training data |
| Testing Metrics | Performance on testing data |

This artifact represents the successful completion of the training process.

---

# Pipeline Execution Flow

The complete workflow is illustrated below.

```text
TrainingPipeline
        │
        ▼
TrainingPipelineConfig
        │
        ▼
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
        │
        ▼
ModelTrainerArtifact
```

Notice that every component communicates only through artifacts.

No component directly depends on another component's internal implementation.

---

# Stage-by-Stage Workflow

## Stage 1 — Data Ingestion

The pipeline initializes the Data Ingestion component using a `DataIngestionConfig`.

Responsibilities:

- Retrieve data from MongoDB
- Create Feature Store
- Split train/test datasets
- Produce DataIngestionArtifact

---

## Stage 2 — Data Validation

The pipeline passes the DataIngestionArtifact to the Data Validation component.

Responsibilities:

- Validate dataset structure
- Detect dataset drift
- Generate validation reports
- Produce DataValidationArtifact

---

## Stage 3 — Data Transformation

The pipeline initializes the Data Transformation component.

Responsibilities:

- Load validated datasets
- Separate features and target
- Apply preprocessing pipeline
- Generate transformed NumPy arrays
- Save preprocessing pipeline
- Produce DataTransformationArtifact

---

## Stage 4 — Model Training

Finally, the pipeline executes the Model Training component.

Responsibilities:

- Train multiple candidate models
- Optimize hyperparameters
- Evaluate models
- Select the best model
- Log MLflow experiments
- Package NetworkModel
- Produce ModelTrainerArtifact

---

# Configuration Flow

The pipeline manages configuration centrally.

```text
TrainingPipelineConfig
        │
        ├──────────────┐
        ▼              ▼
DataIngestionConfig
DataValidationConfig
DataTransformationConfig
ModelTrainerConfig
```

Each component receives only the configuration required for its own execution.

---

# Artifact Flow

Artifacts are the communication mechanism between stages.

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

This design minimizes coupling between components.

---

# Component Interaction

The interaction between pipeline stages follows a consistent pattern.

```text
Configuration
        │
        ▼
Component
        │
        ▼
Artifact
        │
        ▼
Next Component
```

This pattern is repeated throughout the entire workflow.

---

# Optional Cloud Synchronization

The current implementation includes optional methods for synchronizing pipeline artifacts with cloud storage.

Current functionality:

- Upload artifacts
- Upload trained models

These methods are designed to support cloud-based workflows while remaining independent of the core Machine Learning logic.

> **Implementation Note:**  
> During our review of the current codebase, the cloud synchronization functionality was identified as optional. It can be disabled when cloud storage is not required, allowing the pipeline to run entirely on a local development environment.

---

# Error Handling

The Training Pipeline manages failures at the orchestration level.

Potential failure scenarios include:

- Data ingestion failure
- Validation failure
- Transformation failure
- Model training failure
- Artifact creation failure
- Cloud synchronization failure

Exceptions raised by individual components are propagated through the pipeline and handled using the project's custom exception framework.

---

# Design Decisions

Several architectural decisions make the Training Pipeline robust and extensible.

### Centralized Orchestration

The pipeline coordinates execution without implementing business logic.

---

### Sequential Execution

Each stage depends on the successful completion of the previous stage.

This ensures consistent and reproducible workflows.

---

### Artifact-Based Communication

Artifacts provide a standardized mechanism for passing outputs between stages.

---

### Configuration-Driven Execution

Components receive configuration objects rather than relying on hardcoded values.

---

### Loose Coupling

Each component can be modified or replaced without affecting the overall pipeline structure, provided its input and output contracts remain unchanged.

---

# Software Engineering Patterns

The Training Pipeline demonstrates several architectural patterns.

| Pattern | Purpose |
|----------|---------|
| Pipeline Pattern | Executes processing stages sequentially |
| Facade Pattern | Provides a single interface for the entire training workflow |
| Orchestrator Pattern | Coordinates independent components |
| Dependency Injection | Supplies configuration objects to components |
| Data Transfer Object (DTO) | Uses artifact objects for communication |
| Single Responsibility Principle | Focuses exclusively on workflow orchestration |

---

# Implementation Notes

The current implementation includes the following orchestration behavior.

- Initializes the master pipeline configuration.
- Executes Data Ingestion.
- Executes Data Validation.
- Executes Data Transformation.
- Executes Model Training.
- Passes artifacts between components.
- Supports optional artifact synchronization to cloud storage.
- Returns the final ModelTrainerArtifact.

These notes reflect the current implementation and may evolve as new pipeline stages are introduced.

---

# Current Limitations

The current implementation has several opportunities for enhancement.

- Pipeline execution is strictly sequential.
- No parallel execution of independent tasks.
- No checkpointing or resume capability.
- No pipeline monitoring dashboard.
- No retry mechanism for failed stages.
- Limited execution status reporting.

Additionally, during our review of the codebase, we identified several implementation-specific improvements:

- The pipeline class name contains a typographical inconsistency (`TrainingPipleine`), which should be renamed to `TrainingPipeline`.
- Cloud synchronization is tightly integrated and could be made configurable through project settings.
- Pipeline execution status could be exposed more explicitly for monitoring and debugging.

These observations are specific to the current implementation and provide opportunities for future refinement.

---

# Future Improvements

Potential enhancements include:

- Pipeline checkpointing and recovery.
- Parallel execution where dependencies allow.
- Workflow scheduling.
- Pipeline monitoring dashboard.
- Automated retry strategies.
- Pipeline notifications.
- Distributed execution.
- Integration with orchestration platforms (e.g., Airflow, Prefect, Kubeflow).

---

# Why the Training Pipeline Matters

Without the Training Pipeline, developers would need to execute every stage manually and manage dependencies between components themselves.

The Training Pipeline provides:

- Automated execution
- Standardized workflow
- Consistent artifact management
- Centralized orchestration
- Improved maintainability
- Easier testing
- Better scalability

It transforms a collection of independent components into a cohesive Machine Learning system.

---

# Summary

The Training Pipeline is the orchestration layer of the Network Security ML Pipeline.

By coordinating configuration, components, and artifacts into a structured workflow, it enables fully automated, reproducible model training while maintaining a clean separation between orchestration and business logic.

As the project evolves, this orchestration layer can be extended with additional pipeline stages, monitoring, scheduling, and cloud-native capabilities without fundamentally changing the architecture.

---

# Next Document

Continue with:

```text
10_Inference_API.md
```

to understand how the trained model is served through FastAPI for prediction and inference.