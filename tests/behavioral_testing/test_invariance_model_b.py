import pytest
import sys
import os

current_directory = os.getcwd()
sys.path.append(current_directory+'\\..\\..\\src\\models') 

from validation_B import pipe_category
from pandas import read_csv

 
class TestInvarianceSexismClassifier:

    def test_invariance_category(self):
        # Test per un messaggio non sessista
        tokens = ["get","obtain"]
        messages = [f"I didn't actually {token} a day without women, and I'm a little disappointed." 
                   for token in tokens]
        for message in messages:
            predicted_label = pipe_category.predict([message])[0]
            assert predicted_label == "2. derogation"
