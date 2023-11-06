import pytest
import sys
import os

current_directory = os.getcwd()
sys.path.append(current_directory+'\\..\\..\\src\\models') 

from validation_B import pipe_category
from pandas import read_csv

 
class TestInvarianceSexismClassifier:

    def test_directional(self):
            
            tokens = ["are","buy"]
            messages = [f"Technically, the women {token} also cat food." 
                    for token in tokens]
            
            predicted_label = []

            for message in messages:
                predicted_label.append(pipe_category.predict([message])[0])
                
            assert predicted_label[0] != predicted_label[1]