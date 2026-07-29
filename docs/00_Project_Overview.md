# Project Overview

## Network Security ML Pipeline

> An end-to-end Machine Learning pipeline for network security data that automates data ingestion, validation, transformation, model training, experiment tracking, and inference. The project is designed using modular software engineering principles and serves as the foundation for a future AI-powered Network Security Log Triage Agent.

---

# Project Goal

The primary goal of this project is to build a production-oriented Machine Learning pipeline for detecting malicious network activity from structured security data.

Unlike a traditional Jupyter Notebook workflow, this project follows a modular architecture where every stage of the Machine Learning lifecycle is implemented as an independent component.

The project demonstrates how to:

- Build reusable Machine Learning components
- Create configurable training pipelines
- Validate incoming datasets
- Perform automated feature preprocessing
- Train and compare multiple Machine Learning models
- Track experiments using MLflow
- Package models for inference
- Serve predictions through a FastAPI application

The repository emphasizes software engineering practices required for production Machine Learning systems rather than focusing solely on model accuracy.

---

# Problem Statement

Network environments generate large volumes of traffic every day.

Among legitimate traffic, malicious activities such as phishing, attacks, or abnormal network behavior may occur.

The objective of this project is to automatically classify network records into normal or malicious categories using supervised Machine Learning.

The complete system automates the workflow from raw data ingestion to prediction, eliminating the need for manual preprocessing or model training.

---

# Dataset

The project uses a structured network security dataset containing multiple numerical network features and a target classification label.

Current data source:

- MongoDB Collection

During training, the dataset is:

1. Retrieved from MongoDB
2. Exported into a local feature store
3. Split into training and testing datasets
4. Validated against the expected schema
5. Checked for dataset drift
6. Transformed into model-ready NumPy arrays

The transformed datasets are then used for Machine Learning training.

---

# ML Workflow

The current Machine Learning workflow follows the architecture below.

```text
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
NetworkModel
    │
    ▼
FastAPI Inference
```

Each stage is implemented as an independent component and communicates with the next stage through artifact objects.

---

# Project Architecture

The project follows a layered architecture.

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
Training Pipeline
        │
        ▼
Inference API
```

Every component has a single responsibility.

For example:

- Data Ingestion only retrieves and prepares data.
- Data Validation only verifies data quality.
- Data Transformation only preprocesses features.
- Model Trainer only trains and evaluates models.

This separation makes the project modular, maintainable, and easy to extend.

---

# Technology Stack

## Programming Language

- Python 3.11

## Machine Learning

- Scikit-learn
- NumPy
- Pandas

## Data Storage

- MongoDB

## Experiment Tracking

- MLflow
- DagsHub (remote MLflow tracking)

## Backend

- FastAPI
- Uvicorn

## Serialization

- Pickle

## Environment Management

- uv
- Virtual Environment

## Configuration

- dotenv
- YAML

## Deployment

- Docker

---

# Current Features

The current implementation supports the following capabilities.

### Data Pipeline

- MongoDB data ingestion
- Local feature store creation
- Train/Test dataset generation

### Data Quality

- Schema validation
- Dataset drift detection
- Drift report generation

### Feature Engineering

- Missing value imputation using KNNImputer
- Scikit-learn preprocessing pipeline
- NumPy dataset generation

### Machine Learning

- Multiple candidate models
- Hyperparameter tuning
- Model comparison
- Classification metrics
- MLflow experiment tracking

### Model Packaging

- Preprocessor persistence
- Trained model persistence
- Unified inference model (NetworkModel)

### API

- FastAPI application
- Training endpoint
- Prediction endpoint
- HTML prediction visualization

---

# Software Engineering Principles

This project is designed around several important engineering principles.

- Separation of Concerns
- Single Responsibility Principle
- Configuration-Driven Design
- Artifact-Based Communication
- Pipeline Architecture
- Modular Components
- Reusable Utilities

These principles make the project easier to maintain, test, and extend.

---

# Repository Status

Current implementation:

- End-to-end Machine Learning training pipeline
- FastAPI inference application
- MLflow experiment tracking
- Docker support
- Modular project architecture

---

# Future Vision

This repository is not intended to remain a traditional Machine Learning pipeline.

It serves as the foundation for a much larger AI-powered cybersecurity platform.

The next stage of development is the **Network Security Log Triage Agent**, where the trained Machine Learning model becomes one tool within an intelligent investigation system.

The planned architecture includes:

```text
Security Alerts
        │
        ▼
Log Ingestion
        │
        ▼
Data Validation
        │
        ▼
Feature Extraction
        │
        ▼
Machine Learning Classification
        │
        ▼
RAG Retrieval
        │
        ▼
LLM Reasoning
        │
        ▼
Investigation Report
        │
        ▼
Knowledge Base
```

The long-term objective is to evolve this project from a classical Machine Learning pipeline into a production-ready AI Security Investigation Platform capable of assisting Security Operations Center (SOC) analysts in triaging and investigating security events.

---

# Learning Objectives

This repository demonstrates practical implementation of:

- Production Machine Learning Pipelines
- Machine Learning System Design
- Software Engineering for AI Applications
- Experiment Tracking
- Model Serving
- FastAPI Deployment
- Modular Python Architecture

It is intended both as a learning project and as the foundation for future AI agent development in the cybersecurity domain.