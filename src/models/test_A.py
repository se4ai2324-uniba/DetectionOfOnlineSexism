"""
Module: test_a
Description: This module contains functions for testing model a.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
Date: 2023-11-03
"""

from pandas import read_csv
from validation_a import pipe_sexism,evaluation_metrics
from codecarbon import EmissionsTracker

# Inizializza l'oggetto EmissionsTracker
tracker = EmissionsTracker(project_name="test_a", output_file="output_test_a.json")

dfs = read_csv('../../data/Raw/test_sexist.csv')

x_test = dfs['text']
y_test= dfs['label_sexist']
dfs.set_index('ID')

with tracker:
    print("TEST: \n", y_test.value_counts(), end="\n\n")

    # Evaluation metrics for the test data
    precision, recall, f1 = evaluation_metrics(x_test, y_test, pipe_sexism)
