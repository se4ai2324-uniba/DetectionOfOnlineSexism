from pydantic import BaseModel, ValidationError
from typing import List, Optional

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
    "available_endpoints": ["/task", "/task/A", "/task/A/metrics", "/task/A/preprocessing", "/task/B", "/task/B/metrics", "/task/B/preprocessing"]
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
    "description": "Category of Sexism: for assigning to each of the sexist texts a category (threats, derogation, animosity, prejudiced discussions",
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

#validation of right endpoints
main_description_model = MainDescriptionModel(**main_description)
task_model = TaskModel(**task)
task_A_model = SubTaskModel(**task_A)
metrics_A_model = MetricsModel(**metrics_A)
preprocessing_A_model = PreprocessingModel(**preprocessing_A)
task_B_model = SubTaskModel(**task_B)
metrics_B_model = MetricsModel(**metrics_B)
preprocessing_B_model = PreprocessingModel(**preprocessing_B)