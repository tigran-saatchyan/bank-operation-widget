import pytest


@pytest.fixture()
def json_test_data():
    return [
        {'state': 'EXECUTED', 'date': '2022-01-01'},
        {'state': 'CANCELED', 'date': '2022-02-01'},
        {'state': 'EXECUTED', 'date': '2022-03-01'},
        {'state': 'EXECUTED', 'date': '2022-04-01'}
    ]
