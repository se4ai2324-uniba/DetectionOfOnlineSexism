"""
Module: train_a
Description: This module contains functions for testing model b.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
Date: 2023-11-03
"""

from pandas import read_csv
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
from validation_b import pipe_category,evaluation_metrics

dfs = read_csv('../../data/Raw/test_category.csv')

x1_test = dfs['text']
y1_test= dfs['label_category']
dfs.set_index('ID')
signature = infer_signature(x1_test, y1_test)

print("TEST: \n", y1_test.value_counts(), end="\n\n")

#evaluation metrics for the test data
precision, recall, f1 = evaluation_metrics(x1_test, y1_test, pipe_category)

mlflow.log_metric("precision_test", precision)
mlflow.log_metric("recall_test", recall)
mlflow.log_metric("f1_test", f1)

mlflow.sklearn.log_model(
        sk_model=pipe_category,
        artifact_path="svm-model-category",
        signature=signature,
        registered_model_name="sklearn-svm-model-category",
    )
mlflow.end_run()
