from pydantic import BaseModel, ValidationError
from typing import List, Optional
import pickle
import os
import sys
import src.models.train_A
import src.models.train_B

current_directory = os.getcwd()
with open(current_directory +'/../../models/validation_A.pkl', 'rb') as file:
    sexism_model = pickle.load(file)
with open(current_directory +'/../../models/validation_B.pkl', 'rb') as file:
    category_model = pickle.load(file)

class PredictionModel(BaseModel):
    Prediction: str

class MainDescriptionModel(BaseModel):
    Title: str
    Description: str
    Version: str
    AvailableEndpoints: List[str]

class TaskModel(BaseModel):
    Title: str
    Description: str
    Pipeline: str
    MoreInformation: List[str]

class SubTaskModel(BaseModel):
    Title: str
    Description: str
    Model: List[str]
    Metrics: str

class MetricsModel(BaseModel):
    Title: str
    Model: str
    F1: float
    Recall: float
    Precision: float

class PreprocessingModel(BaseModel):
    Title: str
    Tokenizer: str
    Vectorizer: str
    Lemmatizer: Optional[str] = None

models = ["LinearSVC classifier", "Random Forest"]

main_description = {
    "Title": "Detection of Online Sexism",
    "Description": "An NLP model used to detect sexist messages and the type of sexism.",
    "Version": "1.0",
    "AvailableEndpoints": ["/task", "/task/A", "/task/A/metrics", "/task/A/preprocessing", "/task/B", "/task/B/metrics", "/task/B/preprocessing"]
}

task = {
    "Title": "Tasks",
    "Description": "The models have two hierarchical tasks: TASK A and TASK B",
    "Pipeline": "- Preprocessing - Training - Validation - Test",
    "MoreInformation": ["/task/A", "/task/B"]
}

task_A = {
    "Title": "Task A",
    "Description": "Sexism Detection: for detecting whether a post is sexist",
    "Model": models,
    "Metrics": "/task/A/metrics"
}

metrics_A = {
    "Title": "Metrics Task A",
    "Model": "Linear SVC",
    "F1": 0.7637,
    "Recall": 0.7444,
    "Precision": 0.7947
}

preprocessing_A = {
    "Title": "Preprocessing Task A",
    "Tokenizer": "TreeBankWord",
    "Vectorizer": "CountVectorizer",
    "Lemmatizer": "Yes",
}

task_B = {
    "Title": "Task B",
    "Description": "Category of Sexism: for assigning to each of the sexist texts a category (threats, derogation, animosity, prejudiced discussions",
    "Model": models,
    "Metrics": "/task/B/metrics"
}

metrics_B = {
    "Title": "Metrics Task B",
    "Model": "Linear SVC",
    "F1": 0.4597,
    "Recall": 0.4438,
    "Precision": 0.4932
}

preprocessing_B = {
    "Title": "Preprocessing Task B",
    "Tokenizer": "TreeBankWord",
    "Vectorizer": "CountVectorizer",
    "Lemmatizer": "No",
}

message_not_sexist= {
    "Prediction": "The message has been categorized as not sexist."
}

message_sexist= {
    "Prediction": "The message has been categorized as sexist."
}

message_prejudiced_discussions = {
    "Prediction": "The category of sexism is 'prejudiced discussions'."
}

message_animosity = {
    "Prediction": "The category of sexism is 'animosity'."
}

message_derogation = {
    "Prediction": "The category of sexism is 'derogation'."
}

message_threats = {
    "Prediction": "The category of sexism is 'threats'."
}


#example of validation error
try:
    #in this case "MoreInformation" should be a list 
    invalid_task_data = {
        "Title": "Invalid Task",
        "Description": "Invalid Description",
        "Pipeline": "Invalid Pipeline",
        "MoreInformation": "Invalid Information"  
    }
    
    invalid_task_model = TaskModel(**invalid_task_data)
except ValidationError as e:
    print(e.json())


def predict_sexism(message):
    predicted_label = sexism_model.predict([message])[0]
    if predicted_label == "not sexist":
        return  "The message has been categorized as not sexist."
    else:
        return  "The message has been categorized as sexist."
    

def predict_category(message):
    predicted_label = sexism_model.predict([message])[0]
    if predicted_label == "1. threats, plans to harm and incitement":
        return "The category of sexism is 'threats'."
    if predicted_label == "2. derogation":
        return  "The category of sexism is 'derogation'."
    if predicted_label == "3. animosity":
        return  "The category of sexism is 'animosity'."
    if predicted_label == "4. prejudiced discussions":
        return  "The category of sexism is 'prejudiced discussions'."
    
#validation of right endpoints
message_not_sexist_model = PredictionModel(**message_not_sexist)
message_sexist_model = PredictionModel(**message_sexist)
message_sexist_model = PredictionModel(**message_prejudiced_discussions)
message_sexist_model = PredictionModel(**message_animosity)
message_sexist_model = PredictionModel(**message_derogation)
message_sexist_model = PredictionModel(**message_threats)
main_description_model = MainDescriptionModel(**main_description)
task_model = TaskModel(**task)
task_A_model = SubTaskModel(**task_A)
metrics_A_model = MetricsModel(**metrics_A)
preprocessing_A_model = PreprocessingModel(**preprocessing_A)
task_B_model = SubTaskModel(**task_B)
metrics_B_model = MetricsModel(**metrics_B)
preprocessing_B_model = PreprocessingModel(**preprocessing_B)