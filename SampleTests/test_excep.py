import pytest


def validate_age(age):
    if age < 0:
        raise ValueError("Age can not be less than zero")


# Even after handling, still testcase shown as failure
def test_validate_age():
    validate_age(-1)


# above will fail the testcase, to b able to pass handle as follows
def test_handle_excep_to_pass_1():
    with pytest.raises(ValueError):
        validate_age(-1)
        # validate_age(3)  # again fails saying did not raise value error


def test_handle_excep_2():
    with pytest.raises(ValueError) as exc_info:
        validate_age(-1)
    print(str(exc_info.value))
    assert str(exc_info.value) == "Age can not be less than zero"


def test_handle_excep_3():
    with pytest.raises(ValueError, "Age can not be less than zero"):
        validate_age(-1)

