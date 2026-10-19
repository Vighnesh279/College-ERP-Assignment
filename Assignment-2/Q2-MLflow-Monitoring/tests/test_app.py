import app as prediction_api


class FakeModel:
    def predict(self, features):
        return [0]


def test_homepage():
    client = prediction_api.app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["service"] == "Iris ML Prediction API"


def test_health_endpoint():
    client = prediction_api.app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "service": "iris-ml-api",
    }


def test_invalid_prediction_input():
    client = prediction_api.app.test_client()
    response = client.post("/predict", json={"features": [1.0, 2.0]})

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_successful_prediction(monkeypatch):
    monkeypatch.setattr(
        prediction_api,
        "get_model",
        lambda: FakeModel(),
    )

    client = prediction_api.app.test_client()
    response = client.post(
        "/predict",
        json={"features": [5.1, 3.5, 1.4, 0.2]},
    )

    assert response.status_code == 200
    assert response.get_json()["prediction"] == 0
    assert response.get_json()["class_name"] == "setosa"


def test_prometheus_metrics_endpoint():
    client = prediction_api.app.test_client()
    response = client.get("/metrics")

    assert response.status_code == 200
    assert b"iris_prediction_requests_total" in response.data