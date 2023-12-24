"""
Module: test_overfit
Description: This module contains functions for doing
tests of overfitting
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
import pytest
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from pandas import read_csv
from src.models.train_a import Predictors, vector, classifier

@pytest.fixture
def setup_training():
    """
    Module: setup_training
    Description: This function sets up training data
    by reading a CSV file, extracting features (x_train)
    and labels (y_train). It then creates a pipeline (pipe_sexism)
    comprising a cleaner, vectorizer, and classifier.
    The pipeline is returned along with the training data.
    """
    dft = read_csv('../../data/Raw/train_sexist.csv')
    x_train = dft['text']
    y_train = dft['label_sexist']
    dft.set_index('ID')

    pipe_sexism = Pipeline([("cleaner", Predictors()),
    ('vectorizer', vector),
    ('classifier', classifier)])

    return pipe_sexism, x_train, y_train

def compute_accuracy_on_batch(pipe, x_batch, y_batch):
    """
    Module: compute_accuracy_on_batch
    Description: This function computes the accuracy of a given pipeline (pipe)
    on a batch of data (x_batch) with corresponding labels (y_batch).
    It uses the pipeline to predict labels and calculates the accuracy score by
    comparing predicted and actual labels. The computed accuracy is returned.
    """
    y_pred = pipe.predict(x_batch)
    accuracy = accuracy_score(y_batch, y_pred)
    return accuracy

def test_decreasing_loss(setup):
    """
    Module: test_decreasing_loss
    Description: This test, utilizing a training setup function,
    checks if the accuracy of the sexism prediction model on
    the training data is approximately 95%, allowing for a 5% margin of error.
    """
    pipe_sexism, x_train, y_train = setup

    accuracy = compute_accuracy_on_batch(pipe_sexism, x_train, y_train)
    assert accuracy == pytest.approx(0.95, abs=0.05)

if __name__ == "__main__":
    pytest.main()
