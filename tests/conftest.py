import pytest
from datetime import datetime

@pytest.fixture
def sample_card_numbers():
    """Фикстура с тестовыми номерами карт."""
    return ["1234567890123456", "4000008000000000", "5555444433332222"]

@pytest.fixture
def sample_account_numbers():
    """Фикстура с тестовыми номерами счетов."""
    return ["73654108430135874305", "64686473678894779589", "35383033474447895560"]

@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми транзакциями."""
    return [
        {
            'id': '441945886',
            'state': 'EXECUTED',
            'date': '2019-08-26T10:50:58.294041',
            'amount': '31957.58',
            'currency': 'руб.'
        },
        {
            'id': '41428829',
            'state': 'CANCELED',
            'date': '2019-07-03T18:35:29.512364',
            'amount': '8099.03',
            'currency': 'руб.'
        },
        {
            'id': '939719570',
            'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572',
            'amount': '9533.75',
            'currency': 'руб.'
        }
    ]

@pytest.fixture
def invalid_transactions():
    """Фикстура с транзакциями, содержащими некорректные даты."""
    return [
        {'id': '1', 'state': 'EXECUTED', 'date': 'invalid-date'},
        {'id': '2', 'state': 'CANCELED', 'date': ''},
        {'id': '3', 'state': 'EXECUTED'}
    ]
