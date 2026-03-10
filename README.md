# End-to-End MLOps Pipeline Production

A production-grade MLOps project covering the full lifecycle of a machine learning system — from data ingestion and model training to evaluation, serving, and CI/CD deployment.

**Built by:** Shubham Haranale

---

## What This Project Does

This project demonstrates how to build and deploy a complete ML pipeline in production using modern MLOps tools and best practices:

- **Data** — Load, validate, and preprocess datasets for training
- **Training** — Train an NLP classification model with experiment tracking
- **Tuning** — Hyperparameter optimization for best model performance
- **Evaluation** — Evaluate model quality with structured metrics
- **Serving** — Deploy the model as a REST API using Ray Serve
- **CI/CD** — Automated testing and deployment with GitHub Actions

---

## What I Learned

- How to structure a **production ML codebase** with proper modularity
- Using **Ray** for distributed training and model serving at scale
- Setting up **CI/CD pipelines** with GitHub Actions for automated ML workflows
- Writing **unit tests and model tests** to validate ML code and outputs
- Managing configs, environments, and dependencies for reproducible ML
- End-to-end MLOps concepts: data → train → evaluate → serve → monitor

---

## Project Structure

```
.
├── madewithml/              # Core ML package
│   ├── config.py            # Project configuration
│   ├── data.py              # Data loading and preprocessing
│   ├── train.py             # Model training
│   ├── tune.py              # Hyperparameter tuning
│   ├── evaluate.py          # Model evaluation
│   ├── predict.py           # Inference logic
│   ├── serve.py             # Ray Serve deployment
│   └── utils.py             # Utility functions
├── notebooks/               # Exploratory notebooks
├── tests/                   # Unit and model tests
│   ├── code/                # Code tests
│   └── model/               # Model behavior tests
├── deploy/                  # Deployment configs
│   ├── jobs/                # Ray job definitions
│   ├── services/            # Serve configs
│   └── cluster_env.yaml     # Cluster environment
├── .github/workflows/       # CI/CD pipelines
├── docs/                    # Project documentation
├── datasets/                # Dataset files
├── pyproject.toml           # Project metadata
├── requirements.txt         # Python dependencies
└── Makefile                 # Useful commands
```

---

## Setup & Running Locally

### 1. Create virtual environment

```bash
conda create --name mlops-pipeline python=3.10
conda activate mlops-pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python -m madewithml.train
```

### 4. Evaluate the model

```bash
python -m madewithml.evaluate
```

### 5. Serve the model

```bash
python -m madewithml.serve
```

---

## Running Tests

```bash
# Code tests
pytest tests/code/

# Model tests
pytest tests/model/
```

---

## Tech Stack

- **ML Framework:** PyTorch, Transformers (HuggingFace)
- **Distributed Computing:** Ray (Train, Tune, Serve)
- **Experiment Tracking:** MLflow
- **CI/CD:** GitHub Actions
- **Testing:** Pytest
- **Docs:** MkDocs
- **Concepts:** MLOps, model serving, distributed training, CI/CD, hyperparameter tuning

---

## Acknowledgement

Project inspired by the [Made With ML](https://github.com/GokuMohandas/Made-With-ML) MLOps curriculum.
