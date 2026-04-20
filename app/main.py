import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from starlette.middleware.base import BaseHTTPMiddleware

from .config import settings
from .logging_config import setup_logging
from .metrics import REQUEST_COUNT, ERROR_COUNT, REQUEST_LATENCY, metrics_response


setup_logging()
logger = logging.getLogger("demo.api")


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        method = request.method
        started = time.perf_counter()

        try:
            response = await call_next(request)
            status_code = str(response.status_code)
            return response
        except Exception:
            ERROR_COUNT.labels(path=path).inc()
            logger.exception(
                "request_failed",
                extra={"extra_fields": {"method": method, "path": path}},
            )
            raise
        finally:
            duration = time.perf_counter() - started
            REQUEST_LATENCY.labels(method=method, path=path).observe(duration)
            status = locals().get("status_code", "500")
            REQUEST_COUNT.labels(method=method, path=path, status_code=status).inc()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(
        "service_starting",
        extra={"extra_fields": {"version": settings.app_version, "env": settings.app_env}},
    )
    yield
    logger.info("service_stopping")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)
app.add_middleware(MetricsMiddleware)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
    }


@app.get("/ready")
async def ready():
    return {
        "ready": True,
        "metrics_enabled": settings.metrics_enabled,
    }


@app.get("/log-test")
async def log_test():
    logger.info(
        "manual_log_test",
        extra={"extra_fields": {"endpoint": "/log-test", "note": "structured log emitted"}},
    )
    return {"logged": True}


@app.get("/error-test")
async def error_test():
    raise RuntimeError("Controlled demo error for observability testing")


@app.get("/metrics")
async def metrics():
    body, content_type = metrics_response()
    return PlainTextResponse(content=body.decode("utf-8"), media_type=content_type)
