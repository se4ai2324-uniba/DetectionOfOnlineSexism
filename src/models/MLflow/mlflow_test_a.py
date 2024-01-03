"""
Module: test_a
Description: This module contains functions for testing model a.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
import os
from pandas import read_csv
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
from validation_a import pipe_sexism,evaluation_metrics

file_dir = os.path.dirname(__file__)

PATH = os.path.join(file_dir, '..//../data/Raw/test_sexist.csv')

dfs = read_csv(PATH)

x_test = dfs['text']
y_test= dfs['label_sexist']
dfs.set_index('ID')
signature = infer_signature(x_test, y_test)
print("TEST: \n", y_test.value_counts(), end="\n\n")

#evaluation metrics for the test data
precision, recall, f1 = evaluation_metrics(x_test, y_test, pipe_sexism)

mlflow.log_metric("precision_test", precision)
mlflow.log_metric("recall_test", recall)
mlflow.log_metric("f1_test", f1)

mlflow.sklearn.log_model(
        sk_model=pipe_sexism,
        artifact_path="svm-model",
        signature=signature,
        registered_model_name="sklearn-svm-model",
    )

mlflow.end_run()
