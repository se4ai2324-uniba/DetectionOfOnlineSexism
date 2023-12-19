"""
    Module: server_api
    Description: This module contains the api calls
    Authors: Francesco Brescia
            Maria Elena Zaza
            Grazia Perna
    Date: 2023-12-17
"""
#pylint: disable=wrong-import-position
#pylint: disable=no-else-return
import sys
import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
sys.path.append(os.getcwd()+"/DetectionOfOnlineSexism")
from src.api.corpus_endpoint import main_description, task, task_A, metrics_A, preprocessing_A
from src.api.corpus_endpoint import task_B, metrics_B, preprocessing_B
from src.api.corpus_endpoint import predict_sexism, predict_category
from src.api.monitoring import instrumentator

class Message(BaseModel):
    """
    Class: Message
    Description: This class contains:
    - message: str
    """
    message: str

app = FastAPI(
    title="DetectionOfOnlineSexism")

instrumentator.instrument(app).expose(app, include_in_schema=False, should_gzip=True)

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Elenco degli origini consentiti
    allow_credentials=True,
    allow_methods=["*"],  # Consenti tutti i metodi, inclusi POST e OPTIONS
    allow_headers=["*"],  # Consenti tutti gli headers
)

@app.get("/")
def main():
    """
    **Main Endpoint:**
    
    **Description:**
    This endpoint represents the main entry point for the application.

    """
    return main_description

@app.get("/task")
def task_api():
    """
    **Task API Endpoint:**
    
    **Description:** 
    This endpoint provides information about available tasks.

    **Query Parameters:** 
    No query parameters are required.

    **Response:** 
    Returns information about the two tasks available.

    """
    return task

@app.get("/task/{task_name}")
def task_a_b(task_name: str):
    """
    **Task A/B Endpoint:**
    
    **Description:** 
    This endpoint returns specific information about task A or B based on the task_name parameter.

    **Query Parameters:** 
    task_name is the name of the task (A or B).

    **Response:**
    Returns information about the specified task or raises a 404 error if the task is not found.

    """
    if task_name == "A":
        return task_A
    elif task_name == "B":
        return task_B
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/prediction_sexism")
def prediction_sexism(data: Message):
    """
    **Prediction Sexism Endpoint:**
    
    **Description:** 
    This endpoint accepts text data and returns a prediction on sexist content.

    **Request Body Parameters:**  
    Requires a JSON object with the 'message' field representing the text to analyze.
    
    **Response:** 
    Returns the prediction on the presence of sexist content.

    """
    return predict_sexism(data.message)

@app.post("/prediction_category")
def prediction_category(data: Message):
    """
    **Prediction Category Endpoint:**
    
    **Description:** 
    This endpoint accepts text data and returns the category of sexism.

    **Request Body Parameters:** 
    Requires a JSON object with the 'message' field representing the text to analyze.

    **Response:** 
    Returns the category of sexism.

    """
    return predict_category(data.message)

@app.get("/task/{task_name}/metrics")
def metrics(task_name: str):
    """
    **Task Metrics Endpoint:**
    
    **Description:** 
    This endpoint provides information on metrics associated
    with task A or B based on the task_name parameter.

    **Query Parameters:** 
    task_name is the name of the task (A or B).

    **Response:**
    Returns information about the metrics of the specified
    task or raises a 404 error if the task is not found.

    """
    if task_name == "A":
        return metrics_A
    elif task_name == "B":
        return metrics_B
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.get("/task/{task_name}/preprocessing")
def preprocessing(task_name: str):
    """
    **Task Preprocessing Endpoint:**
    
    **Description:** 
    This endpoint provides information on preprocessing
    associated with task A or B based on the task_name parameter.

    **Query Parameters:** 
    task_name is the name of the task (A or B).

    **Response:** 
    Returns information about the preprocessing of the specified
    task or raises a 404 error if the task is not found.

    """
    if task_name == "A":
        return preprocessing_A
    elif task_name == "B":
        return preprocessing_B
    else:
        raise HTTPException(status_code=404, detail="Task not found")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
