Detection Of Online Sexism
==============================
![pylint](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/actions/workflows/pylint_check.yaml/badge.svg)
![pydantic](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/actions/workflows/pydantic_check.yaml/badge.svg)
![fastapi](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/actions/workflows/fastapi_check.yaml/badge.svg)
![pytest](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/actions/workflows/pytest_check.yaml/badge.svg)
![drift-detection](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/actions/workflows/alibi-detect_check.yaml/badge.svg)


The system addresses the SemEval 2023 - Task 10 - Explainable Detection of Online Sexism (EDOS) challenge hosted on CodaLab. The primary aim of this initiative is to create and implement models capable of identifying and analyzing sexist content in online textual data. This documentation provides an overview of the methodologies employed, including data preprocessing techniques and the application of advanced machine learning models, to tackle the challenge effectively. The project underscores the importance of developing tools to foster a more inclusive and respectful online environment.

Project Description
------------
The initial phase of the project involved the preprocessing of the dataset. This step was crucial to ensure the effectiveness of the models. The preprocessing techniques included:
- Removing Extra Spaces: Ensuring that the text data is free from unnecessary spaces which could affect the model's interpretation.
- Converting Text to Lowercase: Standardizing the text data by converting all characters to lowercase to maintain uniformity.
- Eliminating Punctuation: Removing punctuation marks to reduce the complexity of the text and focus on the content.
- Tokenization: Breaking down the text into smaller units (tokens) for better analysis.
- Lemmatization (Task A specific): Reducing words to their base or root form, which is particularly beneficial for linguistic analysis.

Post-preprocessing, the text data was subjected to feature extraction. This involved the use of a CountVectorizer, which transformed the textual data into numerical features. These features were then utilized for classification purposes in the models.

The challenge have two hierarchical tasks:
- TASK A - Sexism Detection: for detecting whether a post is sexist by using the LinearSVC classifier.
- TASK B - Category of Sexism: for assigning to each of the sexist texts one of the following categories:
    - threats
    - derogation
    - animosity
    - prejudiced discussions

To conclude, for both task the system utilizes the SVM model in order to compute the two tasks and to evaluate the performance of the models the GriSearchCV was employed for performing the hyperparameter tuning in order to determine the optimal values of the models. It uses the Cross-Validation method, fixed to 10.

The project, the paper and a simple demo are available at: https://github.com/graziaperna/NLP-project.

Web-App Links
------------
The Machine Learning system was deployed by using the Microsoft Azure provider. You can access the frontend and backend of the application using and prometheus dashboard the following links:

- Frontend: http://52.188.133.113
- Backend: http://52.188.133.113:8000
- Prometheus: https://prometheusonlinesexism.azurewebsites.net

Uptime Monitoring
------------
We use Better Uptime to monitor the status of our website. You can check the current status and past incidents at our Better Uptime status page:

- Link: https://detectiononlinesexism.betteruptime.com

Documentation Structure 
------------
Within each folder, you will find specific documentation that explains the topic covered in that particular section. These documents offer detailed information and resources related to the specific subject of the folder, allowing for a comprehensive understanding of the topics addressed.

For a comprehensive overview and easy reference across all sprints, navigate to [references/](references/README.md) folder. In this central documentation, you will find an index that includes all the topics. 

