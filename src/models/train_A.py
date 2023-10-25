import string
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from pandas import read_csv
import nltk
import os
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer
import pickle
import dagshub
import mlflow

dagshub.init("DetectionOfOnlineSexism", "se4ai2324-uniba", mlflow=True)

n_cpu = os.cpu_count()
print("Number of CPUs in the system:", n_cpu)

#init spaCy
punctuations = string.punctuation

# Custom transformer using spaCy
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        # Cleaning Text
        return [clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}

# Basic function to clean the text
def clean_text(text):
    # Removing spaces and converting text into lowercase
    translator = str.maketrans("", "", string.punctuation)
    text_without_punctuation = text.translate(translator)
    return text_without_punctuation.lower()
    #return text.strip().lower()

def treebankWordTokenizer(sentence):

    tokenizer = TreebankWordTokenizer()
    lemmatizer = WordNetLemmatizer()

    # Tokenize the sentence
    tokens = tokenizer.tokenize(sentence)

    # Lemmatize each token
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return lemmatized_tokens

nltk.download('wordnet')
nltk.download('omw-1.4')

vector = CountVectorizer(tokenizer = treebankWordTokenizer, ngram_range=(1,2))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
dft = read_csv('../../data/Raw/train_sexist.csv')
x_train = dft['text']
y_train = dft['label_sexist']
dft.set_index('ID')
print("TRAIN: \n", y_train.value_counts(), end="\n\n")
    
classifier = svm.LinearSVC(max_iter = 10000, class_weight= {"not sexist": 0.2, "sexist": 1})

# Create the pipeline

pipe_sexism = Pipeline([("cleaner", predictors()),
('vectorizer', vector),
('classifier', classifier)])

pipe_sexism.fit(x_train, y_train)

pickle.dump(pipe_sexism, open('../../models/train_A.pkl', 'wb'))
