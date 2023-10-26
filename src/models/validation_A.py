from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, recall_score, f1_score, make_scorer
from pandas import read_csv
from train_A import pipe_sexism, x_train, y_train, n_cpu
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
dfv = read_csv('../../data/Raw/dev_sexist.csv')
x_val = dfv['text']
y_val = dfv['label_sexist']
dfv.set_index('ID')
print("VALIDATION: \n", y_val.value_counts(), end="\n\n")


#evaluation metrics for the validation data
precision, recall, f1 = evaluation_metrics(x_val, y_val, pipe_sexism)

mlflow.log_metric("precision_val", precision)
mlflow.log_metric("recall_val", recall)
mlflow.log_metric("f1_val", f1)


# params = {'vectorizer__ngram_range': [(1,1),(1,2)],
#           'classifier__C': [0.2, 0.4, 1],
#           'classifier__class_weight': ['balanced', None]}
# 
# pipe_optimized = GridSearchCV(pipe_sexism,param_grid=params,cv=10,scoring=make_scorer(f1_score, average="macro"),n_jobs=n_cpu-1,refit=True)
# pipe_optimized.fit(x_train, y_train)
# print("Migliori iperparametri:",pipe_optimized.best_params_)
# 
# best_params = pipe_optimized.best_params_
# pipe_sexism.set_params(**best_params)

pipe_sexism.fit(x_train, y_train)

pickle.dump(pipe_sexism, open('../../models/validation_A.pkl', 'wb'))
