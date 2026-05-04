# FastAPI Observability Demo

A small, public-safe FastAPI backend demo showing health checks, readiness checks, structured JSON logging, Prometheus metrics, Docker setup, tests, and CI.

## Why I built this

I built this as a lightweight public example of backend support, observability, and operational reliability workflows that I use on private platform work.

It is intentionally simple, readable, and safe to share with recruiters.

## What this demonstrates

- FastAPI API service
- Health and readiness endpoints
- Structured JSON logs to stdout
- Prometheus metrics endpoint
- Request-count and latency instrumentation
- Controlled log and error test endpoints
- Environment-based configuration
- Docker and Docker Compose setup
- Pytest test coverage
- GitHub Actions CI

## Endpoints

| Endpoint | Purpose |
|---|---|
| /health | Basic service health check |
| /ready | Readiness check with metrics flag |
| /metrics | Prometheus metrics output |
| /log-test | Emits a structured JSON log |
| /error-test | Raises a controlled demo error for observability testing |

## Local quick start

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    cp .env.example .env
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8011

Open:

    http://127.0.0.1:8011/health
    http://127.0.0.1:8011/ready
    http://127.0.0.1:8011/metrics

## Docker quick start

    cp .env.example .env
    docker compose up --build

Then test:

    curl http://127.0.0.1:8011/health
    curl http://127.0.0.1:8011/ready
    curl http://127.0.0.1:8011/log-test
    curl http://127.0.0.1:8011/metrics

## Run tests

    pytest -q

## Safe separation from private work

This project is intentionally standalone:

- no imports from private repositories
- no production credentials
- no customer names
- no internal IPs
- no proprietary trading logic

## Notes

This is a lightweight public demo, not a full production platform template. Its purpose is to show practical backend observability patterns in a clean, safe, recruiter-friendly repository.
