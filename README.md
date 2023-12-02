Detection Of Online Sexism
==============================
![workflow](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/workflows/pylint_check.yaml/badge.svg?)

The project described in this documentation has been developed for the "SemEval 2023 - Task 10 - Explainable Detection of Online Sexism (EDOS)" challenge on CodaLab by Grazia Perna, Maria Elena Zaza and Francesco Brescia in which two models have been implemented.

Before training the models, the used data was preprocessed to remove spaces, convert text to lowercase and eliminate punctuation. Other techniques like tokenization and lemmatization (for task A) were also used here.
The preprocessed text was then inserted into a CountVectorizer, which transformed the text into numerical features suitable for classification.

The models have two hierarchical tasks:
- TASK A - Sexism Detection: for detecting whether a post is sexist by using the LinearSVC classifier.
- TASK B - Category of Sexism: for assigning to each of the sexist texts one of the following categories:
    - threats
    - derogation
    - animosity
    - prejudiced discussions

To evaluate the performance of the models the GriSearchCV was employed for performing the hyperparameter tuning in order to determine the optimal values of the models. It uses the Cross-Validation method, fixed to 10.

The project, the paper and a simple demo are available at: https://github.com/graziaperna/NLP-project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── Raw            <- Datasets used for training, validation and test.
    │   │    ├── dev_category.csv
    │   │    ├── dev_sexist.csv
    │   │    ├── test_sexist.csv
    │   │    ├── test_category.csv
    │   │    ├── train_sexist.csv
    │   │    └── train_category.csv
    │   │
    │   └── README.md      <- The README for developers using these datasets.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── api            <- Scripts to crate Api using FastAPI
    │   │   ├── corpus_endpoint.py
    │   │   ├── redoc.py
    │   │   └── server_api.py
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── test_a.py
    │   │   ├── test_b.py
    │   │   ├── train_a.py
    │   │   ├── train_b.py
    │   │   ├── validation_a.py
    │   │   ├── validation_b.py
    │   │   ├── mlruns
    │   │   └── MLflow
    │   │       ├── test_a.py
    │   │       ├── test_b.py
    │   │       ├── train_a.py
    │   │       ├── train_b.py
    │   │       ├── validation_a.py
    │   │       └── validation_b.py
    │   ├── tests         <- Scripts to test using Pytest
    │   │   ├── api_testing
    │   │   │   └── test_api.py
    │   │   │
    │   │   ├── dataset_testing
    │   │   │   ├── test_dataset_model_a.py
    │   │   │   └── test_dataset_model_b.py
    │   │   │
    │   │   ├── model_training_testing
    │   │   │    └── test_overfit.py
    │   │   │
    │   │   ├── preprocessing_testing
    │   │   │    └── test_preprocessing.py
    │   │   │
    │   │   └── behavioral_testing
    │   │       ├── test_directional_model_a.py
    │   │       ├── test_directional_model_b.py
    │   │       ├── test_invariance_model_a.py
    │   │       ├── test_invariance_model_b.py
    │   │       ├── test_minimum_funcionality_model_a.py
    │   │       └── test_minimum_funcionality_model_b.py
    │   │  
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
