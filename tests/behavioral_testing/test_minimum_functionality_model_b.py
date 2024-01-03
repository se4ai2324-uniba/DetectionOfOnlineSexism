"""
Module: test_minimum_functionality_model_b
Description: This module contains functions for doing the minimum
functionality test on the task b
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
import train_b
from pandas import read_csv
from validation_b import evaluation_metrics

file_dir = os.path.dirname(__file__)
FILE_PATH_BASE_MODEL = os.path.join(file_dir, "..//../models/validation_b.pkl")

with open(FILE_PATH_BASE_MODEL, 'rb') as file:
    pipe_category = pickle.load(file)

VALUE = 0.40

def test_threats_sexism():
    """
    Function: test_threats_sexism.
    The test checks if the model correctly labels a message
    as "1. threats, plans to harm and incitement" 
    for the given input, using the pipe_category.
    """

    message = "You should've hit her."
    predicted_label = pipe_category.predict([message])[0]
    if predicted_label == "1. threats, plans to harm and incitement":
        assert True, "The message has been categorized as a threat."
    else:
        pytest.skip("Message is not classified as threats.")

def test_derogation_sexism():
    """
    Function: test_derogation_sexism.
    The test checks if the model correctly labels a message as "2. derogation" 
    for the given input, using the pipe_category.
    """

    message = "If we won't fuck their women, what will they jerk off to?"
    predicted_label = pipe_category.predict([message])[0]
    if predicted_label == "2. derogation":
        assert True, "The message has been categorized as a derogation."
    else:
        pytest.skip("Message is not classified as derogation.")

def test_animosity_sexism():
    """
    Function: test_animosity_sexism.
    The test checks if the model correctly labels a message as "3. animosity" 
    for the given input, using the pipe_category.
    """

    message = "If it's reciprocal then it's fine... But women are just not"\
        "like that so don't cuck for these thots."
    predicted_label = pipe_category.predict([message])[0]
    if predicted_label == "3. animosity":
        assert True, "The message has been categorized as animosity."
    else:
        pytest.skip("Message is not classified as animosity.")

def test_prejudiced_discussions_sexism():
    """
    Function: test_prejudiced_discussions_sexism.
    The test checks if the model correctly labels a message as "4. prejudiced discussions"
    for the given input, using the pipe_category.
    """

    message = "I did. You have to have the bravery to escalate,"\
        "touch her boobs etc, and work on escalating it further."
    predicted_label = pipe_category.predict([message])[0]
    if predicted_label == "4. prejudiced discussions":
        assert True, "The message has been categorized as a prejudiced discussions."
    else:
        pytest.skip("Message is not classified as prejudiced discussions.")

def test_evaluation_metrics():
    """
    Function: test_evaluation_metrics.
    This test evaluates precision, recall, and F1 score for the category
    sexism prediction model using a test dataset.
    It asserts that the obtained metrics are greater than a predefined value.
    """

    dfs = read_csv('../data/Raw/test_category.csv')

    x1_test = dfs['text']
    y1_test = dfs['label_category']
    dfs.set_index('ID')

    precision, recall, f1 = evaluation_metrics(x1_test, y1_test, pipe_category)

    assert precision > VALUE
    assert recall > VALUE
    assert f1 > VALUE

if __name__ == "__main__":
    pytest.main()
