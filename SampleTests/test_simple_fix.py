import pytest


@pytest.fixture
def input_value():
    return "python"


# Uppercase
def test_upper(input_value):
    assert input_value.upper() == "PYTHON"


# Length of a string
def test_len(input_value):
    assert len(input_value) == 6


# Is Alpha
def test_isalpha(input_value):
    assert input_value.isalpha() == True


# Palindrome
def test_ispalindrome(input_value):
    assert input_value == input_value[::-1]
