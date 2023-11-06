import pytest
import sys
import os

current_directory = os.getcwd()
sys.path.append(current_directory+'\\..\\..\\src\\models') 

from validation_A import pipe_sexism
from pandas import read_csv

 
class TestInvarianceSexismClassifier:

    def test_non_sexist_message(self):
        # Test per un messaggio non sessista
        tokens = ["want","wish"]
        messages = [f"Hell i {token} to marry her and im a straight female" 
                   for token in tokens]
        for message in messages:
            predicted_label = pipe_sexism.predict([message])[0]
            assert predicted_label == "not sexist"

    def test_sexist_message(self):
        # Test per un messaggio non sessista
        tokens = ["send","give"]
        messages = [f"I'm not going to {token} you money just because you have a pussy. Entitled cunt." 
                   for token in tokens]
        for message in messages:
            predicted_label = pipe_sexism.predict([message])[0]
            assert predicted_label == "sexist"
    
