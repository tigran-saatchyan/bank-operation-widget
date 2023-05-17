import pytest

OPERATION_DATA = {
    "date": "2022-01-01",
    "description": 'Test Operation',
    "amount": "475",
    "currency": 'USD',
    "masked_from_account": 'Credit Card Number 1234 56** **** '
                           '5678 -> ',
    "masked_to_account": 'Счет **5678'
}

GET_OPERATION_DATA = [
    (
        {
            'from': 'Credit Card Number 1234567812345678',
            'to': 'Счет 1234567812345678',
            'date': '2022-01-01T10:00:00',
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
            'date': '2022-03-01T10:00:00',
            'description': 'Открытие вклада',
            'operationAmount': {
                'amount': "5478",
                'currency': {
                    'name': 'руб.'
                }
            }
        },
        {
            "date": "2022-03-01",
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
    return [
        {'state': 'EXECUTED', 'date': '2022-01-01'},
        {'state': 'CANCELED', 'date': '2022-02-01'},
        {'state': 'EXECUTED', 'date': '2022-03-01'},
        {'state': 'EXECUTED', 'date': '2022-04-01'}
    ]


@pytest.fixture()
def card_num_sample():
    return '1234567812345678'


@pytest.fixture()
def account_num_sample():
    return '1234567812345678'


@pytest.fixture()
def mock_data():
    return [
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


@pytest.fixture()
def mock_operations():
    return [
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


@pytest.fixture()
def mock_operation_data():
    return [
        {
            "date": "2019-08-26",
            "description": "Перевод организации",
            "masked_from_account": "Maestro 1596 83** **** 5199 -> ",
            "masked_to_account": "Счет **9589",
            "amount": "31957.58",
            "currency": "руб."
        },
        {
            "date": "2019-07-03",
            "description": "Перевод организации",
            "masked_from_account": "MasterCard 7158 30** **** 6758 -> ",
            "masked_to_account": "Счет **5560",
            "amount": "8221.37",
            "currency": "USD"
        },
        {
            "date": "2018-03-23",
            "description": "Открытие вклада",
            "masked_from_account": "",
            "masked_to_account": "Счет **2431",
            "amount": "48223.05",
            "currency": "руб."
        },
        {
            "date": "2018-02-23",
            "description": "Открытие вклада",
            "masked_from_account": "",
            "masked_to_account": "Счет **2431",
            "amount": "48223.05",
            "currency": "руб."
        }
    ]
