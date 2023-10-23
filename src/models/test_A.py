from pandas import read_csv
from validation_A import pipe_optimized,evaluation_metrics
import mlflow
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))
dfs = read_csv('../../data/Raw/test_sexist.csv')



x_test = dfs['text']
y_test= dfs['label_sexist']
dfs.set_index('ID')
print("TEST: \n", y_test.value_counts(), end="\n\n")

#evaluation metrics for the test data
accuracy, precision, recall, f1 = evaluation_metrics(x_test, y_test, pipe_optimized)
mlflow.start_run()
mlflow.log_metric("accuracy_test_A", accuracy)
mlflow.log_metric("precision_test_A", precision)
mlflow.log_metric("recall_test_A", recall)
mlflow.log_metric("f1_test_A", f1)
mlflow.end_run()