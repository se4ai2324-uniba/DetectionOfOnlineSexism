import pytest
import os, sys
import pickle
from pandas import read_csv
sys.path.append(os.getcwd()+"/src/models/")
import train_a
from validation_a import evaluation_metrics

os.chdir(os.getcwd() + '/../../models/')
with open(os.getcwd() + '/validation_a.pkl', 'rb') as file:
    pipe_sexism = pickle.load(file)

VALUE = 0.70

def test_non_sexist_message():
    message = "Then, she's a keeper"
    predicted_label = pipe_sexism.predict([message])[0]
    assert predicted_label == "not sexist", f"The message has been categorized as not sexist."

def test_sexist_message():

    message = "I did. You have to have the bravery to escalate, touch her boobs etc, and work on escalating it further"
    predicted_label = pipe_sexism.predict([message])[0]
    assert predicted_label == "sexist", f"The message has been categorized as sexist."

def test_empty_message():
    message = ""
    predicted_label = pipe_sexism.predict([message])[0]
    assert predicted_label == "not sexist"  # Sostituisci con il comportamento desiderato

def test_evaluation_metrics():
    dfs = read_csv('../data/Raw/test_sexist.csv')

    x_test = dfs['text']
    y_test= dfs['label_sexist']
    dfs.set_index('ID')

    precision, recall, f1 = evaluation_metrics(x_test, y_test, pipe_sexism)

    assert precision > VALUE
    assert recall > VALUE
    assert f1 > VALUE

if __name__ == "__main__":
    pytest.main()