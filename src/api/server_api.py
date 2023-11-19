from fastapi import FastAPI, HTTPException
import uvicorn
from src.api.corpus_endpoint import main_description, task, task_A, metrics_A, preprocessing_A, task_B, metrics_B, preprocessing_B

app = FastAPI() 

@app.get("/") 
def main():   
    return main_description

@app.get("/task") 
def get_task():   
    return task

@app.get("/task/{task_name}") 
def task_AB(task_name:str):
    if task_name=="A":
        return task_A
    if task_name=="B":
        return task_B
    else:
        raise HTTPException(status_code=404, detail="Task not found")

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