import pytest
from src.models.validation_b import pipe_category

def test_invariance_category():
    tokens = ["get","obtain"]
    messages = [f"I didn't actually {token} a day without women, and I'm a little disappointed." 
                for token in tokens]
    for message in messages:
        predicted_label = pipe_category.predict([message])[0]
        assert predicted_label == "2. derogation"

if __name__ == "__main__":
    pytest.main()