from fastapi import FastAPI 
import uvicorn
from src.api.corpus_endpoint import main_description, task, task_A, metrics_A, preprocessing_A, task_B, metrics_B, preprocessing_B

app = FastAPI() 

@app.get("/") 
def root():   
    return main_description

@app.get("/task") 
def root():   
    return task

@app.get("/task/A") 
def root():   
    return task_A

@app.get("/task/A/metrics") 
def root():   
    return metrics_A

@app.get("/task/A/preprocessing") 
def root():   
    return preprocessing_A

@app.get("/task/B") 
def root():   
    return task_B

@app.get("/task/B/metrics") 
def root():   
    return metrics_B

@app.get("/task/B/preprocessing") 
def root():   
    return preprocessing_B


if __name__ == '__main__':
   uvicorn.run(app, host='127.0.0.1', port=8000)