import pytest
from src.api.server_api import app
from fastapi.testclient import TestClient
from src.api.corpus_endpoint import main_description, task, task_A, metrics_A, preprocessing_A, task_B, metrics_B, preprocessing_B

client = TestClient(app)

def test_main_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == main_description

def test_task_endpoint():
    response = client.get("/task")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    print(response.json())
    print("ciao")
    print(task)
    assert response.json() == task

def test_task_A_endpoint():
    response = client.get("/task/A")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == task_A

def test_task_B_endpoint():
    response = client.get("/task/B")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == task_B

def test_task_not_found_endpoint():
    response = client.get("/task/C")
    assert response.status_code == 404
    assert "Task not found" in response.text

def test_metrics_A_endpoint():
    response = client.get("/task/A/metrics")

    assert response.status_code == 200
    assert response.request.method == 'GET'

    expected_keys = ["title", "model", "f1", "recall", "precision"]
    for key in expected_keys:
        assert key in response.json()

def test_metrics_B_endpoint():
    response = client.get("/task/B/metrics")

    assert response.status_code == 200
    assert response.request.method == 'GET'

    expected_keys = ["title", "model", "f1", "recall", "precision"]
    for key in expected_keys:
        assert key in response.json()


def test_preprocessing_A_endpoint():
    response = client.get("/task/A/preprocessing")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == preprocessing_A

def test_preprocessing_B_endpoint():
    response = client.get("/task/B/preprocessing")
    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.json() == preprocessing_B