import pytest
import os, sys
sys.path.append(os.getcwd()+"DetectionOfOnlineSexism")
from src.models.validation_A import pipe_sexism

def test_non_sexist_message():
    tokens = ["want","wish"]
    messages = [f"Hell i {token} to marry her and im a straight female" 
                for token in tokens]
    for message in messages:
        predicted_label = pipe_sexism.predict([message])[0]
        assert predicted_label == "not sexist"

def test_sexist_message():
    tokens = ["send","give"]
    messages = [f"I'm not going to {token} you money just because you have a pussy. Entitled cunt." 
                for token in tokens]
    for message in messages:
        predicted_label = pipe_sexism.predict([message])[0]
        assert predicted_label == "sexist"
    
if __name__ == "__main__":
    pytest.main()