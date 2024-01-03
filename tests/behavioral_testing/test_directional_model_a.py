"""
Module: test_directional_model_a
Description: This module contains functions for doing directional testing
on the task A
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
#pylint: disable=import-error
#pylint: disable=unused-import
#pylint: disable=wrong-import-position

import os
import sys
sys.path.append(os.getcwd()+"/src/models/")
import pickle
import train_a
import pytest



file_dir = os.path.dirname(__file__)
FILE_PATH_BASE_MODEL = os.path.join(file_dir, "..//../models/")

with open('/validation_a.pkl', 'rb') as file:
    pipe_sexism = pickle.load(file)

def test_directional():
    """
    Function: test_directional.
    This test, using predefined tokens, ensures the model differentiates 
    messages with "fat" and "bitch" expecting distinct predictions for category labels.
    """
    tokens = ["fat","bitch"]
    messages = [f"Hey {token} girls need love too, bub"
                for token in tokens]

    predicted_label = []

    for message in messages:
        predicted_label.append(pipe_sexism.predict([message])[0])

    assert predicted_label[0] != predicted_label[1]

if __name__ == "__main__":
    pytest.main()
