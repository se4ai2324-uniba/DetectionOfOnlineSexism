"""
Module: test_invariance_model_a
Description: This module contains functions for doing invariance testing
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
import pickle
import pytest
sys.path.append(os.getcwd()+"/src/models/")
import train_a

file_dir = os.path.dirname(__file__)
FILE_PATH_BASE_MODEL = os.path.join(file_dir, "..//../models/validation_a.pkl")

with open(FILE_PATH_BASE_MODEL, 'rb') as file:
    pipe_sexism = pickle.load(file)

def test_non_sexist_message():
    """
    Function: test_non_sexist_message.
    The test checks if the model correctly categorizes messages 
    containing "want" or "wish" as "not sexist".
    """
    tokens = ["want","wish"]
    messages = [f"Hell i {token} to marry her and im a straight female"
                for token in tokens]
    for message in messages:
        predicted_label = pipe_sexism.predict([message])[0]
        assert predicted_label == "not sexist"

def test_sexist_message():
    """
    Function: test_sexist_message.
    The test checks if the model correctly categorizes messages 
    containing "send" or "give" as "sexist".
    """
    tokens = ["send","give"]
    messages = [f"I'm not going to {token} you money just because you have a pussy. Entitled cunt."
                for token in tokens]
    for message in messages:
        predicted_label = pipe_sexism.predict([message])[0]
        assert predicted_label == "sexist"

if __name__ == "__main__":
    pytest.main()
