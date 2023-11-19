from fastapi import FastAPI, HTTPException,Form
from typing import Annotated
import uvicorn
from corpus_endpoint import main_description, task, task_A, metrics_A, preprocessing_A, task_B, metrics_B, preprocessing_B, predict_sexism, predict_category

app = FastAPI() 

@app.get("/") 
def main():   
    return main_description

@app.get("/task") 
def task():   
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
def prediction_sexism(message: Annotated[str, Form()]):
    return predict_sexism(message)

@app.post("/prediction_category")
def prediction_category(message: Annotated[str, Form()]):
    return predict_category(message)

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