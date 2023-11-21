import pytest
import os, sys
sys.path.append(os.getcwd()+"/DetectionOfOnlineSexism")
from src.models.validation_b import pipe_category

def test_directional():
        
        tokens = ["are","buy"]
        messages = [f"Technically, the women {token} also cat food." 
                for token in tokens]
        
        predicted_label = []

        for message in messages:
            predicted_label.append(pipe_category.predict([message])[0])
            
        assert predicted_label[0] != predicted_label[1]

if __name__ == "__main__":
    pytest.main()