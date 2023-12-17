"""
Module: train_b
Description: This module contains functions for training model b.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
Date: 2023-11-03
"""
#pylint: disable=no-member
import string
import pickle
import os
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from pandas import read_csv
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer
from codecarbon import EmissionsTracker
import pynvml

n_cpu = os.cpu_count()
print("Number of CPUs in the system:", n_cpu)

# Custom transformer using spaCy
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
        return [clean_text(text) for text in x]

    def fit(self, x, y=None, **fit_params): # pylint: disable=unused-argument
        """
        Fit the transformer (no operation).

        Args:
            X: The input data.
            y: The target labels (ignored).

        Returns:
            self: The fitted transformer instance.
        """
        return self

    def get_params(self, deep=True): # pylint: disable=unused-argument
        """
        Get the parameters of the transformer (empty dictionary).

        Returns:
            dict: An empty dictionary.
        """
        return {}

# Basic function to clean the text
def clean_text(text):
    """
    This function takes a text as input, 
    removes punctuation characters, 
    and converts the text to lowercase.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned and preprocessed text.

    """
    # Removing spaces and converting text into lowercase
    translator = str.maketrans("", "", string.punctuation)
    text_without_punctuation = text.translate(translator)
    return text_without_punctuation.lower()

def treebank_word_tokenizer(sentence):
    """
    This function takes a sentence as input, 
    tokenizes it using Treebank Word Tokenizer, 
    and then lemmatizes each token using WordNetLemmatizer.

    Args:
        sentence (str): The input sentence to be tokenized and lemmatized.

    Returns:
        list: A list of lemmatized tokens extracted from the input sentence.

    """
    tokenizer = TreebankWordTokenizer()
    lemmatizer = WordNetLemmatizer()

    # Tokenize the sentence
    tokens = tokenizer.tokenize(sentence)

    # Lemmatize each token
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return lemmatized_tokens

try:
    with EmissionsTracker(project_name="Train_B_Emission",
                          output_file="output_codecarbon/output_train_b.csv") as tracker:
        vector_no_lemma = CountVectorizer(tokenizer = treebank_word_tokenizer, ngram_range=(1,2))
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        dft = read_csv('../../data/Raw/train_category.csv')
        x1_train = dft['text']
        y1_train = dft['label_category']
        dft.set_index('ID')
        print("TRAIN: \n", y1_train.value_counts(), end="\n\n")
        classifier = svm.LinearSVC(max_iter = 10000, class_weight= 'balanced', C=0.2)
        # Create the pipeline
        pipe_category = Pipeline([("cleaner", Predictors()),
        ('vectorizer', vector_no_lemma),
        ('classifier', classifier)])

        pipe_category.fit(x1_train, y1_train)
        with open('../../models/train_b.pkl', 'wb') as file_train_b:
            pickle.dump(pipe_category, file_train_b)

except pynvml.NVMLError as e:
    if e.value == pynvml.NVMLError_NotSupported:
        print("Attenzione: Il monitoraggio delle emissioni non è supportato sulla tua GPU.")
    else:
        print(f"Errore sconosciuto di pynvml: {e}")
