"""
Module: detect
Description: This module contains functions for alibi detect
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
import os
import sys
import numpy as np
sys.path.append(os.getcwd()+"/src/models/")
import train_a
import train_b
from datetime import datetime
import string
import pandas as pd
import pickle
from alibi_detect.cd import KSDrift, ClassifierDrift
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import TransformerMixin




COLUMN_DATA = 'text'
SEXISM_TRAIN_DATA_PATH = "../../data/Raw/train_sexist.csv"
SEXISM_TEST_DATA_PATH = "../../data/Raw/test_sexist.csv"
SEXISM_VALIDATION_DATA_PATH = "../../data/Raw/dev_sexist.csv"

SEXISM_MODEL_PATH = "../../models/validation_a.pkl"
CATEGORY_MODEL_PATH = "../../models/validation_b.pkl"

CATEGORY_TRAIN_DATA_PATH = "../../data/Raw/train_category.csv"
CATEGORY_TEST_DATA_PATH = "../../data/Raw/test_category.csv"
CATEGORY_VALIDATION_DATA_PATH = "../../data/Raw/dev_category.csv"

SEXISM_LOG_FILE = "../../data/alibi_detect_logs/model_sexism.txt"
CATEGORY_LOG_FILE = "../../data/alibi_detect_logs/model_category.txt"

DRIFT_THRESHOLD = 0.4


class Predictors(TransformerMixin):
    """
    A custom transformer class for text preprocessing using scikit-learn's TransformerMixin.
    This class provides text preprocessing capabilities 
    by implementing the TransformerMixin interface from scikit-learn.
    """
    def transform(self, x):
        """
        Preprocess and clean a list of text data.

        Args:
            x (list): A list of text data to be preprocessed.

        Returns:
            list: A list of cleaned and preprocessed text data.
        """
        return [' '.join(clean_text(text)) for text in x]

    def fit(self):
        """
        Fit the transformer (no operation).

        Returns:
            self: The fitted transformer instance.
        """
        return self

    def get_params(self):
        """
        Get the parameters of the transformer (empty dictionary).

        Returns:
            dict: An empty dictionary.
        """
        return {}

def clean_text(text):
    """
    This function takes a text as input, removes punctuation characters
    and converts the text to lowercase.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned and preprocessed text.

    """
    translator = str.maketrans("", "", string.punctuation)
    text_without_punctuation = text.translate(translator).lower()

    tokenizer = TreebankWordTokenizer()
    lemmatizer = WordNetLemmatizer()

    tokens = tokenizer.tokenize(text_without_punctuation)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return lemmatized_tokens


def compute_features(train_data_path, test_data_path, validation_data_path):
    """
    Compute features using CountVectorizer.

    Parameters:
    - train_data_path (str): Path to the training data CSV file.
    - test_data_path (str): Path to the test data CSV file.
    - validation_data_path (str): Path to the validation data CSV file.

    Returns:
    tuple: A tuple containing three arrays - train_features, test_features, and validation_features.
           Each array contains the computed features using CountVectorizer.
    """
    vectorizer = CountVectorizer(tokenizer=lambda x: x.split(), ngram_range=(1, 2))

    train_features = vectorizer.fit_transform(data_preprocessing(train_data_path)).toarray()
    validation_features =  vectorizer.transform(data_preprocessing(validation_data_path)).toarray()
    test_features = vectorizer.transform(data_preprocessing(test_data_path)).toarray()

    print("Train Features shape:", train_features.shape)
    print("Test Features shape:", test_features.shape)
    print("Validation Features shape:", validation_features.shape)

    return train_features, test_features, validation_features


def data_preprocessing(data_path):
    """
    Preprocess the text data from the specified CSV file.

    Parameters:
    - data_path (str): Path to the CSV file containing the text data.

    Returns:
    list: A list of preprocessed text data using the Predictors transformer.
    """
    data = pd.read_csv(data_path)
    texts = data[COLUMN_DATA]
    return Predictors().transform(texts)


def detect_drift(train_features, test_features, validation_features, model):
    """
    Detect drift between train, test, and validation features.

    Parameters:
    - train_features (ndarray)
    - test_features (ndarray)
    - validation_features (ndarray)

    Returns:
    tuple: Drift results for train vs test and train vs validation.
    """

    drift_results_train_test = create_and_perform_drift_detection(
        train_features, test_features, model)

    drift_results_train_validation = create_and_perform_drift_detection(
        train_features, validation_features, model)

    return drift_results_train_test, drift_results_train_validation


def create_and_perform_drift_detection(feature_of_drift, feature_to_compare, model, threshold=DRIFT_THRESHOLD):
    """
    Create and perform drift detection between two sets of features.

    Parameters:
    - feature_of_drift (ndarray): Features for drift detection.
    - feature_to_compare (ndarray): Features to compare for drift.
    - threshold (float): Threshold for drift detection. Default is 0.1.

    Returns:
    dict: Drift detection results.
    """
    x_ref = np.random.rand(100, 1)
    #drift_detector = KSDrift(feature_of_drift, p_val=threshold)
    drift_detector = ClassifierDrift(x_ref =x_ref, p_val=threshold, model=model)

    drift_results = drift_detector.predict(
        feature_to_compare,
        drift_type='batch',
        return_p_val=True,
        return_distance=True)

    return drift_results


def log_drift_results(log_file, model_name, dataset_name, drift_results, drift_threshold=DRIFT_THRESHOLD):
    """
    Log drift detection results to a file and print a message if drift is detected.

    Parameters:
    - log_file (str): Path to the log file.
    - model_name (str): Name of the model.
    - dataset_name (str): Name of the dataset.
    - drift_results (dict): Drift detection results.
    - drift_threshold (float): Threshold for drift detection. Default is 0.1.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open(log_file, 'a', encoding='utf-8') as log:
        log.write(f"[{current_time}] Model: {model_name}, Dataset: {dataset_name}\n")
        log.write(f"  Drift Detected: {drift_results['data']['is_drift']}\n")
        log.write(f"  p-value: {drift_results['data']['p_val']}\n")
        log.write(f"  distance: {drift_results['data']['distance']}\n")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    drift_detected = drift_results['data']['is_drift']
    distance = drift_results['data']['distance']

    if drift_detected and max(distance) > drift_threshold:
        print(f"Drift detected in {dataset_name}"+
              "for {model_name}"+
              "with distance {max(distance)}")


