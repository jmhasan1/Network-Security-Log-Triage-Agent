# Configuration and Artifacts

This document explains two fundamental concepts that enable the modular design of the **Network Security ML Pipeline**:

- **Configuration Objects**
- **Artifact Objects**

These two concepts form the communication backbone of the pipeline.

Instead of hardcoding paths, parameters, or sharing variables between components, the project uses configuration objects to define **how** each component should execute and artifact objects to represent **what** each component produces.

This design keeps the pipeline modular, reusable, and easy to maintain.

---

# Overview

The relationship between configurations and artifacts can be summarized as follows:

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

Every pipeline stage follows the same pattern:

1. Receive a configuration object.
2. Execute its responsibility.
3. Produce an artifact object.
4. Pass the artifact to the next stage.

This consistent workflow simplifies both development and testing.

---

# Configuration Objects

## What is a Configuration Object?

A configuration object stores all the information required for a pipeline stage to execute.

Instead of embedding values directly in the code, each component receives a dedicated configuration object containing its runtime settings.

Typical configuration information includes:

- Input paths
- Output paths
- Dataset locations
- Directory names
- File names
- Thresholds
- Hyperparameters
- Feature store locations

Configuration objects describe **how a component should run**, but they do not perform any processing themselves.

---

# Why Use Configuration Objects?

Without configuration objects, components would contain many hardcoded values.

Example (hardcoded approach):

```python
train_path = "artifacts/data_ingestion/train.csv"
```

This tightly couples the implementation to a specific directory structure.

Instead, configuration objects provide these values externally.

Conceptually:

```text
Component
      │
      ▼
Configuration Object
      │
      ▼
Input Paths
Output Paths
Thresholds
Directories
```

Benefits:

- Centralized configuration
- Easier maintenance
- Better readability
- Simplified testing
- Greater flexibility

---

# Configuration Hierarchy

The pipeline begins with a master configuration object.

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

Each stage receives only the configuration relevant to its responsibilities.

This prevents unnecessary dependencies between components.

---

# Configuration Objects in the Project

The project currently defines the following configuration classes.

| Configuration Class | Purpose |
|---------------------|---------|
| `TrainingPipelineConfig` | Defines global pipeline settings and artifact directories |
| `DataIngestionConfig` | Configures data ingestion and feature store paths |
| `DataValidationConfig` | Configures validation inputs, schema, and drift reports |
| `DataTransformationConfig` | Configures preprocessing outputs and transformed datasets |
| `ModelTrainerConfig` | Configures model storage, expected accuracy, and training parameters |

Together, these classes control the execution of the complete training workflow.

---

# Artifact Objects

## What is an Artifact?

An artifact is the output produced by a pipeline stage.

Instead of returning multiple unrelated variables, each component returns a structured artifact object that contains everything required by the next stage.

Artifacts represent **the result of completed work**.

---

# Why Use Artifacts?

Consider Data Ingestion.

After execution, it produces:

- Training dataset path
- Testing dataset path
- Feature store path

Instead of returning three separate values:

```python
return train_path, test_path, feature_store_path
```

the component returns one artifact object.

Conceptually:

```text
DataIngestionArtifact

├── train_file_path
├── test_file_path
└── feature_store_path
```

This approach:

- keeps interfaces clean,
- improves readability,
- reduces coupling,
- makes extending outputs much easier.

---

# Artifact Flow

Artifacts move through the pipeline in sequence.

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
        │
        ▼
ModelTrainerArtifact
```

Each artifact contains only the information required by the next stage.

---

# Artifact Classes in the Project

| Artifact Class | Produced By | Used By |
|----------------|------------|---------|
| `DataIngestionArtifact` | Data Ingestion | Data Validation |
| `DataValidationArtifact` | Data Validation | Data Transformation |
| `DataTransformationArtifact` | Data Transformation | Model Trainer |
| `ModelTrainerArtifact` | Model Trainer | Final pipeline output |

This creates a clean and predictable communication chain throughout the pipeline.

---

# Configuration and Artifact Interaction

Every pipeline stage follows the same execution pattern.

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

For example:

```text
DataTransformationConfig
            │
            ▼
Data Transformation Component
            │
            ▼
DataTransformationArtifact
            │
            ▼
Model Trainer
```

This pattern is repeated consistently across all stages.

---

# Pipeline Example

The complete workflow can be visualized as:

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
Model Trainer
        │
        ▼
ModelTrainerArtifact
```

Notice that no component directly calls another component's internal logic. Communication always occurs through artifacts.

---

# Advantages of This Design

Using configuration and artifact objects provides several engineering benefits.

### Modularity

Each component is self-contained and independent.

### Loose Coupling

Components communicate only through well-defined objects.

### Maintainability

Configuration changes can often be made without modifying business logic.

### Scalability

New fields can be added to configurations or artifacts without changing the communication pattern.

### Testability

Individual components can be tested by providing mock configuration and artifact objects.

### Readability

Inputs and outputs are explicit, making the pipeline easier to understand.

---

# Software Engineering Patterns

The configuration and artifact system demonstrates several established software engineering patterns.

| Pattern | Purpose |
|----------|---------|
| Configuration Object Pattern | Encapsulates runtime settings |
| Data Transfer Object (DTO) Pattern | Artifact objects transfer structured data between components |
| Dependency Injection | Components receive dependencies rather than creating them |
| Pipeline Pattern | Sequential execution of processing stages |
| Single Responsibility Principle | Each object has one clear responsibility |

These patterns improve the flexibility and maintainability of the overall system.

---

# Why This Matters

Many beginner Machine Learning projects pass variables directly between functions or rely on global state.

This project instead adopts a production-oriented architecture where every component has:

- clearly defined inputs,
- clearly defined outputs,
- isolated responsibilities,
- standardized communication.

This approach makes the pipeline easier to extend as new capabilities are introduced.

For example, adding a new pipeline stage would simply require:

1. Creating a new configuration object.
2. Implementing the new component.
3. Defining a new artifact object.
4. Updating the pipeline orchestration.

The existing architecture remains unchanged.

---

# Summary

Configuration objects define **how** each component executes.

Artifact objects define **what** each component produces.

Together they create a clean, modular, and extensible communication mechanism that allows the entire Machine Learning pipeline to remain loosely coupled and easy to maintain.

---

# Next Document

Continue with:

```text
05_Data_Ingestion.md
```

to explore the first stage of the Machine Learning pipeline in detail.