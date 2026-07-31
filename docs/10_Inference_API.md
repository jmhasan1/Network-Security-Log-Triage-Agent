# Inference API

The **Inference API** is responsible for serving the trained Machine Learning model through a RESTful web service built using **FastAPI**.

Unlike the Training Pipeline, which builds the model, the Inference API loads the trained model and preprocessing pipeline to generate predictions for new datasets.

This separation allows model training and model serving to evolve independently while ensuring consistent preprocessing during inference.

---

# Purpose

The objective of the Inference API is to expose the trained Machine Learning model through HTTP endpoints.

It enables users to:

- Train the model through an API endpoint.
- Upload datasets for prediction.
- Automatically preprocess incoming data.
- Generate predictions.
- Display prediction results in an HTML table.

The API acts as the interface between users and the Machine Learning pipeline.

---

# Responsibilities

The Inference API performs the following tasks:

- Initialize the FastAPI application.
- Configure middleware.
- Load environment variables.
- Provide model training endpoint.
- Provide prediction endpoint.
- Load trained models.
- Apply preprocessing.
- Generate predictions.
- Render prediction results.

---

# High-Level Architecture

The inference workflow is shown below.

```text
                User
                  │
                  ▼
             FastAPI Server
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   /train Endpoint     /predict Endpoint
        │                   │
        ▼                   ▼
Training Pipeline     Load Trained Model
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

---

# Application Components

The FastAPI application consists of several logical sections.

| Component | Purpose |
|-----------|---------|
| FastAPI Application | Web framework |
| CORS Middleware | Cross-Origin Resource Sharing |
| Jinja2 Templates | HTML rendering |
| Training Endpoint | Execute Training Pipeline |
| Prediction Endpoint | Generate predictions |

---

# Application Initialization

The application begins by:

- Loading environment variables.
- Creating the FastAPI application.
- Configuring middleware.
- Connecting required services.
- Initializing template rendering.

This setup occurs only once when the application starts.

---

# Environment Configuration

The API loads configuration from the project's `.env` file.

Typical configuration includes:

- MongoDB connection string
- MLflow settings
- Cloud configuration

Keeping configuration external allows the application to run across multiple environments without code changes.

---

# FastAPI Application

The application creates a FastAPI instance that serves as the entry point for all HTTP requests.

Current responsibilities include:

- Registering routes
- Serving Swagger documentation
- Processing prediction requests
- Triggering model training

---

# Middleware

The project currently configures **CORS (Cross-Origin Resource Sharing)** middleware.

CORS allows browser-based applications running on different origins to communicate with the API.

This is especially useful when the frontend and backend are deployed separately.

---

# HTML Templates

Prediction results are rendered using **Jinja2 Templates**.

Current template:

```text
templates/

table.html
```

Instead of returning raw JSON, prediction results are displayed in a formatted HTML table.

This improves readability during development and demonstration.

---

# API Endpoints

The current implementation exposes two primary endpoints.

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/train` | GET | Execute the complete training pipeline |
| `/predict` | POST | Generate predictions from uploaded datasets |

---

# Training Endpoint

The `/train` endpoint provides an API interface for executing the complete Machine Learning pipeline.

Execution flow:

```text
HTTP Request

↓

TrainingPipeline

↓

Data Ingestion

↓

Data Validation

↓

Data Transformation

↓

Model Training

↓

Save Model

↓

HTTP Response
```

This endpoint automates the complete model training workflow.

---

# Prediction Endpoint

The `/predict` endpoint generates predictions for uploaded datasets.

Execution flow:

```text
Upload CSV

↓

Read CSV

↓

Load Preprocessor

↓

Load Trained Model

↓

Create NetworkModel

↓

Generate Predictions

↓

Append Prediction Column

↓

Render HTML Table
```

The endpoint returns prediction results without retraining the model.

---

# Model Loading

The inference process loads:

```text
preprocessor.pkl

+

model.pkl

↓

NetworkModel
```

The loaded NetworkModel ensures that every prediction undergoes the same preprocessing steps used during training.

---

# Prediction Workflow

The complete prediction workflow is shown below.

```text
CSV Upload

↓

Pandas DataFrame

↓

NetworkModel

↓

Preprocessing

↓

Classifier

↓

Predictions

↓

Prediction DataFrame

↓

HTML Rendering
```

This guarantees consistent feature processing during inference.

---

# HTML Rendering

After predictions are generated:

