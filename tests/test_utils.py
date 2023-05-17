# test_utils.py

import sys
from io import StringIO

import pytest

from bank_operation_widget.utils import filter_executed_operations, \
    get_operation_data, load_data_from_file, mask_account_number, \
    mask_card_or_account_number, mask_credit_card_number, print_operation


def test_load_data_from_file():
    data = load_data_from_file()

    assert isinstance(data, list), "Data should be loaded as a list"
    assert isinstance(data[0], dict), "List must contain dictionaries"
    assert len(data) > 0, "Data should not be empty"


def test_filter_executed_operations(json_test_data):
    result = filter_executed_operations(json_test_data)
    assert len(result) == 3, "Expected 3 executed operations"
    assert result[0][
               'date'] == '2022-04-01', "First operation should have the latest date"
    assert result[1][
               'date'] == '2022-03-01', "Second operation should have the second-latest date"
    assert result[2][
               'date'] == '2022-01-01', "Third operation should have the oldest date"


def test_mask_credit_card_number():
    # Test masking a credit card number
    card_number = '1234567812345678'
    masked_number = mask_credit_card_number(card_number)
    assert masked_number == '1234 56** **** 5678', "Credit card number should be masked correctly"


def test_mask_account_number():
    # Test masking an account number
    account_number = '1234567890'
    masked_number = mask_account_number(account_number)
    assert masked_number == '**7890', "Account number should be masked correctly"


@pytest.mark.parametrize(
    "card_number, expected, error_message", [
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
)
def test_mask_card_or_account_number(card_number, expected, error_message):

    masked_number = mask_card_or_account_number(card_number)
    assert masked_number == expected, error_message


def test_get_operation_data():
    # Sample operation data for testing
    operation = {
        'from': 'Credit Card Number 1234567812345678',
        'to': 'Счет 1234567812345678',
        'date': '2022-01-01T10:00:00',
        'description': 'Test Operation',
        'operationAmount': {
            'amount': 100.0,
            'currency': {
                'name': 'USD'
            }
        }
    }

    # Call the function to get operation data
    operation_data = get_operation_data(operation)

    # Check if operation data is retrieved correctly
    assert operation_data[
               'date'] == '2022-01-01', "Date should be retrieved correctly"
    assert operation_data[
               'description'] == 'Test Operation', "Description should be retrieved correctly"
    assert operation_data[
               'amount'] == 100.0, "Amount should be retrieved correctly"
    assert operation_data[
               'currency'] == 'USD', "Currency should be retrieved correctly"
    assert operation_data[
               'masked_from_account'] == 'Credit Card Number 1234 56** **** 5678 -> ', "From account should be masked correctly"
    assert operation_data[
               'masked_to_account'] == 'Счет **5678', "To account should be masked correctly"

    operation = {
        'to': 'Счет 1234567812345678',
        'date': '2022-01-01T10:00:00',
        'description': 'Test Operation',
        'operationAmount': {
            'amount': 100.0,
            'currency': {
                'name': 'USD'
            }
        }
    }

    # Call the function to get operation data
    operation_data = get_operation_data(operation)

    # Check if operation data is retrieved correctly
    assert operation_data[
               'date'
           ] == '2022-01-01', "Date should be retrieved correctly"
    assert operation_data[
               'description'
           ] == 'Test Operation', "Description should be retrieved correctly"
    assert operation_data[
               'amount'
           ] == 100.0, "Amount should be retrieved correctly"
    assert operation_data[
               'currency'
           ] == 'USD', "Currency should be retrieved correctly"
    assert operation_data[
               'masked_from_account'
           ] == '', "From account should be masked correctly"
    assert operation_data[
               'masked_to_account'
           ] == 'Счет **5678', "To account should be masked correctly"


def test_print_operation():
    # Create a sample operation data
    operation_data = {
        "date": "2022-01-01",
        "description": "Sample Operation",
        "masked_from_account": "**** **** **** 1234 -> ",
        "masked_to_account": "**5678",
        "amount": 100.0,
        "currency": "USD"
    }

    # Use sys.stdout to capture the output
    captured_stdout = StringIO()
    sys.stdout = captured_stdout

    # Call the function to print the operation data
    print_operation(operation_data)

    # Get the printed output
    printed_output = captured_stdout.getvalue()

    # Restore sys.stdout
    sys.stdout = sys.__stdout__

    # Check if the expected output is correct
    expected_output = """2022-01-01 Sample Operation
**** **** **** 1234 -> **5678
100.0 USD

"""
    assert printed_output == expected_output
