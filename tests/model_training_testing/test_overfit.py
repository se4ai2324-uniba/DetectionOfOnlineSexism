import pytest
import os, sys
sys.path.append(os.getcwd()+"DetectionOfOnlineSexism")
from src.models.train_A import Predictors, vector, classifier
from sklearn.pipeline import Pipeline
from pandas import read_csv
from sklearn.metrics import accuracy_score

@pytest.fixture
def setup_training():
    dft = read_csv('../../data/Raw/train_sexist.csv')
    x_train = dft['text']
    y_train = dft['label_sexist']
    dft.set_index('ID')
    
    # Create the pipeline
    pipe_sexism = Pipeline([("cleaner", Predictors()),
    ('vectorizer', vector),
    ('classifier', classifier)])

    return pipe_sexism, x_train, y_train

def compute_accuracy_on_batch(pipe, x_batch, y_batch):
    y_pred = pipe.predict(x_batch)
    accuracy = accuracy_score(y_batch, y_pred)
    return accuracy

def test_decreasing_loss(setup_training):
    pipe_sexism, x_train, y_train = setup_training

    accuracy = compute_accuracy_on_batch(pipe_sexism, x_train, y_train)
    assert accuracy == pytest.approx(0.95, abs=0.05)

if __name__ == "__main__":
    pytest.main()