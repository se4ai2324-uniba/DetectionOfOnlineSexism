# Source Code Documentation

## Introduction

The `src` directory of our project includes two main components: the API and the feature-related code. The API is built using FastAPI, a high-performance web framework for building APIs with Python 3.7+. It's designed for automatic data validation and documentation generation, leveraging standard Python type hints. This section also covers the use of Docker Compose to launch a monitoring infrastructure with Prometheus and Grafana, along with a custom backend and frontend.

## API with FastAPI

The API is built using [FastAPI](https://fastapi.tiangolo.com/), a modern, high-performance web framework for building APIs with Python 3.7+. FastAPI leverages standard Python type hints for automatic data validation and documentation generation.

#### System Functionalities

This project has several endpoints with different tasks:

1. **`/task` Endpoint:** This endpoint is the main entry point for model activities. Through this, users can access general information about available tasks and the current version of the model.

2. **`/task/A` \ `/task/B` Endpoint:** This endpoint is useful to see in detail all the relevant information regarding the choosen task (A or B), in particular:
   -  the description of the task
   -  the models used for this task
   -  the path of the metrics related to the task

3. **`/task/A/metrics` \ `/task/B/metrics` Endpoint:** This endpoint provides evaluation metrics associated with the task choosen. Metrics include F1-score, recall and precision, offering an assessment of the model's performance.

4. **`/task/A/preprocessing` \ `/task/B/preprocessing` Endpoint:** This endpoint regards the preprocessing steps associated with the specified task specified, in fact it includes information about the tokenizer, the type of vectorizer and whether a lemmatizer was applied.

5. **`/prediction_sexism` Endpoint:** This endpoint is designed to predict whether a given message is sexist or not using a pre-trained model. The function takes a message as input and uses the model to predict the label, 

6. **`/prediction_category` Endpoint:** This endpoint has the same aim of the `/prediction_sexism` endpoint but in this case the prediction regards the category of sexism of the message taken in input. 

It uses HTTP GET requests for retrieving information through the first four endpoints, meanwhile the last two endpoints are set up to handle HTTP POST requests.

#### Running the API

To start the FastAPI server:

```bash
uvicorn main:app --reload
```
#### Swagger UI
It is possible to test the API  using Swagger UI, a user-friendly interface that simplifies the understanding of API functionalities. To access to the Swagger UI, navigate too: http://127.0.0.1:8000/docs

Here is showed the main window of the UI.

![SwaggerUI](../references/images_doc/SwaggerUI.png)

As we can see in the picture there are two endpoint used to make the prediction of a given message. 

Here there is an example of the `/prediction_sexism` endpoint.

![Sexism1](../references/images_doc/Sexism1.png)

In the response body is showned the message that has been inserted from the user and the prediction.

![Sexism2](../references/images_doc/Sexism2.png)

Instead here we have an example  of the `/prediction_category` endpoint. The user has to insert the message and then it will be displayed the result.

![Category1](../references/images_doc/Category1.png)

## Monitoring with Prometheus and Grafana
### Prometheus

[Prometheus](https://prometheus.io/) is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects metrics from configured targets at specified intervals, evaluates rule expressions, and can trigger alerts if conditions are met. Prometheus scrapes metrics from the "backend" service, as specified in the configuration file. The collected metrics are stored locally in a time-series database. Prometheus provides a query language (PromQL) for querying and processing the collected metrics.

In order to acquire the metrics, fastAPI and Prometheus have been connected using the `docker-compose.yml` file.

#### Configuration
The Prometheus configuration file [prometheus.yml](../prometheus.yml) contains global settings and scrape configurations.
The provided `prometheus.yml` file configures Prometheus with the following settings:

Global Configurations:
- `scrape_interval`: Metrics are collected globally every 15 seconds.
- `external_labels`: All collected metrics are labeled with 'monitor: codelab-monitor'.

Job-specific Configuration:
- Job Name: 'fastapi-it'
  - `scrape_interval`: Metrics for this job are collected every 5 seconds.
  - Target Configuration:
    - Target: 'backend:8000' - Prometheus collects metrics from a service named 'backend' on port 8000.

![Prometheus_configuration](../references/images_doc/prometheus_configuration.png)

#### How to execute docker-compose.yml

1. Ensure Docker is installed.
2. Navigate to the directory containing the docker-compose.yml file.
3. Run `docker-compose up` to start the services in detached mode.
4. Now you can access the following services:

   -  **Prometheus UI**: http://localhost:9090
   -  **Grafana UI**: http://localhost:3000 (default credentials: admin/admin)

### Grafana
Grafana is an open-source analytics and observability platform that allows users to visualize and monitor data from various sources in real-time. In the context of this setup, Grafana is integrated with Prometheus to create interactive dashboards for monitoring a FastAPI application.

#### Configuration
We have created 3 dashboards to organize in a better way the relevant metrics:
- Python Garbage Collection Metrics
- Scrape Metrics
- Sexism prediction Metrics

The main elements of these configurations are:

-  **Panel ID (id)**: A unique identifier for the panel.
-  **Panel Size (gridPos)**: Specifies the dimensions and position of the panel on the dashboard.
-  **Panel Options (options)**: Contains settings specific to the panel's behavior, such as tooltip management and legend display.
-  **Field Configuration (fieldConfig)**: Defines default settings and customizations for the panel's data field.
-  **Datasource (datasource)**: Specifies the datasource type (in this case, Prometheus) and a unique identifier (uid).
-  **Targets** represent different Prometheus metrics or expressions that the panel will display.

The queries related to `Python Garbage Collection Metrics` are:
- **python_gc_collections_total**:
   - Represents the total number of garbage collections performed by the Python runtime.
- **python_gc_objects_collected_total**:
   - Displays the overall count of objects collected during garbage collection.
- **python_gc_objects_uncollectable_total**:
   - Indicates the total count of objects marked as uncollectable and not reclaimed by the garbage collector.

![graphana_python](../references/images_doc/graphana_python.png)`

The queries related to `Scrape Metrics` are:
- **scrape_duration_seconds**:
   - Measures the duration of Prometheus scraping operations.
- **scrape_samples_post_metric_relabeling**:
   - Represents the count of samples after metric relabeling during the scraping process.
- **scrape_samples_scraped**:
   - Indicates the count of samples successfully scraped by Prometheus.
- **scrape_series_added**:
   - Reflects the count of time series added during scraping.

![graphana_scrape](../references/images_doc/graphana_scrape.png)`

The queries related to `Sexism prediction Metrics` are:
- **fastapi_inprogress**:
   - Represents the number of in-progress requests in the FastAPI application.
- **fastapi_model_total_predictions_created**:
   - Displays the total count of predictions created by a machine learning model in the FastAPI application.
- **fastapi_model_total_predictions_total**:
   - Shows the overall total count of predictions made by the machine learning model in FastAPI.
- **fastapi_model_prediction_result_count**:
   - Indicates the count of results generated from the model predictions in FastAPI.
- **fastapi_model_prediction_response_size_count**:
   - Represents the count of response sizes resulting from the model predictions in FastAPI.
- **fastapi_model_prediction_latency_count**:
   - Measures the latency of message prediction, helping to assess the speed and responsiveness of the prediction process.
- **fastapi_model_prediction_request_size_count**:
   - Indicates the size of prediction requests, offering visibility into the volume of data processed during predictions.

Dashboards were saved as json file and have been uploaded in [dashboards](api/dashboards)`.

## Drift Detection with Alibi Detect

### Alibi Detect

Alibi Detect is an open-source Python library designed for outlier and adversarial instance detection, concept drift monitoring and machine learning model interpretability. It provides a collection of algorithms and tools to assess and enhance the trustworthiness of machine learning models in production.

Alibi Detect is often used to continuously monitor models in production, ensuring that they remain effective and reliable as the underlying data distribution evolves.

### Drift Detection

In [drift_detection.py](./features/drift_detection.py)`, we can find the entire implementation for the drift detection.

The initial step involves loading the training datasets for both the models (sexism model and category model). Subsequently, a synthetic dataset is generated using the Faker library.

![alibi_detect_fake_data](../references/images_doc/AlibiDetectFakeData.png)

Both the training datasets and the artificially generated dataset are subjected to a preprocessing step using the same methodology employed in the preprocessing for the tasks A and B (tokenizer and vectorizer).

![alibi_detect_preprocessing](../references/images_doc/AlibiDetectPreprocessing.png)

The following code snippet shows the application of the KSDrift algorithm, that is employed to assess the distributional drift between the training dataset and the new fake generated dataset.
After applying the KSDrift algorithm, the script proceeds to make predictions using the model on artificially generated fake data. This dual process provides insights into the model's robustness and performance under varying data distributions.

![alibi_detect_KSDrift](../references/images_doc/AlibiDetectKSD.png)

For tracking and recording drift detection results, we generated logs that contain valuable information about the drift detection process:

-   **Timestamp**: The current date and time when the log is created
-   **Model Name**: The name of the machine learning model being monitored (`Model Sexism` or `Model Category`)
-   **Drift Detected**: Indicates whether drift is detected
-   **p-value**: The p-value associated with the drift detection, providing a statistical measure of significance
-   **Distance**: The calculated distance representing the shift in the statistical distribution of features

![alibi_detect_log](../references/images_doc/AlibiDetectLog.png)

### Results

![model_sexism](../references/images_doc/sexism_drift.png)

![model_category](../references/images_doc/category_drift.png)

For both models, the detection of drift with that distance and p-value indicates a substantial difference between the features of the training dataset and those of the new data, suggesting that there might be a change in the underlying characteristics that could impact the model's performance.
