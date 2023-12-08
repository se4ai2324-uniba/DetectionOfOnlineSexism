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

app = FastAPI() 

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
    return main_description

@app.get("/task") 
def task_api():   
    return task

@app.get("/task/{task_name}") 
def task_AB(task_name:str):
    if task_name=="A":
        return task_A
    if task_name=="B":
        return task_B
    else:
        raise HTTPException(status_code=404, detail="Task not found")
    
@app.post("/prediction_sexism")
def prediction_sexism(data: Message):
    return predict_sexism(data.message)

@app.post("/prediction_category")
def prediction_category(data: Message):
    return predict_category(data.message)

@app.get("/task/{task_name}/metrics") 
def metrics(task_name:str):   
    if task_name=="A":
        return metrics_A
    if task_name=="B":
        return metrics_B
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.get("/task/{task_name}/preprocessing") 
def preprocessing(task_name:str):   
    if task_name=="A":
        return preprocessing_A
    if task_name=="B":
        return preprocessing_B
    else:
        raise HTTPException(status_code=404, detail="Task not found")

if __name__ == '__main__':
   uvicorn.run(app, host='127.0.0.1', port=8000)