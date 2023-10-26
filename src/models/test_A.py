from pandas import read_csv
from validation_A import pipe_sexism,evaluation_metrics
import mlflow
import os 

#os.chdir(os.path.dirname(os.path.abspath(__file__)))
dfs = read_csv('../../data/Raw/test_sexist.csv')

x_test = dfs['text']
y_test= dfs['label_sexist']
dfs.set_index('ID')
print("TEST: \n", y_test.value_counts(), end="\n\n")

#evaluation metrics for the test data
precision, recall, f1 = evaluation_metrics(x_test, y_test, pipe_sexism)

mlflow.log_metric("precision_test", precision)
mlflow.log_metric("recall_test", recall)
mlflow.log_metric("f1_test", f1)
mlflow.end_run()