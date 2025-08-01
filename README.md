# Colorectal Cancer Prediction MLOps Pipeline

A complete machine learning operations pipeline for predicting colorectal cancer using modern MLOps tools and practices. This project demonstrates end-to-end ML workflow deployment on Google Cloud Platform with Kubernetes orchestration.

## Overview

This project implements a comprehensive MLOps pipeline that predicts colorectal cancer using patient data. The pipeline includes data processing, model training, experiment tracking, and deployment using industry-standard tools like Kubeflow, MLflow, and Kubernetes.

## Features

- **End-to-end ML Pipeline**: Complete workflow from data ingestion to model deployment
- **Experiment Tracking**: MLflow integration for tracking experiments and model versions
- **Container Orchestration**: Kubernetes deployment with Minikube for local development
- **CI/CD Integration**: GitLab CI and Jenkins pipeline automation
- **Monitoring & Visualization**: Prometheus and Grafana for pipeline monitoring
- **REST API**: Flask-based API for model predictions
- **Scalable Architecture**: Google Cloud Platform deployment ready

## Tech Stack

- **ML Framework**: Scikit-learn
- **Orchestration**: Kubeflow Pipelines (KFP)
- **Experiment Tracking**: MLflow
- **Container Platform**: Kubernetes, Minikube
- **CI/CD**: GitLab CI, Jenkins
- **Monitoring**: Prometheus, Grafana
- **API Framework**: Flask
- **Cloud Platform**: Google Cloud Platform (GCP)
- **Data Visualization**: Matplotlib, Seaborn

## Dataset

The project uses colorectal cancer dataset from Kaggle, containing patient clinical features and histopathological data for cancer prediction.

## Installation

### Prerequisites
- Python 3.8+
- Docker
- Minikube
- kubectl
- Google Cloud SDK (for GCP deployment)

### Dependencies
```bash
pip install pandas numpy setuptools scikit-learn Flask joblib matplotlib seaborn mlflow kfp
```

### Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/colorectal-cancer-prediction-mlops.git
cd colorectal-cancer-prediction-mlops
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Start Minikube:
```bash
minikube start
```

4. Deploy Kubeflow Pipelines:
```bash
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=1.8.5"
kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=1.8.5"
```

## Usage

### Running the Pipeline
1. Start MLflow tracking server:
```bash
mlflow ui --host 0.0.0.0 --port 5000
```

2. Execute the training pipeline:
```bash
python src/train_pipeline.py
```

3. Deploy the model:
```bash
python src/deploy_model.py
```

### Making Predictions
Start the Flask API:
```bash
python app.py
```

Send POST request to `http://localhost:5000/predict` with patient data in JSON format.

## Project Structure
```
├── src/
│   ├── data_processing.py
│   ├── model_training.py
│   ├── train_pipeline.py
│   └── deploy_model.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── config/
│   ├── kubeflow/
│   └── monitoring/
├── app.py
├── requirements.txt
└── README.md
```

## Pipeline Components

1. **Data Processing**: Handles data cleaning, feature engineering, and preprocessing
2. **Model Training**: Trains multiple ML models and selects the best performer
3. **Experiment Tracking**: Logs experiments, parameters, and metrics using MLflow
4. **Model Deployment**: Deploys trained models to Kubernetes cluster
5. **Monitoring**: Tracks model performance and pipeline health

## Monitoring

Access monitoring dashboards:
- **MLflow UI**: `http://localhost:5000`
- **Kubeflow Pipelines**: `kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80`
- **Grafana**: `kubectl port-forward svc/grafana 3000:80`

## Results

The pipeline achieves consistent model performance with automated retraining capabilities. All experiments are tracked and models are versioned for reproducibility.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Kaggle for providing the colorectal cancer dataset
- Kubeflow community for the excellent pipeline framework
- MLflow team for experiment tracking capabilities
