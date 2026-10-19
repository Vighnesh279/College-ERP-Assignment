import os

import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
from mlflow.tracking import MlflowClient
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5001")
EXPERIMENT_NAME = "Iris Classification"
MODEL_NAME = "IrisClassifier"


def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)

    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        random_state=42,
        stratify=iris.target,
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42,
    )

    with mlflow.start_run() as run:
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        weighted_f1 = f1_score(y_test, predictions, average="weighted")

        mlflow.log_params(
            {
                "model_type": "RandomForestClassifier",
                "n_estimators": 100,
                "max_depth": 5,
                "random_state": 42,
                "test_size": 0.2,
                "dataset": "Iris",
            }
        )

        mlflow.log_metrics(
            {
                "accuracy": float(accuracy),
                "weighted_f1": float(weighted_f1),
            }
        )

        signature = infer_signature(X_train, model.predict(X_train))

        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="iris_model",
            registered_model_name=MODEL_NAME,
            input_example=X_train[:3],
            signature=signature,
        )

        run_id = run.info.run_id

    client = MlflowClient()
    versions = client.search_model_versions(f"name='{MODEL_NAME}'")

    if not versions:
        raise RuntimeError("The model was not registered successfully.")

    latest_version = max(versions, key=lambda version: int(version.version))
    client.set_registered_model_alias(
        MODEL_NAME,
        "champion",
        latest_version.version,
    )

    print("Model training completed successfully.")
    print(f"Experiment: {EXPERIMENT_NAME}")
    print(f"Run ID: {run_id}")
    print(f"Registered model: {MODEL_NAME}")
    print(f"Model version: {latest_version.version}")
    print(f"Model alias: champion")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Weighted F1 score: {weighted_f1:.4f}")


if __name__ == "__main__":
    main()