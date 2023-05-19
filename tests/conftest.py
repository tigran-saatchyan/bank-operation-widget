""" Conftest module """
import pytest

OPERATION_DATA = {
    "date": "01.01.2022",
    "description": 'Test Operation',
    "amount": "475",
    "currency": 'USD',
    "masked_from_account": 'Credit Card Number 1234 56** **** 5678 -> ',
    "masked_to_account": 'Счет **5678'
}

GET_OPERATION_DATA = [
    (
        {
            'from': 'Credit Card Number 1234567812345678',
            'to': 'Счет 1234567812345678',
            'date': '2022-01-01T10:00:00.972075',
            'description': 'Test Operation',
            'operationAmount': {
                'amount': "475",
                'currency': {
                    'name': 'USD'
                }
            }
        },
        OPERATION_DATA,
        [
            "Date should be retrieved correctly",
            "Description should be retrieved correctly",
            "Amount should be retrieved correctly",
            "Currency should be retrieved correctly",
            "From account should be masked correctly",
            "To account should be masked correctly"
        ],

    ),
    (
        {
            'to': 'Счет 1234567812345678',
            'date': '2022-03-01T10:00:00.000000',
            'description': 'Открытие вклада',
            'operationAmount': {
                'amount': "5478",
                'currency': {
                    'name': 'руб.'
                }
            }
        },
        {
            "date": "01.03.2022",
            "description": 'Открытие вклада',
            "amount": "5478",
            "currency": 'руб.',
            "masked_from_account": '',
            "masked_to_account": 'Счет **5678'
        },
        [
            "Date should be retrieved correctly",
            "Description should be retrieved correctly",
            "Amount should be retrieved correctly",
            "Currency should be retrieved correctly",
            "From account should be masked correctly",
            "To account should be masked correctly"
        ]
    )
]

MASK_CARD_OR_ACCOUNT_NUMBER = [
    (
        'Credit Card Number 1234567812345678',
        'Credit Card Number 1234 56** **** 5678',
        'Credit card number should be masked correctly'),
    (
        'Счет 1234567812345678',
        'Счет **5678',
        'Account number should be masked correctly'
    )
]


@pytest.fixture()
def json_test_data():
    """
    Fixture for JSON test data.

    Returns a list of dictionaries representing test data.
    """
    return [
        {'state': 'EXECUTED', 'date': '01.01.2022'},
        {'state': 'CANCELED', 'date': '01.02.2022'},
        {'state': 'EXECUTED', 'date': '01.03.2022'},
        {'state': 'EXECUTED', 'date': '01.04.2022'}
    ]


@pytest.fixture()
def card_num_sample():
    """
    Fixture for a sample credit card number.

    Returns a sample credit card number as a string.
    """
    return '1234567812345678'


@pytest.fixture()
def account_num_sample():
    """
    Fixture for a sample account number.

    Returns a sample account number as a string.
    """
    return '1234567812345678'


MOCK_DATA = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "CANCELED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }
    ]


MOCK_OPERATIONS = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-02-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }
    ]

MOCK_OPERATION_DATA = [
        {
            "date": "26.08.2019",
            "description": "Перевод организации",
            "masked_from_account": "Maestro 1596 83** **** 5199 -> ",
            "masked_to_account": "Счет **9589",
            "amount": "31957.58",
            "currency": "руб."
        },
        {
            "date": "03.07.2019",
            "description": "Перевод организации",
            "masked_from_account": "MasterCard 7158 30** **** 6758 -> ",
            "masked_to_account": "Счет **5560",
            "amount": "8221.37",
            "currency": "USD"
        },
        {
            "date": "23.02.2018",
            "description": "Открытие вклада",
            "masked_from_account": "",
            "masked_to_account": "Счет **2431",
            "amount": "48223.05",
            "currency": "руб."
        },
        {
            "date": "23.02.2018",
            "description": "Открытие вклада",
            "masked_from_account": "",
            "masked_to_account": "Счет **2431",
            "amount": "48223.05",
            "currency": "руб."
        }
    ]
