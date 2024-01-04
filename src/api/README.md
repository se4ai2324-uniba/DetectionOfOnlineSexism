# API Documentation

## Introduction

The API for our system is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+. FastAPI leverages standard Python type hints for automatic data validation and documentation generation.
In addition, it explains the usage of Docker Compose to launch a monitoring infrastructure that includes Prometheus and Grafana, a custom backend ("backend"), and a frontend.

## Framework Used

### FastAPI

[FastAPI](https://fastapi.tiangolo.com/) is employed as the primary framework for building our API. It provides a robust and efficient foundation for creating API endpoints with Python, ensuring high performance and ease of use.

## System Functionalities

The API supports the following system functionalities through two distinct tasks:

1. **Sexism Detection Task:**
   - **Endpoint:** `/prediction_sexism`

2. **Category Detection Task:**
   - **Endpoint:** `/prediction_category`

## Usage

To run the FastAPI server, execute the following command:

```bash
uvicorn main:app --reload
```
## Swagger UI
It is possible to test the API  using Swagger UI, a user-friendly interface that simplifies the understanding of API functionalities. To access to the Swagger UI, navigate to:

```bash
http://127.0.0.1:8000/docs
```
Here is showed the main window of the UI.

![SwaggerUI](../../references/images_doc/SwaggerUI.png)

As we can see in the picture there are two endpoint used to make the prediction of a given message. 

Here there is an example of the `/prediction_sexism` endpoint.

![Sexism1](../../references/images_doc/Sexism1.png)

In the response body is showned the message that has been inserted from the user and the prediction.

![Sexism2](../../references/images_doc/Sexism2.png)

Instead here we have an example  of the `/prediction_category` endpoint. The user has to insert the message and then it will be displayed the result.

![Category1](../../references/images_doc/Category1.png)

Documentation: Docker Compose with Prometheus
Introduction


## Prometheus
Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects metrics from configured targets at specified intervals, evaluates rule expressions, and can trigger alerts if conditions are met.

Prometheus scrapes metrics from the "backend" service, as specified in the configuration file. The collected metrics are stored locally in a time-series database.
Prometheus provides a query language (PromQL) for querying and processing the collected metrics.

In order to acquire the metrics, fastAPI and Prometheus have been connected using a docker compose file.
The provided docker-compose.yml file defines the following services:
-  **backend**: A service representing the backend of the application. It is built from the current context (".") and the resulting image is tagged as "detectiononlinesexism_backend." It exposes port 8000 for requests and also exposes it to be scraped by Prometheus.
-  **frontend**: A service representing the frontend of the application. It is built from the context of the "./frontend" folder, and the resulting image is tagged as "detectiononlinesexism_frontend." It exposes port 8080 for requests. It depends on the "backend" service.
-  **prometheus**: Uses the "prom/prometheus" image. It mounts the "./prometheus.yml" file into the container at "/etc/prometheus/prometheus.yml." It exposes port 9090 for accessing the Prometheus web UI. It depends on the "backend" service.
-  **grafana**: Uses the "grafana/grafana" image. It exposes port 3000 for accessing the Grafana web UI. It depends on the "prometheus" service.

## Configuration
The Prometheus configuration file (prometheus.yml) contains global settings and scrape configurations. Below is an explanation of a part of the configuration:


Global Settings:

scrape_interval: Specifies the global interval at which Prometheus scrapes targets for metrics (15 seconds in this case).
external_labels: Defines external labels that are applied to all scraped metrics. In this example, a label monitor is set to 'codelab-monitor.'
Scrape Configurations:

scrape_configs: Describes the list of targets and their configurations.
job_name: Identifies the job being scraped, in this case, 'fastapi.'
scrape_interval: Overrides the global scrape interval for this specific job (5 seconds in this case).
static_configs: Specifies static target configurations.
targets: Lists the targets to scrape. In this example, it targets the host host.docker.internal on port 8000.
To use this Docker Compose setup:

Ensure Docker and Docker Compose are installed.
Create a Docker network (if not already created): docker network create prom-net
Navigate to the directory containing the docker-compose.yml file.
Run docker-compose up -d to start the services in detached mode.
Access the following services:


Prometheus UI: http://localhost:9090
Grafana UI: http://localhost:3000 (default credentials: admin/admin)
Ensure that your application exposes relevant metrics for Prometheus to scrape and adjust the configuration as needed.





