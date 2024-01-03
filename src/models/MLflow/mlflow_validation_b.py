"""
Module: validation_a
Description: This module contains functions for validating model b.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
Date: 2023-11-03
"""
import os
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, recall_score, f1_score, make_scorer
from pandas import read_csv
import mlflow
from train_b import pipe_category, x1_train, y1_train, n_cpu

def evaluation_metrics(x, y, pipe):
    """
    Calculate precision, recall, and F1 score for a classification model.

    Parameters:
        x (array-like): Input data for predictions.
        y (array-like): True labels.
        pipe (estimator): A scikit-learn estimator (e.g., a fitted pipeline).

    Returns:
        precision (float): The macro-averaged precision score.
        recall (float): The macro-averaged recall score.
        f1 (float): The macro-averaged F1 score.
    """
    y_pred = pipe.predict(x)

    precision_value = precision_score(y, y_pred, average="macro")
    recall_value = recall_score(y, y_pred, average="macro")
    f1_value = f1_score(y, y_pred, average="macro")

    print(f"Precision: {precision_value:.4f}")
    print(f"Recall: {recall_value:.4f}")
    print(f"F1 Score: {f1_value:.4f}")

    return precision_value, recall_value, f1_value

file_dir = os.path.dirname(__file__)
PATH = os.path.join(file_dir, '..//../data/Raw/dev_category.csv')
dfv = read_csv(PATH)

x1_val = dfv['text']
y1_val = dfv['label_category']
dfv.set_index('ID')
print("VALIDATION: \n", y1_val.value_counts(), end="\n\n")

#evaluation metrics for the validation data
precision, recall, f1 = evaluation_metrics(x1_val, y1_val, pipe_category)

mlflow.log_metric("precision_val", precision)
mlflow.log_metric("recall_val", recall)
mlflow.log_metric("f1_val", f1)

params = {'vectorizer__ngram_range': [(1,1),(1,2)],
          'classifier__C': [0.2, 0.4, 1],
          'classifier__class_weight': ['balanced', None]}

pipe1_optimized = GridSearchCV(pipe_category,param_grid=params,cv=10,
                               scoring=make_scorer(f1_score, average="macro"),
                               n_jobs=n_cpu-1,refit=True)
pipe1_optimized.fit(x1_train, y1_train)
print("Migliori iperparametri:",pipe1_optimized.best_params_)
best_params = pipe1_optimized.best_params_
pipe_category.set_params(**best_params)
pipe_category.fit(x1_train, y1_train)

with open('../../models/validation_B.pkl', 'wb') as file_validation_b:
    pickle.dump(pipe_category, file_validation_b)
