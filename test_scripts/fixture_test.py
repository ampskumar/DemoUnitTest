import pytest


'''
Hey Julia, a fixture’s scope defines how many times a fixture will be invoked and a Fixture can have 4 Scopes:

Module: If the Module scope is defined, the fixture will be created/invoked only once per module.

Class: With Class scope, one fixture will be created per class object.

Session: With the Session scope, the fixture will be created only once for entire test session.
 This is mainly used to manage Webdriver sessions.

Function: This is the default value for fixture scope and the fixture is executed/run once per test session.
'''
class Fruit:
    def __init__(self, name):
        self.name = name

    # def __eq__(self, other):
    #     return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket