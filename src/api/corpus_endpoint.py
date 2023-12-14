"""
Module: corpus_endpoint
Description: This module contains the functions and dictionaries 
            for the api calls and their validation using Pydantic.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
Date: 2023-12-14
"""
from pydantic import BaseModel, ValidationError
from typing import List, Optional
import pickle
import os
import sys

sys.path.append(os.getcwd()+"/src/models/")
import train_a
import train_b

# Percorso alla cartella genitore della cartella corrente
parent_directory = os.path.dirname(os.path.dirname(os.getcwd()))

# Percorso alla cartella 'models' che si trova al livello superiore rispetto a 'src'
models_path = os.path.join(parent_directory, 'models')

# Aggiungi il percorso alla cartella 'models' al sys.path
sys.path.append(models_path)

# Carica il file validation_a.pkl
sexism_model_path = os.path.join(models_path, 'validation_a.pkl')
with open(sexism_model_path, 'rb') as file:
    sexism_model = pickle.load(file)

# Carica il file validation_b.pkl
category_model_path = os.path.join(models_path, 'validation_b.pkl')
with open(category_model_path, 'rb') as file:
    category_model = pickle.load(file)


class PredictionModel(BaseModel):
    prediction: str

class MainDescriptionModel(BaseModel):
    title: str
    description: str
    version: str
    available_endpoints: List[str]

class TaskModel(BaseModel):
    title: str
    description: str
    pipeline: str
    more_information: List[str]

class SubTaskModel(BaseModel):
    title: str
    description: str
    model: List[str]
    metrics: str

class MetricsModel(BaseModel):
    title: str
    model: str
    f1: float
    recall: float
    precision: float

class PreprocessingModel(BaseModel):
    title: str
    tokenizer: str
    vectorizer: str
    lemmatizer: Optional[str] = None

models = ["LinearSVC classifier", "Random Forest"]

main_description = {
    "title": "Detection of Online Sexism",
    "description": "An NLP model used to detect sexist messages and the type of sexism.",
    "version": "1.0",
    "available_endpoints": ["/task", "/task/A", 
                            "/task/A/metrics", 
                            "/task/A/preprocessing", 
                            "/task/B", 
                            "/task/B/metrics", 
                            "/task/B/preprocessing"]
}

task = {
    "title": "Tasks",
    "description": "The models have two hierarchical tasks: TASK A and TASK B",
    "pipeline": "- Preprocessing - Training - Validation - Test",
    "more_information": ["/task/A", "/task/B"]
}

task_A = {
    "title": "Task A",
    "description": "Sexism Detection: for detecting whether a post is sexist",
    "model": models,
    "metrics": "/task/A/metrics"
}

metrics_A = {
    "title": "Metrics Task A",
    "model": "Linear SVC",
    "f1": 0.7637,
    "recall": 0.7444,
    "precision": 0.7947
}

preprocessing_A = {
    "title": "Preprocessing Task A",
    "tokenizer": "TreeBankWord",
    "vectorizer": "CountVectorizer",
    "lemmatizer": "Yes",
}

task_B = {
    "title": "Task B",
    "description": "Category of Sexism: for assigning to each of the sexist texts a category " +
                    "(threats, derogation, animosity, prejudiced discussions",
    "model": models,
    "metrics": "/task/B/metrics"
}

metrics_B = {
    "title": "Metrics Task B",
    "model": "Linear SVC",
    "f1": 0.4597,
    "recall": 0.4438,
    "precision": 0.4932
}

preprocessing_B = {
    "title": "Preprocessing Task B",
    "tokenizer": "TreeBankWord",
    "vectorizer": "CountVectorizer",
    "lemmatizer": "No",
}


message_prediction= {
    "message": "null",
    "prediction": "not_sexist"
}

#example of validation error
try:
    #in this case "MoreInformation" should be a list
    invalid_task_data = {
        "title": "Invalid Task",
        "description": "Invalid Description",
        "pipeline": "Invalid Pipeline",
        "more_information": "Invalid Information"  
    }

    invalid_task_model = TaskModel(**invalid_task_data)
except ValidationError as e:
    print(e.json())


def changeMessagePrediction(message, prediction):
    message_prediction["message"] = message
    message_prediction["prediction"] = prediction

def predict_sexism(message):
    global messageToPrint
    messageToPrint = message
    predicted_label = sexism_model.predict([message])[0]
    if predicted_label == "not sexist":
        changeMessagePrediction(message, "not_sexist")
        return  message_prediction
    else:
        changeMessagePrediction(message, "sexist")
        return  message_prediction

def predict_category(message):

    predicted_label = category_model.predict([message])[0]
    if predicted_label == "1. threats, plans to harm and incitement":
        changeMessagePrediction(message, "threats")
        return message_prediction
    if predicted_label == "2. derogation":
        changeMessagePrediction(message, "derogation")
        return  message_prediction
    if predicted_label == "3. animosity":
        changeMessagePrediction(message, "animosity")
        return  message_prediction
    if predicted_label == "4. prejudiced discussions":
        changeMessagePrediction(message, "prejudiced_discussions")
        return  message_prediction


#validation of right endpoints
message_not_sexist_model = PredictionModel(**message_prediction)
message_sexist_model = PredictionModel(**message_prediction)
message_sexist_model = PredictionModel(**message_prediction)
message_sexist_model = PredictionModel(**message_prediction)
message_sexist_model = PredictionModel(**message_prediction)
message_sexist_model = PredictionModel(**message_prediction)
main_description_model = MainDescriptionModel(**main_description)
task_model = TaskModel(**task)
task_A_model = SubTaskModel(**task_A)
metrics_A_model = MetricsModel(**metrics_A)
preprocessing_A_model = PreprocessingModel(**preprocessing_A)
task_B_model = SubTaskModel(**task_B)
metrics_B_model = MetricsModel(**metrics_B)
preprocessing_B_model = PreprocessingModel(**preprocessing_B)
