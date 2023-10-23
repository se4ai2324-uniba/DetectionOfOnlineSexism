from pandas import read_csv
from validation_B import pipe_category,evaluation_metrics
import mlflow
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
dfs = read_csv('../../data/Raw/test_category.csv')

x1_test = dfs['text']
y1_test= dfs['label_category']
dfs.set_index('ID')
print("TEST: \n", y1_test.value_counts(), end="\n\n")

#evaluation metrics for the test data
accuracy, precision, recall, f1 = evaluation_metrics(x1_test, y1_test, pipe_category)
mlflow.start_run()
mlflow.log_metric("accuracy_B", accuracy)
mlflow.log_metric("precision_B", precision)
mlflow.log_metric("recall_B", recall)
mlflow.log_metric("f1_B", f1)
mlflow.end_run() 