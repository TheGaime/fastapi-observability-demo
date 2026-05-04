from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app, raise_server_exceptions=False)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "FastAPI Observability Demo"
    assert "version" in data


def test_ready_endpoint():
    response = client.get("/ready")

    assert response.status_code == 200
    data = response.json()
    assert data["ready"] is True
    assert "metrics_enabled" in data


def test_log_test_endpoint():
    response = client.get("/log-test")

    assert response.status_code == 200
    assert response.json() == {"logged": True}


def test_error_test_endpoint_returns_500():
    response = client.get("/error-test")

    assert response.status_code == 500


def test_metrics_endpoint_exposes_prometheus_metrics():
    client.get("/health")
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "text/plain" in response.headers["content-type"]

    body = response.text
    assert "demo_requests_total" in body
    assert "demo_request_latency_seconds" in body
