from fastapi import FastAPI 
from flask import Flask, jsonify, request
import uvicorn

app = FastAPI() 

@app.get("/") 
def root(): 
    return {
            "Title": "MalURLs"     
}


if __name__ == '__main__':
   uvicorn.run(app, host='127.0.0.1', port=8000)