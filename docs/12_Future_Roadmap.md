# Future Roadmap

The current repository implements a modular Machine Learning pipeline for network security data, covering the complete lifecycle from data ingestion to model deployment through a FastAPI application.

While this architecture provides a strong production-ready foundation, it represents only the first stage of a broader vision.

The long-term objective is to evolve this repository into an **AI-powered Network Security Log Triage Agent** capable of analyzing security events, retrieving relevant contextual knowledge, reasoning over evidence, and assisting security analysts during incident investigation.

This document outlines that planned evolution.

---

# Vision

The current project focuses on **classification**.

The future project will focus on **security investigation**.

Instead of simply predicting whether an event is malicious, the system will answer questions such as:

- What happened?
- Why was this event flagged?
- How severe is the threat?
- Which evidence supports this conclusion?
- What should the analyst do next?

The objective is to transform the project from a Machine Learning model into an intelligent security assistant.

---

# Repository Evolution

The planned evolution of the repository is illustrated below.

```text
Version 1
│
▼
Machine Learning Pipeline
│
▼
Version 2
│
▼
Production ML Platform
│
▼
Version 3
│
▼
AI-Powered Log Triage Agent
│
▼
Version 4
│
▼
Autonomous Security Investigation Platform
```

Each version builds upon the previous one rather than replacing it.

---

# Current State (Version 1)

The current repository already includes:

- Data ingestion from MongoDB
- Dataset validation
- Dataset drift detection
- Feature preprocessing
- Multiple candidate models
- Hyperparameter optimization
- MLflow experiment tracking
- FastAPI inference
- Modular architecture
- Artifact-driven workflow

These capabilities provide a strong foundation for future AI-based enhancements.

---

# Phase 1 — Production Machine Learning

The first stage of evolution focuses on strengthening the existing ML pipeline.

Potential enhancements include:

- Improved feature engineering
- Advanced preprocessing pipelines
- Additional classification algorithms
- Explainable AI (SHAP/LIME)
- Automated retraining
- Model monitoring
- Performance dashboards
- CI/CD integration
- Model registry
- Container orchestration

The goal of this phase is to improve reliability, maintainability, and production readiness.

---

# Phase 2 — Security Log Intelligence

Once the core pipeline is mature, the project can evolve from structured tabular data to real-world security logs.

Potential capabilities include:

- Log ingestion from multiple sources
- Syslog support
- Firewall log parsing
- IDS/IPS log processing
- Endpoint security events
- Cloud security logs
- Log normalization
- Event enrichment

Rather than classifying preprocessed datasets, the system will process raw security events.

---

# Phase 3 — Retrieval-Augmented Generation (RAG)

Security analysts often require additional context to investigate alerts.

This phase introduces Retrieval-Augmented Generation (RAG) to provide contextual information alongside predictions.

Possible knowledge sources include:

- Security documentation
- MITRE ATT&CK
- Internal playbooks
- Incident response guides
- Vendor advisories
- CVE databases

Conceptually:

```text
Security Alert

↓

Retrieve Relevant Knowledge

↓

Large Language Model

↓

Context-Aware Response
```

The objective is to generate responses that are grounded in trusted security knowledge.

---

# Phase 4 — Agentic AI

The next stage introduces AI agents capable of coordinating multiple investigation tasks.

Rather than answering a single question, the system will execute workflows such as:

- Understanding the alert
- Gathering additional evidence
- Searching knowledge bases
- Summarizing findings
- Recommending remediation steps

A conceptual workflow is shown below.

```text
Security Alert

↓

Planning Agent

↓

Evidence Collection

↓

Knowledge Retrieval

↓

Reasoning

↓

Investigation Report
```

This transforms the application from a predictive model into an investigative assistant.

---

# Phase 5 — Multi-Agent Security Platform

As the project grows, specialized AI agents can collaborate to perform complex investigations.

Possible agent roles include:

- Log Analysis Agent
- Threat Intelligence Agent
- Retrieval Agent
- Investigation Agent
- Report Generation Agent
- Recommendation Agent

