"""
Module: detect
Description: This module contains functions for alibi detect
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
#pylint: disable=import-error
#pylint: disable=unused-import
#pylint: disable=wrong-import-position

import os
import sys
from datetime import datetime
import pickle
import string
sys.path.append(os.getcwd()+"/src/models/")
import train_a
import train_b
import pandas as pd
from alibi_detect.cd import KSDrift
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import TransformerMixin
from faker import Faker


SEXISM_MODEL_PATH = os.path.join(os.path.dirname(__file__),
                                    '..//..//models/validation_a.pkl')
CATEGORY_MODEL_PATH = os.path.join(os.path.dirname(__file__),
                                   '..//..//models/validation_b.pkl')

NUMBER_OF_FAKE_DATA = 5000

COLUMN_DATA = 'text'
SEXISM_TRAIN_DATA_PATH = os.path.join(os.path.dirname(__file__),
                                      '..//../data/Raw/train_sexist.csv')
CATEGORY_TRAIN_DATA_PATH = os.path.join(os.path.dirname(__file__),
                                        '..//../data/Raw/train_category.csv')

SEXISM_LOG_PATH = os.path.join(os.path.dirname(__file__),
                               '..//../data/alibi_detect_logs/model_sexism.txt')
CATEGORY_LOG_PATH = os.path.join(os.path.dirname(__file__),
                                 '..//../data/alibi_detect_logs/model_category.txt')

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


def generate_fake_data(label_column_name, model, num_samples = NUMBER_OF_FAKE_DATA):
    """
    Generate fake data with predicted labels using a pre-trained model.

    Args:
        label_column_name (str): Name of the label column.
        model: Pre-trained model for making predictions.
        num_samples (int): Number of fake data samples to generate.

    Returns:
        pd.DataFrame: DataFrame containing generated fake data.
    """

    fake = Faker()
    fake_data = pd.DataFrame({
        'ID': range(num_samples),
        'text': [fake.sentence() for _ in range(num_samples)],
    })
    fake_data[label_column_name] = model.predict(fake_data['text'])

    return fake_data

def compute_features(train_data_path, fake_data):
    """
    Compute features using CountVectorizer.

    Parameters:
    - train_data_path (str): Path to the training data CSV file.
    - fake_data (pd.DataFrame): DataFrame containing fake data.

    Returns:
    tuple: A tuple containing two arrays - train_features and fake_features.
           Each array contains the computed features using CountVectorizer.
    """

    vectorizer = CountVectorizer(tokenizer=lambda x: x.split(), ngram_range=(1, 2))
    training_data = pd.read_csv(train_data_path)
    train_features = vectorizer.fit_transform(data_preprocessing(training_data)).toarray()
    fake_features = vectorizer.transform(data_preprocessing(fake_data)).toarray()

    print("Train Features shape:", train_features.shape)
    print("Fake Features shape:", fake_features.shape)

    return train_features, fake_features

def data_preprocessing(data):
    """
    Preprocess the text data from the specified DataFrame.

    Parameters:
    - data (pd.DataFrame): DataFrame containing the text data.

    Returns:
    list: A list of preprocessed text data using the Predictors transformer.
    """

    texts = data[COLUMN_DATA]
    return Predictors().transform(texts)


def detect_drift(train_features, fake_features):
    """
    Detect drift between train and fake features.

    Parameters:
    - train_features (ndarray): Features from the training data.
    - fake_features (ndarray): Features from the generated fake data.

    Returns:
    dict: Drift detection results for train vs fake.
    """

    drift_results_fake_test = create_and_perform_drift_detection(
        train_features, fake_features)


    return drift_results_fake_test


def create_and_perform_drift_detection(feature_of_drift,
                                       feature_to_compare,
                                       threshold=DRIFT_THRESHOLD):
    """
    Create and perform drift detection between two sets of features.

    Parameters:
    - feature_of_drift (ndarray): Features for drift detection.
    - feature_to_compare (ndarray): Features to compare for drift.
    - threshold (float): Threshold for drift detection. 

    Returns:
    dict: Drift detection results.
    """

    drift_detector = KSDrift(feature_of_drift, p_val=threshold)

    drift_results = drift_detector.predict(
        feature_to_compare,
        drift_type='batch',
        return_p_val=True,
        return_distance=True)

    return drift_results


def log_drift_results(log_file, model_name, drift_results):
    """
    Log drift detection results to a file and print a message if drift is detected.

    Parameters:
    - log_file (str): Path to the log file.
    - model_name (str): Name of the model.
    - drift_results (dict): Drift detection results.
    """

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open(log_file, 'w', encoding='utf-8') as log:
        log.write(f"[{current_time}] Model: {model_name}\n")
        log.write(f"  Drift Detected: {drift_results['data']['is_drift']}\n")
        log.write(f"  p-value: {drift_results['data']['p_val']}\n")
        log.write(f"  distance: {drift_results['data']['distance']}\n")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":

    #drift detection for sexism model
    with open(SEXISM_MODEL_PATH, 'rb') as file:
        sexism_model = pickle.load(file)

    sexism_fake_data = generate_fake_data('label_sexist',
                                          sexism_model)
    print(sexism_fake_data.head())

    sexism_feature, fake_sexism_feature = compute_features(
        SEXISM_TRAIN_DATA_PATH, sexism_fake_data
    )

    model_sexism_drift_results = detect_drift(
        sexism_feature, fake_sexism_feature
    )


    #drift detection for category model
    with open(CATEGORY_MODEL_PATH, 'rb') as file:
        category_model = pickle.load(file)

    category_fake_data = generate_fake_data('label_category',
                                            category_model)

    print(category_fake_data.head())

    category_feature, fake_category_feature = compute_features(
        CATEGORY_TRAIN_DATA_PATH, category_fake_data
    )

    model_category_drift_results = detect_drift(
        category_feature, fake_category_feature
    )

    print("Model Sexism - Drift Detected:",
          model_sexism_drift_results['data']['is_drift'])
    print("Model Category - Drift Detected:",
          model_category_drift_results['data']['is_drift'])

    log_drift_results(SEXISM_LOG_PATH,
                      "Model Sexism",
                      model_sexism_drift_results)

    log_drift_results(CATEGORY_LOG_PATH,
                      "Model Category",
                      model_category_drift_results)
