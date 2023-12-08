Detection Of Online Sexism
==============================
![pylint](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/actions/workflows/pylint_check.yaml/badge.svg)
![pydantic](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/actions/workflows/pydantic_check.yaml/badge.svg)
![fastapi](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/actions/workflows/fastapi_check.yaml/badge.svg)


The system, developed by Grazia Perna, Maria Elena Zaza, and Francesco Brescia, addresses the SemEval 2023 - Task 10 - Explainable Detection of Online Sexism (EDOS) challenge hosted on CodaLab. The primary aim of this initiative is to create and implement models capable of identifying and analyzing sexist content in online textual data. This documentation provides an overview of the methodologies employed, including data preprocessing techniques and the application of advanced machine learning models, to tackle the challenge effectively. The project underscores the importance of developing tools to foster a more inclusive and respectful online environment.

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
