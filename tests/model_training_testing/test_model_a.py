import pytest
from validation_a import pipe_sexism,evaluation_metrics
from pandas import read_csv

VALUE = 0.70
 
class TestSexismClassifier:

    # Esempi di test per il modello NLP
    def test_non_sexist_message(self):
        # Test per un messaggio non sessista
        message = "Then, she's a keeper"
        predicted_label = pipe_sexism.predict([message])[0]
        assert predicted_label == "not sexist"
    
    def test_sexist_message(self):
        # Test per un messaggio sessista
        message = "I did. You have to have the bravery to escalate, touch her boobs etc, and work on escalating it further"
        predicted_label = pipe_sexism.predict([message])[0]
        assert predicted_label == "sexist"
    
    def test_empty_message(self):
        # Test per un messaggio vuoto
        message = ""
        predicted_label = pipe_sexism.predict([message])[0]
        assert predicted_label == "not sexist"  # Sostituisci con il comportamento desiderato
    
    def test_evaluation_metrics(self):
        dfs = read_csv('../../data/Raw/test_sexist.csv')

        x_test = dfs['text']
        y_test= dfs['label_sexist']
        dfs.set_index('ID')
    
        precision, recall, f1 = evaluation_metrics(x_test, y_test, pipe_sexism)
    
        # Assicurati di adattare i valori attesi in base ai tuoi dati di test
        assert precision > VALUE
        assert recall > VALUE
        assert f1 > VALUE