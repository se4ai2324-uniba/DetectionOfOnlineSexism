import dagshub
import mlflow

dagshub.init("DetectionOfOnlineSexism", "graziaperna", mlflow=True)
mlflow.start_run()

# train your model...

mlflow.log_param("parameter name ", "value")
mlflow.log_metric("metric name", 1)

mlflow.end_run()