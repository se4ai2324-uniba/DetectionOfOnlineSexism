import string
from train_A import clean_text


def test_clean_text():

    #Basic test case with punctuation and mixed case
    input_text = "Then, she's a keeper"
    expected_output = "then she's a keeper"
    assert clean_text(input_text) == expected_output

    #Test with only lowercase text
    input_text = "if youre hyping up your nintendo switch to women, then its already so over lmfao"
    expected_output = "if youre hyping up your nintendo switch to women then its already so over lmfao"
    assert clean_text(input_text) == expected_output

    #Test with only uppercase text
    input_text = "OR..........[USER] WE COULD MAKE IT A TRIPLE THREAT MATCH WITH [USER] BLISS VS [USER] VS [USER] McMAHON. BUT AS MUCH AS WE'D LIKE TO SEE [USER] VS [USER] AT [USER], I THINK THE [USER] UNIVERSE IS CRAAAAAAVVVVVVINNNNNGGGGG!!!"
    expected_output = "or..........user we could make it a triple threat with user bliss vs user vs user mcmahon but as much as we'd like to see user vs user at user i think the user universe is craaaaaavvvvvvinnnnnggggg"
    assert clean_text(input_text) == expected_output

    #Test with empty input
    input_text = ""
    expected_output = ""
    assert clean_text(input_text) == expected_output

    #Test with a mix of text and numbers
    input_text = "Goddam that Stormer article on women shutting the f up is going to hit 6,000,000 comments before midnight"
    expected_output = "goddam that stormer article on women shutting the f up is going to hit 6000000 comments before midnight"
    assert clean_text(input_text) == expected_output

    print("All test cases pass")

if __name__ == "__main__":
    test_clean_text()