- A new prediction column is added.
- The updated DataFrame is converted to HTML.
- Jinja2 injects the table into `table.html`.
- The formatted page is returned to the browser.

This provides an interactive way to inspect prediction results.

---

# Data Flow

```text
Client

↓

FastAPI

↓

Prediction Endpoint

↓

NetworkModel

↓

Predictions

↓

HTML Response
```

---

# Error Handling

Potential issues include:

- Missing uploaded file.
- Invalid CSV format.
- Missing trained model.
- Missing preprocessing pipeline.
- Prediction failures.
- HTML rendering errors.

All exceptions are handled using the project's custom exception framework.

---

# Design Decisions

Several architectural decisions improve the maintainability of the API.

### Separate Training and Inference

Training and prediction are independent workflows.

A trained model can serve many prediction requests without retraining.

---

### RESTful API

FastAPI provides a clean interface for interacting with the Machine Learning pipeline.

---

### Persistent Models

The model is loaded from disk rather than retrained for each request.

---

### HTML-Based Output

Prediction results are presented in an easily readable format using Jinja2 templates.

---

### Modular Design

The API delegates Machine Learning tasks to the Training Pipeline and NetworkModel rather than implementing them directly.

---

# Software Engineering Patterns

The Inference API demonstrates several architectural patterns.

| Pattern | Purpose |
|----------|---------|
| Facade Pattern | Provides a simplified interface to the ML pipeline |
| MVC-like Separation | API, templates, and ML logic remain independent |
| Dependency Injection | Loads configuration externally |
| Composition | Combines preprocessing and classifier through NetworkModel |
| Single Responsibility Principle | Focuses exclusively on serving predictions |

---

# Implementation Notes

The current implementation includes:

- FastAPI application.
- Swagger documentation.
- `/train` endpoint.
- `/predict` endpoint.
- CSV upload support.
- Jinja2 HTML rendering.
- Prediction DataFrame generation.
- NetworkModel-based inference.

These notes reflect the current implementation and may evolve as additional API capabilities are introduced.

---

# Current Limitations

The current implementation has several limitations.

- Predictions are limited to CSV uploads.
- Model is loaded during prediction requests instead of application startup.
- No authentication or authorization.
- No request validation.
- Limited API documentation.
- No asynchronous prediction support.
- No model version selection.
- HTML output only (limited API response formats).

Additionally, during our review of the implementation, we identified several opportunities for improvement:

- The application currently loads the preprocessor and classifier separately before creating the `NetworkModel`. Persisting and loading the complete `NetworkModel` directly would simplify inference and reduce initialization logic.
- The trained model is loaded for prediction requests rather than being initialized once during application startup, which may introduce unnecessary overhead.
- The prediction output directory should be created automatically if it does not already exist.
- The HTML interface could be enhanced with summary statistics, download options, and improved styling for a better user experience.

These observations describe the current implementation and provide a roadmap for future enhancements.

---

# Future Improvements

Potential enhancements include:

- REST API versioning.
- JSON prediction responses.
- Batch prediction.
- Model registry integration.
- Authentication and authorization.
- Asynchronous inference.
- Background prediction jobs.
- Model caching at startup.
- Health check endpoints.
- Monitoring and logging.
- Interactive dashboard.

---

# Why the Inference API Matters

Training a Machine Learning model is only one part of a production system.

The Inference API transforms the trained model into a reusable service that can generate predictions for new data on demand.

By separating model training from model serving, the project achieves:

- Better scalability.
- Faster predictions.
- Easier deployment.
- Independent model updates.
- Cleaner software architecture.

This separation is a key characteristic of production Machine Learning systems.

---

# Training vs. Inference Architecture

                TRAINING

MongoDB
    │
    ▼
Training Pipeline
    │
    ▼
NetworkModel
    │
    ▼
Saved Model


                INFERENCE

Client
    │
    ▼
FastAPI
    │
    ▼
Load Saved NetworkModel
    │
    ▼
Prediction
    │
    ▼
Response

---

# Summary

The Inference API provides a production-oriented interface for interacting with the trained Machine Learning model.

Using FastAPI, the application exposes endpoints for both model training and prediction while ensuring that identical preprocessing is applied during inference through the `NetworkModel`.

This design separates model development from model serving, enabling reusable, maintainable, and scalable deployment of the Machine Learning pipeline.

---

# Next Document

Continue with:

```text
11_Utilities.md
```

to understand the shared utility modules that support every stage of the Machine Learning pipeline.