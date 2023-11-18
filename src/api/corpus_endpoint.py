from pydantic import BaseModel, ValidationError
from typing import List, Optional

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

#validation of right endpoints
main_description_model = MainDescriptionModel(**main_description)
task_model = TaskModel(**task)
task_A_model = SubTaskModel(**task_A)
metrics_A_model = MetricsModel(**metrics_A)
preprocessing_A_model = PreprocessingModel(**preprocessing_A)
task_B_model = SubTaskModel(**task_B)
metrics_B_model = MetricsModel(**metrics_B)
preprocessing_B_model = PreprocessingModel(**preprocessing_B)