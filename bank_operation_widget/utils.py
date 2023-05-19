""" Utils module"""

import json
import os
from datetime import datetime
from typing import Any


def load_data_from_file() -> dict:
    """
    Load data from a file.

    :return: The loaded data.
    :rtype: dict
    """
    file_path: str = os.path.join(os.path.dirname(__file__), 'operations.json')
    with open(file_path, 'r', encoding="UTF-8") as file:
        data: dict = json.load(file)
    return data


def filter_executed_operations(data: dict) -> list[dict]:
    """
    Filter executed operations from the data.

    :param data: The data containing operations.
    :type data: dict
    :return: The filtered executed operations.
    :rtype: list
    """
    operations: list[Any] = sorted(
        (operation for operation in data
         if operation.get('state', 'CANCELED') == 'EXECUTED'),
        key=lambda operation: operation['date'],
        reverse=True
    )
    return operations


def mask_credit_card_number(card_number: str) -> str:
    """
    Mask a credit card number.

    :param card_number: The credit card number.
    :type card_number: str
    :return: The masked credit card number.
    :rtype: str
    """
    return f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'


def mask_account_number(account_number: str) -> str:
    """
    Mask an account number.

    :param account_number: The account number.
    :type account_number: str
    :return: The masked account number.
    :rtype: str
    """
    return f'**{account_number[-4:]}'


def mask_card_or_account_number(account_number: str) -> str:
    """
    Determine whether the account number is a credit card or account number,
    and mask it accordingly.

    :param account_number: The account number.
    :type account_number: str
    :return: The masked account number.
    :rtype: str
    """
    name: str
    number: str
    name, number = account_number.rsplit(' ', 1)
    is_account: bool = "счет" in name.lower()
    masked_number: str = mask_account_number(
        number
    ) if is_account else mask_credit_card_number(number)

    return ' '.join([name, masked_number])


def date_format_converter(date_string) -> str:
    """
    Convert a date string from the format "%Y-%m-%dT%H:%M:%S.%f" to
    "DD.MM.YYYY".

    :param date_string: The input date string
    :type date_string: str
    :return: The converted date string in the format "DD.MM.YYYY".
    :rtype: str
    """
    datetime_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    return datetime_obj.strftime("%d.%m.%Y")


def get_operation_data(operation: dict) -> dict:
    """
    Get operation data.

    :param operation: The operation.
    :type operation: dict
    :return: The operation data.
    :rtype: dict
    """
    from_account: str = operation.get('from', '')
    to_account: str = operation['to']

    operation_data = {
        "date": date_format_converter(operation['date']),
        "description": operation['description'],
        "amount": operation['operationAmount']['amount'],
        "currency": operation['operationAmount']['currency']['name']
    }

    if from_account:
        operation_data[
            "masked_from_account"
        ] = mask_card_or_account_number(from_account) + " -> "
    else:
        operation_data["masked_from_account"] = ""

    operation_data[
        "masked_to_account"
    ] = mask_card_or_account_number(to_account)

    return operation_data


def print_operation(operation_data: dict):
    """
    Print operation details.

    :param operation_data: The operation data.
    :type operation_data: dict
    """
    print(f'{operation_data["date"]} {operation_data["description"]}')
    print(
        f'{operation_data["masked_from_account"]}'
        f'{operation_data["masked_to_account"]}'
    )
    print(f'{operation_data["amount"]} {operation_data["currency"]}\n')
