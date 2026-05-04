from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest


REQUEST_COUNT = Counter(
    "demo_requests_total",
    "Total number of demo requests",
    ["method", "path", "status_code"],
)

ERROR_COUNT = Counter(
    "demo_errors_total",
    "Total number of demo errors",
    ["path"],
)

REQUEST_LATENCY = Histogram(
    "demo_request_latency_seconds",
    "Request latency in seconds",
    ["method", "path"],
)


def metrics_response():
    return generate_latest(), CONTENT_TYPE_LATEST