Project Organization
------------
    ├── .dvc                <- Data Version Control configurations.
    ├── .github             <- Folder containing all the yaml files for the GitHub Actions
    │   └── workflows
    │       ├── fastapi_check.yaml
    │       ├── pydantic_check.yaml
    │       ├── alibi-detect_check.yaml    
    │       ├── pylint_check.yaml
    │       ├── pytest_check.yaml
    │       └── README.md   <- GitHub Actions documentation
    │
    ├── data
    │   ├── Raw            <- Datasets used for training, validation and test.
    │   │    ├── dev_category.csv
    │   │    ├── dev_sexist.csv
    │   │    ├── test_sexist.csv
    │   │    ├── test_category.csv
    │   │    ├── train_sexist.csv
    │   │    ├── train_category.csv
    │   │    ├── dev_category.csv.dvc
    │   │    ├── dev_sexist.csv.dvc
    │   │    ├── test_sexist.csv.dvc
    │   │    ├── test_category.csv.dvc
    │   │    ├── train_sexist.csv.dvc
    │   │    └── train_category.csv.dvc
    │   │
    │   └── README.md      <- The README for developers using these datasets.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── frontend           <- All HTML, CSS, JS and configuration files about the frontend.
    │   ├── Dockerfile     <- Docker file for the frontend
    |   ├── index.html     <- Frontend html
    │   ├── logo.png       <- Web Page logo
    │   ├── nginx.conf     <- Configuration file for nginx.
    │   ├── script.js      <- Frontend script
    │   └── README.md      
    |
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │   ├── validation_a.pkl
    │   ├── validation_b.pkl
    │   ├── train_a.pkl
    │   ├── train_b.pkl
    │   └── README.md      
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    |
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    |   |
    │   ├── deploy_doc
    │   │   └── README.md 
    │   ├── docker_doc
    │   │   └── README.md
    │   ├── dvc_mlflow_doc
    │   │   └── README.md
    │   ├── great_expectations_doc
    │   │   ├── expectations
    │   │   ├── static
    │   │   └── index.html
    │   ├── monitoring_doc
    │   │   └── README.md
    │   ├── images_doc
    │   └── READMME.md
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── alibi_detect_logs            <- Logs generated after data drift analysis.
    │   │    ├── model_category.txt
    │   │    └── model_sexsism.txt
    │   ├── locust                       <- Logs generated after locust analysis.
    │   │    ├── report_exceptions.csv
    │   │    ├── report_stats_history.csv
    │   │    ├── report_stats.csv
    │   │    └── report_failures.csv
    │   ├── output_codecarbon           <- Logs generated after code carbon analysis.
    │   │    ├── output_train_a.csv
    │   │    ├── output_train_a.csv.bak
    │   │    ├── output_train_b.csv
    │   │    └── output_train_b.csv.bak
    │   ├── mlruns                      <- Logs generated after mlflow runs.
    │   └── figures                     <- Generated graphics and figures to be used in reporting
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   ├── README.md
    │   ├── api            <- Scripts to crate Api using FastAPI
    │   │   ├── corpus_endpoint.py
    │   │   ├── prometheus_monitoring.py
    │   │   ├── server_api.py
    │   │   └── dashboards
    │   │       └── grafana.json
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   ├── drift_detection.py
    │   │   └── build_features.py
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── test_a.py
    │   │   ├── test_b.py
    │   │   ├── train_a.py
    │   │   ├── train_b.py
    │   │   ├── validation_a.py
    │   │   ├── validation_b.py
    │   │   ├── .codecarbon.config
    │   │   └── MLflow
    │   │       ├── mlflow_test_a.py
    │   │       ├── mlflow_test_b.py
    │   │       ├── mlflow_train_a.py
    │   │       ├── mlflow_train_b.py
    │   │       ├── mlflow_validation_a.py
    │   │       └── mlflow_validation_b.py
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │   
    ├── tests         <- Scripts to test using Pytest
    │   ├── api_testing
    │   │   └── test_api.py
    │   ├── dataset_testing
    │   │   ├── test_dataset_model_a.py
    │   │   └── test_dataset_model_b.py
    │   ├── model_training_testing
    │   │    └── test_overfit.py
    │   ├── preprocessing_testing
    │   │    └── test_preprocessing.py
    │   ├── behavioral_testing
    │   │   ├── test_directional_model_a.py
    │   │   ├── test_directional_model_b.py
    │   │   ├── test_invariance_model_a.py
    │   │   ├── test_invariance_model_b.py
    │   │   ├── test_minimum_funcionality_model_a.py
    │   │   └── test_minimum_funcionality_model_b.py
    │   └── README.md
    |
    ├── .dockerignore           <- Docker ignore file.
    ├── .dvcignore              <- Data Version Control ignore file.
    ├── .gitignore              <- Specifications of files to be ignored by Git.
    ├── docker-compose.yaml     <- Docker Compose configuration.
    ├── Dockerfile              <- Docker file for the backend.
    ├── dvc.lock                <- Data Version Control record file.
    ├── dvc.yaml                <- Data Version Control pipeline file.
    ├── get-pip.py              <- Script to automatically install the latest version of pip
    ├── LICENSE                 <- License as plain text.
    ├── locustfile.py           <- Defines user behavior in load testing.
    ├── Makefile                <- Makefile with commands like `make data` or `make train`
    ├── prometheus.yml          <- Prometheus configuration file.
    ├── README.md               <- The top-level README for developers using this project
    ├── requirements.txt        <- The requirements file for production environment.
    ├── setup.py                <- Makes project pip installable (pip install -e .) so src can be imported
    ├── test_environment.py     <- Checks python version.
    └── tox.ini                 <- tox file with settings for running tox; see tox.readthedocs.io
    


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
