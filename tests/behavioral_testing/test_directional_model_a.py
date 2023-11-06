import pytest
import sys
import os

current_directory = os.getcwd()
sys.path.append(current_directory+'\\..\\..\\src\\models') 

from validation_A import pipe_sexism
from pandas import read_csv

 
class TestInvarianceSexismClassifier:

    def test_directional(self):
        
        tokens = ["fat","bitch"]
        messages = [f"Hey {token} girls need love too, bub" 
                   for token in tokens]
        
        predicted_label = []

        for message in messages:
            predicted_label.append(pipe_sexism.predict([message])[0])
            
        assert predicted_label[0] != predicted_label[1]
    
