"""
Module: test_directional_model_b
Description: This module contains functions for doing directional testing
on the task B
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
sys.path.append(os.getcwd()+"/src/models/")
import train_b
import pytest


file_dir = os.path.dirname(__file__)
FILE_PATH_BASE_MODEL = os.path.join(file_dir, "..//../models/validation_b.pkl")

with open(FILE_PATH_BASE_MODEL, 'rb') as file:
     pipe_category = pickle.load(file)

def test_directional():
    """
    Function: test_directional.
    This test, using predefined tokens, ensures the model differentiates 
    messages with "are" and "buy" expecting distinct predictions for category labels.
    """

    tokens = ["are","buy"]
    messages = [f"Technically, the women {token} also cat food."
    for token in tokens]
    predicted_label = []

    for message in messages:
        predicted_label.append(pipe_category.predict([message])[0])

    assert predicted_label[0] != predicted_label[1]

if __name__ == "__main__":
    pytest.main()
