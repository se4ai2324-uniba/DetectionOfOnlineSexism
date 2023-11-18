models = ["LinearSVC classifier", "Random Forest"]

main_description = {"Title": "Detection of Online Sexism",
            "Description": "An NLP model used to detect sexist messages and the type of sexism.",
            "Version": "1.0",
            "Available endpoints": ["/task", "/task/A", "/task/A/metrics", "/task/A/preprocessing", "/task/B", "/task/B/metrics", "/task/B/preprocessing"]  }

task = {
    "Title": "Tasks",
    "Description": "The models have two hierarchical tasks: TASK A and TASK B",
    "Pipeline": "- Preprocessing - Training - Validation - Test",
    "More information": ["/task/A", "/task/B"]
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