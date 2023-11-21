import pytest
import os, sys
import pickle
sys.path.append(os.getcwd()+"/src/models/")
import train_b

os.chdir(os.getcwd() + '/../../models/')
with open(os.getcwd() + '/validation_b.pkl', 'rb') as file:
    pipe_category = pickle.load(file)

def test_invariance_category():
    tokens = ["get","obtain"]
    messages = [f"I didn't actually {token} a day without women, and I'm a little disappointed." 
                for token in tokens]
    for message in messages:
        predicted_label = pipe_category.predict([message])[0]
        assert predicted_label == "2. derogation"

if __name__ == "__main__":
    pytest.main()