if __name__ == "__main__":

    with open(SEXISM_MODEL_PATH, 'rb') as file:
        sexism_model = pickle.load(file)

    with open(CATEGORY_MODEL_PATH, 'rb') as file:
        category_model = pickle.load(file)

    sexism_train, sexism_test, sexism_validation = compute_features(
        SEXISM_TRAIN_DATA_PATH, SEXISM_TEST_DATA_PATH, SEXISM_VALIDATION_DATA_PATH
    )

    category_train,category_test, category_validation = compute_features(
        CATEGORY_TRAIN_DATA_PATH, CATEGORY_TEST_DATA_PATH, CATEGORY_VALIDATION_DATA_PATH
    )

    # model_sexism_drift_results_test, model_sexism_drift_results_validation = detect_drift(
    #     sexism_train, sexism_test, sexism_validation
    # )

    # model_category_drift_results_test, model_category_drift_results_validation = detect_drift(
    #     category_train, category_test, category_validation
    # )

    model_sexism_drift_results_test, model_sexism_drift_results_validation = detect_drift(
        sexism_train, sexism_test, sexism_validation, model=sexism_model
    )

    model_category_drift_results_test, model_category_drift_results_validation = detect_drift(
        category_train, category_test, category_validation, model=category_model
    )
    print("Model Sexism - Drift Detected (Test Set):",
          model_sexism_drift_results_test['data']['is_drift'])
    print("Model Sexism - Drift Detected (Validation Set):",
          model_sexism_drift_results_validation['data']['is_drift'])
    print("Model Category - Drift Detected (Test Set):",
          model_category_drift_results_test['data']['is_drift'])
    print("Model Category - Drift Detected (Validation Set):",
          model_category_drift_results_validation['data']['is_drift'])

    log_drift_results(SEXISM_LOG_FILE,
                      "Model Sexism",
                      "Test Set",
                      model_sexism_drift_results_test)

    log_drift_results(SEXISM_LOG_FILE,
                      "Model Sexism",
                      "Validation Set",
                      model_sexism_drift_results_validation)

    log_drift_results(CATEGORY_LOG_FILE,
                      "Model Category",
                      "Test Set",
                      model_category_drift_results_test)

    log_drift_results(CATEGORY_LOG_FILE,
                      "Model Category",
                      "Validation Set",
                      model_category_drift_results_validation)
