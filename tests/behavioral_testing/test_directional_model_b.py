import pytest
import os, sys
import pickle
sys.path.append(os.getcwd()+"/src/models/")
import train_b

os.chdir(os.getcwd() + '/../../models/')
with open(os.getcwd() + '/validation_b.pkl', 'rb') as file:
    pipe_category = pickle.load(file)

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