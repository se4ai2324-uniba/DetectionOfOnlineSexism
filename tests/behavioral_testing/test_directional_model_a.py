import pytest
import os, sys
import pickle
sys.path.append(os.getcwd()+"/src/models/")
import train_a

os.chdir(os.getcwd() + '/../../models/')
with open(os.getcwd() + '/validation_a.pkl', 'rb') as file:
    pipe_sexism = pickle.load(file)
 
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