# Q2 - MLflow Model Tracking and Monitoring

## 1. Project Overview

This project demonstrates an end-to-end machine learning workflow using MLflow, Flask, Docker, Prometheus, and Grafana.

A Random Forest classifier is trained on the Iris dataset. MLflow tracks the experiment and manages the registered model. A Flask REST API serves predictions, while Prometheus collects application metrics and Grafana visualizes the monitoring data.

## 2. Objectives

- Train and evaluate an Iris classification model.
- Track experiment parameters, metrics, and model artifacts using MLflow.
- Register the model as IrisClassifier and assign the champion alias.
- Serve model predictions through a Flask API.
- Containerize and orchestrate services using Docker Compose.
- Monitor requests, errors, and prediction latency using Prometheus.
- Visualize monitoring metrics using Grafana.
- Validate API functionality with automated tests.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Model training and API development |
| Scikit-learn | Random Forest classifier and Iris dataset |
| MLflow | Experiment tracking and model registry |
| Flask | Prediction REST API |
| Docker | Containerization |
| Docker Compose | Multi-service orchestration |
| Prometheus | Metrics collection |
| Grafana | Monitoring dashboard |
| Pytest | Automated testing |

## 4. Project Files

- `app.py` - Flask prediction API and Prometheus metrics.
- `train_model.py` - Model training, evaluation, and registration.
- `requirements.txt` - Python dependencies.
- `Dockerfile` - Image definition for the Python services.
- `docker-compose.yml` - Configuration for all five services.
- `prometheus.yml` - Prometheus scrape configuration.
- `tests/test_app.py` - Automated API tests.
- `grafana/` - Dashboard and data source provisioning.
- `Screenshots/` - Project execution and verification evidence.

## 5. System Architecture

1. The trainer trains a Random Forest classifier using the Iris dataset.
2. MLflow records parameters, evaluation metrics, and model artifacts.
3. The model is registered as `IrisClassifier` with the `champion` alias.
4. Flask loads the registered model and serves predictions.
5. Prometheus scrapes metrics from the API.
6. Grafana queries Prometheus and displays monitoring visualizations.
7. Pytest checks the API and metrics endpoint.

## 6. Prerequisites

- Docker Desktop or Docker Engine.
- Docker Compose.
- An internet connection for the initial image builds.

The Python dependencies are installed inside the Docker image.

## 7. Running the Project

Run these commands from the repository root.

### Start all services

`docker compose -f Assignment-2/Q2-MLflow-Monitoring/docker-compose.yml up --build -d`

### Check service status

`docker compose -f Assignment-2/Q2-MLflow-Monitoring/docker-compose.yml ps`

### View training logs

`docker compose -f Assignment-2/Q2-MLflow-Monitoring/docker-compose.yml logs trainer`

### Stop services

`docker compose -f Assignment-2/Q2-MLflow-Monitoring/docker-compose.yml down`

Docker named volumes store MLflow, Prometheus, and Grafana data.

## 8. Service URLs

| Service | URL |
|---|---|
| MLflow Tracking UI | http://localhost:5001 |
| Prediction API | http://localhost:5002 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

The initial Grafana credentials are `admin` / `admin`. Change the password if prompted.

## 9. API Endpoints

### Homepage

`GET /`

Returns basic information about the API.

### Health check

`GET /health`

Example response:

`{"service":"iris-ml-api","status":"ok"}`

### Make a prediction

`POST /predict`

Example JSON request:

`{"features":[5.1,3.5,1.4,0.2]}`

The API accepts four numeric Iris features and returns the predicted class, model name, and model alias.

Example response:

`{"alias":"champion","class_name":"setosa","model":"IrisClassifier","prediction":0}`

### Application metrics

`GET /metrics`

Exposes prediction request counts, prediction error counts, and a prediction latency histogram for Prometheus.

## 10. Monitoring

Prometheus scrapes the API metrics endpoint at `http://api:5002/metrics`.

The Grafana ML Monitoring Dashboard contains three panels:

- **Prediction Requests per Minute** - Displays prediction activity.
- **Prediction Errors per Minute** - Displays prediction failures.
- **Average Prediction Latency** - Displays average prediction processing time.

An error rate of zero is expected when prediction requests succeed.

## 11. Automated Testing

Run the tests from the repository root:

`docker compose -f Assignment-2/Q2-MLflow-Monitoring/docker-compose.yml run --rm api python -m pytest -v tests/test_app.py`

The test suite covers:

1. Homepage response.
2. Health endpoint.
3. Invalid prediction input.
4. Successful prediction.
5. Prometheus metrics endpoint.

**Verified result: 5 passed, 9 warnings.**

The warnings were non-fatal deprecation warnings from MLflow and its dependencies.

## 12. Screenshots and Evidence

The `Screenshots/` directory contains evidence of the following:

| File | Evidence |
|---|---|
| `01-mlflow-tracking-ui.png` | MLflow tracking interface |
| `01-mlflow-experiment-run.png` | Experiment run details |
| `02-mlflow-registered-model.png` | Registered model |
| `03-prediction-api.png` | Prediction API response |
| `04-prometheus-targets.png` | Prometheus target status |
| `05-grafana-dashboard.png` | Grafana monitoring dashboard |
| `05-grafana-dashboard-initial.png` | Initial Grafana dashboard |
| `06-automated-tests-passed.png` | Passing automated tests |

## 13. Conclusion

This project implements a machine learning lifecycle with experiment tracking, model registration, API deployment, containerization, automated testing, and monitoring.

MLflow manages the model lifecycle, Flask serves predictions, Docker Compose orchestrates services, Prometheus collects operational metrics, and Grafana visualizes the monitoring data.