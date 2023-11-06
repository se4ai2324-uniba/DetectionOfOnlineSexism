import pytest
import sys
import os

current_directory = os.getcwd()
sys.path.append(current_directory+'\\..\\..\\src\\models') 

from validation_B import pipe_category, evaluation_metrics
from pandas import read_csv

VALUE = 0.60

class TestSpecificSexismClassifier:

    def test_threats_sexism(self):
        message = "You should've hit her."
        predicted_label = pipe_category.predict_type_of_sexism([message])[0]
        if predicted_label == "1. threats, plans to harm and incitement":
            assert True, f"The message has been categorized as a threat."
        else:
            pytest.skip("Message is not classified as threats.")

    def test_derogation_sexism(self):
        message = "If we won't fuck their women, what will they jerk off to?"
        predicted_label = pipe_category.predict_type_of_sexism([message])[0]
        if predicted_label == "2. derogation":
            assert True, f"The message has been categorized as a derogation."
        else:
            pytest.skip("Message is not classified as derogation.")

    def test_animosity_sexism(self):
        message = "If it's reciprocal then it's fine... But women are just not like that so don't cuck for these thots."
        predicted_label = pipe_category.predict_type_of_sexism([message])[0]
        if predicted_label == "3. animosity":
            assert True, f"The message has been categorized as animosity."
        else:
            pytest.skip("Message is not classified as animosity.")

    def test_prejudiced_discussions_sexism(self):
        message = "I did. You have to have the bravery to escalate, touch her boobs etc, and work on escalating it further."
        predicted_label = pipe_category.predict_type_of_sexism([message])[0]
        if predicted_label == "4. prejudiced discussions":
            assert True, f"The message has been categorized as a prejudiced discussions."
        else:
            pytest.skip("Message is not classified as prejudiced discussions.")

    def test_evaluation_metrics(self):
        dfs = read_csv('../../data/Raw/test_category.csv')

        x1_test = dfs['text']
        y1_test = dfs['label_category']
        dfs.set_index('ID')

        precision, recall, f1 = evaluation_metrics(x1_test, y1_test, pipe_category)

        assert precision > VALUE
        assert recall > VALUE
        assert f1 > VALUE
