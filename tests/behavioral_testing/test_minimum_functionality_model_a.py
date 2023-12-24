"""
Module: test_minimum_functionality_model_a
Description: This module contains functions for doing the minimum
functionality test on the task a
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
#pylint: disable=import-error
#pylint: disable=unused-import
#pylint: disable=wrong-import-position

import os
import sys
import pickle
import pytest
sys.path.append(os.getcwd()+"/src/models/")
import train_a
from pandas import read_csv
from validation_a import evaluation_metrics

os.chdir(os.getcwd() + '/../../models/')
with open(os.getcwd() + '/validation_a.pkl', 'rb') as file:
    pipe_sexism = pickle.load(file)

VALUE = 0.70

def test_non_sexist_message():
    """
    Function: test_non_sexist_message.
    The test checks if the model correctly labels a message as "not sexist" 
    for the given input, using the pipe_sexism.
    """
    message = "Then, she's a keeper"
    predicted_label = pipe_sexism.predict([message])[0]
    assert predicted_label == "not sexist","The message has been categorized as not sexist."

def test_sexist_message():
    """
    Function: test_sexist_message.
    The test checks if the model correctly labels a message as "sexist" 
    for the given input, using the pipe_sexism.
    """
    message = "I did. You have to have the bravery to escalate,"\
    "touch her boobs etc, and work on escalating it further"
    predicted_label = pipe_sexism.predict([message])[0]
    assert predicted_label == "sexist", "The message has been categorized as sexist."

def test_empty_message():
    """
    Function: test_empty_message.
    The test checks if the model correctly labels a message as "not sexist" 
    for the given input, using the pipe_sexism.
    """
    message = ""
    predicted_label = pipe_sexism.predict([message])[0]
    assert predicted_label == "not sexist"

def test_evaluation_metrics():
    """
    Function: test_evaluation_metrics.
    This test evaluates precision, recall, and F1 score for the sexism prediction
    model using a test dataset.
    It asserts that the obtained metrics are greater than a predefined value.
    """
    dfs = read_csv('../data/Raw/test_sexist.csv')

    x_test = dfs['text']
    y_test= dfs['label_sexist']
    dfs.set_index('ID')

    precision, recall, f1 = evaluation_metrics(x_test, y_test, pipe_sexism)

    assert precision > VALUE
    assert recall > VALUE
    assert f1 > VALUE

if __name__ == "__main__":
    pytest.main()
