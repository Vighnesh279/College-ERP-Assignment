import os
import time

import mlflow
import mlflow.pyfunc
import numpy as np
from flask import Flask, jsonify, request
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    Histogram,
    generate_latest,
)
from sklearn.datasets import load_iris

app = Flask(__name__)

MLFLOW_TRACKING_URI = os.getenv(
    "MLFLOW_TRACKING_URI", "http://localhost:5001"
)
MODEL_NAME = "IrisClassifier"
MODEL_ALIAS = "champion"
IRIS_NAMES = load_iris().target_names.tolist()

PREDICTION_REQUESTS = Counter(
    "iris_prediction_requests_total",
    "Total number of prediction requests",
)
PREDICTION_ERRORS = Counter(
    "iris_prediction_errors_total",
    "Total number of invalid or failed prediction requests",
)
PREDICTION_LATENCY = Histogram(
    "iris_prediction_duration_seconds",
    "Prediction request processing time in seconds",
)

_model = None


def get_model():
    global _model

    if _model is None:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        model_uri = f"models:/{MODEL_NAME}@{MODEL_ALIAS}"
        _model = mlflow.pyfunc.load_model(model_uri)

    return _model


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        service="Iris ML Prediction API",
        model=MODEL_NAME,
        alias=MODEL_ALIAS,
        endpoints={
            "health": "/health",
            "predict": "/predict",
            "metrics": "/metrics",
        },
    )


@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok", service="iris-ml-api"), 200


@app.route("/predict", methods=["POST"])
def predict():
    started = time.perf_counter()
    PREDICTION_REQUESTS.inc()

    try:
        payload = request.get_json(silent=True)

        if not isinstance(payload, dict):
            PREDICTION_ERRORS.inc()
            return jsonify(error="JSON object required"), 400

        features = payload.get("features")

        if not isinstance(features, list) or len(features) != 4:
            PREDICTION_ERRORS.inc()
            return jsonify(
                error="Provide exactly four numeric features"
            ), 400

        try:
            values = np.asarray(features, dtype=float)
        except (TypeError, ValueError):
            PREDICTION_ERRORS.inc()
            return jsonify(error="All features must be numeric"), 400

        if not np.isfinite(values).all():
            PREDICTION_ERRORS.inc()
            return jsonify(error="Features must be finite numbers"), 400

        model = get_model()
        prediction = int(model.predict(values.reshape(1, 4))[0])

        return jsonify(
            prediction=prediction,
            class_name=IRIS_NAMES[prediction],
            model=MODEL_NAME,
            alias=MODEL_ALIAS,
        ), 200

    except Exception:
        PREDICTION_ERRORS.inc()
        app.logger.exception("Prediction failed")
        return jsonify(error="Prediction service unavailable"), 503

    finally:
        PREDICTION_LATENCY.observe(time.perf_counter() - started)


@app.route("/metrics", methods=["GET"])
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)