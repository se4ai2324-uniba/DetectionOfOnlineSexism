from fastapi import FastAPI 
import uvicorn

app = FastAPI() 

@app.get("/") 
def root():   
    return corpus

corpus={"Title": "Detection of Online Sexism",
            "Description": "An NLP model used to detect sexist messages and the type of sexism.",
            "Version": "1.0",
            "Available endpoints": []  }

if __name__ == '__main__':
   uvicorn.run(app, host='127.0.0.1', port=8000)