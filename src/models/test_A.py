"""
Module: test_a
Description: This module contains functions for testing model a.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
Date: 2023-11-03
"""

from pandas import read_csv
from src.models.validation_a import pipe_sexism,evaluation_metrics

dfs = read_csv('../../data/Raw/test_sexist.csv')

x_test = dfs['text']
y_test= dfs['label_sexist']
dfs.set_index('ID')

print("TEST: \n", y_test.value_counts(), end="\n\n")

#evaluation metrics for the test data
precision, recall, f1 = evaluation_metrics(x_test, y_test, pipe_sexism)
