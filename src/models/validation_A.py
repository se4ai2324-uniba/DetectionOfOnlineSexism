"""
Module: validation_a
Description: This module contains functions for validating model a.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
Date: 2023-11-03
"""

import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, recall_score, f1_score, make_scorer
from pandas import read_csv
import sys
sys.path.append('C:/Users/Utente/Desktop/Progetto Software Engineering/DetectionOfOnlineSexism')
from src.models.train_a import pipe_sexism, x_train, y_train, n_cpu

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

dfv = read_csv('../../data/Raw/dev_sexist.csv')
x_val = dfv['text']
y_val = dfv['label_sexist']
dfv.set_index('ID')
print("VALIDATION: \n", y_val.value_counts(), end="\n\n")

#evaluation metrics for the validation data
precision, recall, f1 = evaluation_metrics(x_val, y_val, pipe_sexism)

params = {'vectorizer__ngram_range': [(1,1),(1,2)],
          'classifier__C': [0.2, 0.4, 1],
          'classifier__class_weight': ['balanced', None]}
pipe_optimized = GridSearchCV(pipe_sexism,param_grid=params,cv=10,
                              scoring=make_scorer(f1_score, average="macro"),
                              n_jobs=n_cpu-1,refit=True)
pipe_optimized.fit(x_train, y_train)
print("Migliori iperparametri:",pipe_optimized.best_params_)
best_params = pipe_optimized.best_params_
pipe_sexism.set_params(**best_params)

pipe_sexism.fit(x_train, y_train)

with open('../../models/validation_A.pkl', 'wb') as file_validation_a:
    pickle.dump(pipe_sexism, file_validation_a)
