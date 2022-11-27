import pytest
vegetables = []


@pytest.fixture()
def cauliflower():
    vegetables.append("cauliflower")


@pytest.fixture(autouse=True)
def potato():
    vegetables.append("potato")


@pytest.fixture()
def onion():
    vegetables.append("onion")


def test_vegetables_order(cauliflower):
    assert vegetables[0] == "potato"
    # assert vegetables == ["onion", "potato", "cauliflower"]
