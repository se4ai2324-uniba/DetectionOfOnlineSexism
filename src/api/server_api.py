from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sys
import os

sys.path.append(os.getcwd()+"/DetectionOfOnlineSexism")
from src.api.corpus_endpoint import main_description, task, task_A, metrics_A, preprocessing_A, task_B, metrics_B, preprocessing_B, predict_sexism, predict_category
from pydantic import BaseModel

class Message(BaseModel):
    message: str

app = FastAPI(
    title="DetectionOfOnlineSexism") 

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
def task_AB(task_name: str):   
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
    This endpoint provides information on metrics associated with task A or B based on the task_name parameter.

    **Query Parameters:** 
    task_name is the name of the task (A or B).

    **Response:**
    Returns information about the metrics of the specified task or raises a 404 error if the task is not found.

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
    This endpoint provides information on preprocessing associated with task A or B based on the task_name parameter.

    **Query Parameters:** 
    task_name is the name of the task (A or B).

    **Response:** 
    Returns information about the preprocessing of the specified task or raises a 404 error if the task is not found.

    """
    if task_name == "A":
        return preprocessing_A
    elif task_name == "B":
        return preprocessing_B
    else:
        raise HTTPException(status_code=404, detail="Task not found")
    
if __name__ == '__main__':
   uvicorn.run(app, host='127.0.0.1', port=8000)