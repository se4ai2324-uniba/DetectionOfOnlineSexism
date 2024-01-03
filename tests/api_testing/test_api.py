"""
Module: test_api
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
Date: 2023-11-03
"""
#pylint: disable=wrong-import-position
import sys
import os
import pytest
from fastapi.testclient import TestClient
sys.path.append(os.getcwd()+"/DetectionOfOnlineSexism")

from src.api.server_api import app
from src.api.corpus_endpoint import main_description, task
from src.api.corpus_endpoint import task_A, preprocessing_A
from src.api.corpus_endpoint import task_B, preprocessing_B


client = TestClient(app)

def test_main_endpoint():
    """
    Function: test_main_endpoint.
    This function is used for testing the main endpoint.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == main_description

def test_task_endpoint():
    """
    Function: test_task_endpoint.
    This function is used for testing the task endpoint.
    """
    response = client.get("/task")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == task

def test_task_a_endpoint():
    """
    Function: test_task_A_endpoint.
    This function is used for testing the endpoint of the task A.
    """
    response = client.get("/task/A")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == task_A

def test_task_b_endpoint():
    """
    Function: test_task_B_endpoint.
    This function is used for testing the endpoint of the task B.
    """
    response = client.get("/task/B")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == task_B

def test_task_not_found_endpoint():
    """
    Function: test_task_not_found_endpoint.
    This function is used for testing if a task is not found.
    """
    response = client.get("/task/C")
    assert response.status_code == 404
    assert "Task not found" in response.text

def test_metrics_a_endpoint():
    """
    Function: test_metrics_A_endpoint.
    This function is used for testing the endpoint of the metrics of the task A.
    """
    response = client.get("/task/A/metrics")

    assert response.status_code == 200
    assert response.request.method == 'GET'

    expected_keys = ["title", "model", "f1", "recall", "precision"]
    for key in expected_keys:
        assert key in response.json()

def test_metrics_b_endpoint():
    """
    Function: test_metrics_B_endpoint.
    This function is used for testing the endpoint of the metrics of the task B.
    """
    response = client.get("/task/B/metrics")

    assert response.status_code == 200
    assert response.request.method == 'GET'

    expected_keys = ["title", "model", "f1", "recall", "precision"]
    for key in expected_keys:
        assert key in response.json()

def test_preprocessing_a_endpoint():
    """
    Function: test_preprocessing_A_endpoint.
    This function is used for testing the endpoint for the preprocessing of the task A.
    """
    response = client.get("/task/A/preprocessing")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == preprocessing_A

def test_preprocessing_b_endpoint():
    """
    Function: test_preprocessing_B_endpoint.
    This function is used for testing the endpoint for the preprocessing of the task B.
    """
    response = client.get("/task/B/preprocessing")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == preprocessing_B

@pytest.fixture
def message_sexism():
    """
    Function: message_sexism.
    This function is used for giving a sample of a sexist message for the task A.
    """
    return {"message": "When a girl gives you shit test, scare the shit out of her."}

def test_prediction_sexism_endpoint(message):
    """
    Function: test_prediction_sexism_endpoint.
    This function is used for testing the endpoint for the prediction of sexist messages.
    """
    response = client.post("/prediction_sexism", data=message)

    assert response.status_code == 200
    assert response.request.method == 'POST'
    assert "prediction" in response.json()

@pytest.fixture
def message_category():
    """
    Function: message_category.
    This function is used for giving a sample of a sexist message for the task B.
    """

    return {"message": "Fuck Claire McCaskill, she is a super twat." +
            "I am voting against her, and everyone else in Missouri should too."}

def test_prediction_category_endpoint(message):
    """
    Function: test_prediction_sexism_endpoint.
    This function is used for testing the endpoint
    for the prediction of the categoy of sexism of a message.
    """
    response = client.post("/prediction_category", data=message)

    assert response.status_code == 200
    assert response.request.method == 'POST'
    assert "prediction" in response.json()
