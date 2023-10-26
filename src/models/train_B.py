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
mlflow.start_run(run_name="Experiment_3_TaskB")

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

#vector that uses TreebankWordTokenizer without lemmatization
vector_no_lemma = CountVectorizer(tokenizer = TreebankWordTokenizer().tokenize, ngram_range=(1,2))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
dft = read_csv('../../data/Raw/train_category.csv')
x1_train = dft['text']
y1_train = dft['label_category']
dft.set_index('ID')
print("TRAIN: \n", y1_train.value_counts(), end="\n\n")
    
mlflow.log_param("max_iter", 10000)
mlflow.log_param("class_weight", 'balanced')
mlflow.log_param("C", 0.4)   
classifier = svm.LinearSVC(max_iter = 10000, class_weight= 'balanced', C=0.4)

# Create the pipeline
pipe_category = Pipeline([("cleaner", predictors()),
('vectorizer', vector_no_lemma),
('classifier', classifier)])

pipe_category.fit(x1_train, y1_train)
pickle.dump(pipe_category, open('../../models/train_B.pkl', 'wb'))
