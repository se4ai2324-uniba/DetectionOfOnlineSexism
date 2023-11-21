"""
Module: test_b
Description: This module contains functions for testing model b.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
Date: 2023-11-03
"""

from pandas import read_csv
import sys, os
sys.path.append(os.getcwd()+"/DetectionOfOnlineSexism")
from src.models.validation_b import pipe_category,evaluation_metrics

dfs = read_csv('../../data/Raw/test_category.csv')

x1_test = dfs['text']
y1_test= dfs['label_category']
dfs.set_index('ID')

print("TEST: \n", y1_test.value_counts(), end="\n\n")

#evaluation metrics for the test data
precision, recall, f1 = evaluation_metrics(x1_test, y1_test, pipe_category)
