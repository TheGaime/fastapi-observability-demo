# FastAPI Observability Demo

A small public-safe demo service showing structured JSON logging, health/readiness endpoints, Prometheus metrics, and environment-based configuration.

## Why I built this

I built this as a lightweight public example of the kind of backend support, observability, and operational tooling work I do on private systems.

## Features

- FastAPI API service
- Structured JSON logs to stdout
- `/health` and `/ready` endpoints
- Prometheus metrics at `/metrics`
- Controlled logging endpoint at `/log-test`
- Controlled error endpoint at `/error-test`
- Docker-ready local setup
- Environment-based configuration via `.env`

## Safe separation from private work

This project is intentionally standalone:
- no imports from private repositories
- no production credentials
- no customer names
- no internal IPs
- no proprietary trading logic
