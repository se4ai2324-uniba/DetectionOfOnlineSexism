"""
Module: test_invariance_model_b
Description: This module contains functions for doing invariance testing
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
import pytest
sys.path.append(os.getcwd()+"/src/models/")
import train_b

file_dir = os.path.dirname(__file__)
FILE_PATH_BASE_MODEL = os.path.join(file_dir, "..//../models/")
with open('/validation_b.pkl', 'rb') as file:
    pipe_category = pickle.load(file)

def test_invariance_category():
    """
    Function: test_directional.
    The test checks if the model correctly categorizes messages 
    containing "get" or "obtain" as "2. derogation".
    """
    tokens = ["get","obtain"]
    messages = [f"I didn't actually {token} a day without women, and I'm a little disappointed."
                for token in tokens]
    for message in messages:
        predicted_label = pipe_category.predict([message])[0]
        assert predicted_label == "2. derogation"

if __name__ == "__main__":
    pytest.main()
