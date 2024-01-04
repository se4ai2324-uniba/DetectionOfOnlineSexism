"""
Module: test_preprocessing
Description: This module contains functions for doing
preprocessing tests
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
import pytest
from src.models.train_a import clean_text

def test_clean_text_punctuation():
    """
    Module: test_clean_text_punctuation
    Description: This basic test case validates that
    the clean_text function removes punctuation and
    converts text to lowercase. The input text
    "Then, she's a keeper" is expected to be transformed
    into "then shes a keeper."
    """
    #Basic test case with punctuation and mixed case
    input_text = "Then, she's a keeper"
    expected_output = "then shes a keeper"
    assert clean_text(input_text) == expected_output

def test_clean_text_uppercase():
    """
    Module: test_clean_text_uppercase
    Description: This test case verifies that the clean_text
    function correctly processes uppercase text,
    removing punctuation and converting it to lowercase.
    The input text with uppercase and symbols is expected to be
    transformed accordingly. 
    """
    #Test with only uppercase text
    input_text = "[USER] WE COULD MAKE IT A TRIPLE THREAT MATCH WITH "\
        "[USER] BLISS VS [USER] VS [USER] McMAHON. BUT AS MUCH AS WE'D "\
            "LIKE TO SEE [USER] VS [USER] AT [USER], I THINK THE [USER] "\
                "UNIVERSE IS CRAAAAAAVVVVVVINNNNNGGGGG!!!"
    expected_output = "user we could make it a triple threat match with "\
        "user bliss vs user vs user mcmahon but as much as wed like to see "\
            "user vs user at user i think the user universe is "\
                "craaaaaavvvvvvinnnnnggggg "
    assert clean_text(input_text) == expected_output

def test_clean_text_empty():
    """
    Module:test_clean_text_empty
    Description: This test case ensures that the clean_text function
    handles an empty input string appropriately, returning an empty
    string as the expected output.
    """
    #Test with empty input
    input_text = ""
    expected_output = ""
    assert clean_text(input_text) == expected_output

def test_clean_text_mix_text():
    """
    Module:test_clean_text_mix_text
    Description: This test case checks if the clean_text function
    correctly processes a specific input text, removing spaces and
    converting the numbers. The expected output is the cleaned version
    of the input text. If the assertion passes, it prints "All test cases pass."
    """
    #Test with a mix of text and numbers
    input_text = "Goddam that Stormer article on women shutting the "\
        "f up is going to hit 6,000,000 comments before midnight "
    expected_output = "goddam that stormer article on women shutting the f "\
        "up is going to hit 6000000 comments before midnight"
    assert clean_text(input_text) == expected_output

    print("All test cases pass")

if __name__ == "__main__":
    pytest.main()
