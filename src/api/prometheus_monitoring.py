"""
Module: monitoring
Description: This module contains functions for prometheus
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
import os
from typing import Callable
from prometheus_client import Histogram
from prometheus_fastapi_instrumentator import Instrumentator, metrics
from prometheus_fastapi_instrumentator.metrics import Info

NAMESPACE = os.environ.get("METRICS_NAMESPACE", "fastapi")
SUBSYSTEM = os.environ.get("METRICS_SUBSYSTEM", "model")

instrumentator = Instrumentator(
    should_group_status_codes=True,
    should_ignore_untemplated=True,
    should_instrument_requests_inprogress=True,
    excluded_handlers=["/metrics"],
    inprogress_name="fastapi_inprogress",
    inprogress_labels=True
)

# Metrics

instrumentator.add(
    metrics.request_size(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        metric_name="prediction_request_size",
        metric_doc="Size of prediction requests",
        metric_namespace=NAMESPACE,
        metric_subsystem=SUBSYSTEM,
    )
)
instrumentator.add(
    metrics.response_size(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        metric_name="prediction_response_size",
        metric_doc="Size of prediction responses",
        metric_namespace=NAMESPACE,
        metric_subsystem=SUBSYSTEM,
    )
)
instrumentator.add(
    metrics.latency(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        metric_name="prediction_latency",
        metric_doc="Latency of message prediction",
        metric_namespace=NAMESPACE,
        metric_subsystem=SUBSYSTEM,
    )
)
instrumentator.add(
    metrics.requests(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        metric_name="total_predictions",
        metric_doc="Total number of message predictions",
        metric_namespace=NAMESPACE,
        metric_subsystem=SUBSYSTEM,
    )
)

def prediction_result_metric(
    metric_name: str = "prediction_result",
    metric_doc: str = "Outcome of message prediction",
    metric_namespace: str = "",
    metric_subsystem: str = "",
    buckets=(0, 1),
) -> Callable[[Info], None]:
    """
    Function: prediction_result_metric.
    This function creates a Prometheus Histogram metric for tracking 
    prediction outcomes in a classification model with specific label categories.
    """
    metric = Histogram(
        metric_name,
        metric_doc,
        labelnames=["prediction_type"],
        buckets=buckets,
        namespace=metric_namespace,
        subsystem=metric_subsystem,
    )

    metric.labels("non_sexist")
    metric.labels("sexist")
    metric.labels("sexist_animosity")
    metric.labels("sexist_threats")
    metric.labels("sexist_derogation")
    metric.labels("sexist_prejudiced")

    def instrumentation(info: Info) -> None:
        """
        Function: instrumentation.
        This function observes prediction outcomes for a sexism classification 
        model and updates the corresponding Prometheus metric.
        """
        if info.modified_handler == "/prediction_sexism":
            prediction_type = info.response.headers.get("X-message-prediction-type")
            if prediction_type:
                metric.labels(prediction_type).observe(1.0)

    return instrumentation


instrumentator.add(prediction_result_metric(metric_namespace=NAMESPACE, metric_subsystem=SUBSYSTEM))