Conceptually:

```text
Security Event

↓

Orchestrator

├── Log Agent
├── Threat Agent
├── Retrieval Agent
├── Investigation Agent
└── Reporting Agent

↓

Unified Investigation Report
```

Each agent focuses on a specific responsibility while collaborating through an orchestration framework.

---

# Proposed Technology Evolution

The project is expected to evolve alongside its architecture.

| Current Technology | Planned Evolution |
|--------------------|-------------------|
| Classical ML | Hybrid AI + LLM |
| Tabular Data | Security Logs |
| Scikit-learn | ML + Deep Learning |
| FastAPI | AI Service Platform |
| MongoDB | Vector Database + Knowledge Base |
| MLflow | MLflow + Model Registry |
| Local Files | Object Storage |
| Rule-Based Workflow | Agentic Workflow |

---

# Architectural Evolution

The system architecture will gradually expand.

Current architecture:

```text
Data

↓

ML Pipeline

↓

Model

↓

FastAPI
```

Future architecture:

```text
Security Logs

↓

Log Processing

↓

Feature Engineering

↓

ML Detection

↓

Knowledge Retrieval

↓

LLM Reasoning

↓

AI Agents

↓

Security Investigation Report
```

The existing pipeline remains a core component within this larger architecture.

---

# Expected Repository Structure

As the project evolves, the repository may be organized as follows.

```text
network-security-agent/

├── ingestion/
├── preprocessing/
├── detection/
├── rag/
├── agents/
├── vector_store/
├── prompts/
├── evaluation/
├── api/
├── frontend/
├── docs/
└── deployment/
```

This structure separates concerns while supporting future expansion.

---

# Learning Roadmap

Developing the future vision requires expertise across multiple domains.

Recommended learning areas include:

### Machine Learning

- Advanced feature engineering
- Model optimization
- Explainable AI
- MLOps

### Cybersecurity

- Network protocols
- Threat detection
- Security Operations Center (SOC) workflows
- MITRE ATT&CK
- SIEM platforms

### Large Language Models

- Prompt engineering
- Fine-tuning
- Evaluation
- Guardrails

### Retrieval-Augmented Generation

- Vector databases
- Embedding models
- Hybrid retrieval
- Reranking

### Agentic AI

- LangGraph
- Multi-agent orchestration
- Tool integration
- Planning and memory

---

# Development Principles

The future project will continue to follow the principles established in the current repository.

- Modular architecture
- Separation of concerns
- Configuration-driven design
- Artifact-based communication
- Reusable components
- Experiment tracking
- Reproducible workflows
- Incremental development

These principles ensure that new capabilities can be added without fundamentally changing the existing architecture.

---

# Long-Term Goal

The ultimate objective is to build an intelligent system that assists security analysts throughout the incident response lifecycle.

Rather than acting solely as a classifier, the system should:

- Detect suspicious activity.
- Explain why it is suspicious.
- Retrieve supporting evidence.
- Recommend next steps.
- Produce structured investigation reports.
- Reduce analyst workload.
- Improve investigation consistency.

This vision extends beyond Machine Learning toward AI-assisted cybersecurity operations.

---

# Summary

The current repository establishes a strong foundation through a modular Machine Learning pipeline that supports data ingestion, validation, transformation, model training, and inference.

Future development will build upon this foundation by incorporating security log processing, Retrieval-Augmented Generation (RAG), Large Language Models, and Agentic AI to create an intelligent Network Security Log Triage Agent.

By evolving incrementally, each new capability can leverage the existing architecture while expanding the system from a predictive model into a comprehensive AI-powered security investigation platform.

# Project Journey

Student ML Project
        │
        ▼
Network Security ML Pipeline
        │
        ▼
Production ML System
        │
        ▼
AI-Powered Log Triage Agent
        │
        ▼
Multi-Agent Security Platform
        │
        ▼
Autonomous Security Investigation System

---