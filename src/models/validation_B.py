from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, recall_score, f1_score, make_scorer
from pandas import read_csv
from train_B import pipe_category, x1_train, y1_train, n_cpu
import mlflow
import pickle
import os

def evaluation_metrics(x, y, pipe):

    y_pred = pipe.predict(x)

    precision = precision_score(y, y_pred, average="macro")
    recall = recall_score(y, y_pred, average="macro")
    f1 = f1_score(y, y_pred, average="macro")

    print("Precision: {:.4f}".format(precision))
    print("Recall: {:.4f}".format(recall))
    print("F1 Score: {:.4f}".format(f1))

    return precision, recall, f1

#os.chdir(os.path.dirname(os.path.abspath(__file__)))
dfv = read_csv('../../data/Raw/dev_category.csv')
x1_val = dfv['text']
y1_val = dfv['label_category']
dfv.set_index('ID')
print("VALIDATION: \n", y1_val.value_counts(), end="\n\n")

#evaluation metrics for the validation data
precision, recall, f1 = evaluation_metrics(x1_val, y1_val, pipe_category)

mlflow.log_metric("precision_val", precision)
mlflow.log_metric("recall_val", recall)
mlflow.log_metric("f1_val", f1)

# params = {'vectorizer__ngram_range': [(1,1),(1,2)],
#           'classifier__C': [0.2, 0.4, 1],
#           'classifier__class_weight': ['balanced', None]}
# 
# pipe1_optimized = GridSearchCV(pipe_category,param_grid=params,cv=10,scoring=make_scorer(f1_score, average="macro"),n_jobs=n_cpu-1,refit=True)
# pipe1_optimized.fit(x1_train, y1_train)
# print("Migliori iperparametri:",pipe1_optimized.best_params_)
# 
# best_params = pipe1_optimized.best_params_
# pipe_category.set_params(**best_params)

pipe_category.fit(x1_train, y1_train)

pickle.dump(pipe_category, open('../../models/validation_B.pkl', 'wb'))
