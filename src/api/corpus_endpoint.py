"""
    Module: corpus_endpoint
    Description: This module contains the functions and dictionaries 
                for the api calls and their validation using Pydantic.
    Authors: Francesco Brescia
            Maria Elena Zaza
            Grazia Perna
    Date: 2023-12-14
"""
#pylint: disable=wrong-import-position
#pylint: disable=import-error
#pylint: disable=unused-import
import pickle
import os
import sys
from typing import List, Optional
sys.path.append(os.getcwd()+"/src/models/")
import train_a
import train_b
from pydantic import BaseModel, ValidationError





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
    """
    Class: PredictionModel
    Description: This class contains:
    - prediction: str
    """
    prediction: str

class MainDescriptionModel(BaseModel):
    """
    Class: MainDescriptionModel
    Description: This class contains:
    - title: str
    - description: str
    - version: str
    - available_endpoints: List[str]
    """
    title: str
    description: str
    version: str
    available_endpoints: List[str]

class TaskModel(BaseModel):
    """
    Class: TaskModel
    Description: This class contains:
    - title: str
    - description: str
    - pipeline: str
    - more_information: List[str]
    """
    title: str
    description: str
    pipeline: str
    more_information: List[str]

class SubTaskModel(BaseModel):
    """
    Class: SubTaskModel
    Description: This class contains:
    - title: str
    - description: str
    - model: List[str]
    - metrics: str
    """
    title: str
    description: str
    model: List[str]
    metrics: str

class MetricsModel(BaseModel):
    """
    Class: MetricsModel
    Description: This class contains:
    - title: str
    - model: str
    - f1: float
    - recall: float
    - precision: float
    """
    title: str
    model: str
    f1: float
    recall: float
    precision: float

class PreprocessingModel(BaseModel):
    """
    Class: PreprocessingModel
    Description: This class contains:
    - title: str
    - tokenizer: str
    - vectorizer: str
    - lemmatizer: Optional[str] = None
    """
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


def change_message_prediction(message, prediction):
    """
    Function: changeMessagePrediction(message, prediction)
    Description: This function allows to change the te message
                prediction dictonary according to its parameter
    """
    message_prediction["message"] = message
    message_prediction["prediction"] = prediction


def predict_sexism(message):
    """
    Function: predict_sexism(message)
    Description: This function allows to predict if a message is sexist or not
    """
    predicted_label = sexism_model.predict([message])[0]
    if predicted_label == "not sexist":
        change_message_prediction(message, "not_sexist")
    else:
        change_message_prediction(message, "sexist")
    return  message_prediction


def predict_category(message):
    """
    Function: predict_sexism(message)
    Description: This function allows to predict the category of sexism
                of a message
    """
    predicted_label = category_model.predict([message])[0]
    if predicted_label == "1. threats, plans to harm and incitement":
        change_message_prediction(message, "threats")
    elif predicted_label == "2. derogation":
        change_message_prediction(message, "derogation")
    elif predicted_label == "3. animosity":
        change_message_prediction(message, "animosity")
    elif predicted_label == "4. prejudiced discussions":
        change_message_prediction(message, "prejudiced_discussions")
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
