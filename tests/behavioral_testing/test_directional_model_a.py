import pytest
import sys
import os
from src.models.validation_a import pipe_sexism
 
def test_directional():
    
    tokens = ["fat","bitch"]
    messages = [f"Hey {token} girls need love too, bub" 
                for token in tokens]
    
    predicted_label = []

    for message in messages:
        predicted_label.append(pipe_sexism.predict([message])[0])
        
    assert predicted_label[0] != predicted_label[1]
    
if __name__ == "__main__":
    pytest.main()