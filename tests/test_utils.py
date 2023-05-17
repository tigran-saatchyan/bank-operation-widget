""" Tests for utils module """

import sys
from io import StringIO

import pytest

from bank_operation_widget.utils import filter_executed_operations, \
    get_operation_data, load_data_from_file, mask_account_number, \
    mask_card_or_account_number, mask_credit_card_number, print_operation
from tests.conftest import GET_OPERATION_DATA, MASK_CARD_OR_ACCOUNT_NUMBER, \
    OPERATION_DATA


def test_load_data_from_file():
    """
    Test the load_data_from_file() function.

    Ensure that the data is loaded correctly and has the expected format.
    """
    data = load_data_from_file()

    assert isinstance(data, list), "Data should be loaded as a list"
    assert isinstance(data[0], dict), "List must contain dictionaries"
    assert len(data) > 0, "Data should not be empty"


def test_filter_executed_operations(json_test_data):
    """
    Test the filter_executed_operations() function.

    Ensure that executed operations are filtered correctly.
    """
    result = filter_executed_operations(json_test_data)
    assert len(result) == 3, "Expected 3 executed operations"
    assert result[0]['date'] == '2022-04-01', "First operation should have " \
                                              "the latest date"
    assert result[1]['date'] == '2022-03-01', "Second operation should have " \
                                              "the second-latest date"
    assert result[2]['date'] == '2022-01-01', "Third operation should have " \
                                              "the oldest date"


def test_mask_credit_card_number(card_num_sample):
    """
    Test the mask_credit_card_number() function.

    Ensure that a credit card number is masked correctly.
    """
    masked_number = mask_credit_card_number(card_num_sample)
    assert masked_number == '1234 56** **** 5678', "Credit card number " \
                                                   "should be masked correctly"


def test_mask_account_number(account_num_sample):
    """
    Test the mask_account_number() function.

    Ensure that an account number is masked correctly.
    """
    masked_number = mask_account_number(account_num_sample)
    assert masked_number == '**7890', "Account number should be masked " \
                                      "correctly"


@pytest.mark.parametrize(
    "card_number, expected, error_message", MASK_CARD_OR_ACCOUNT_NUMBER
)
def test_mask_card_or_account_number(card_number, expected, error_message):
    """
    Test the mask_card_or_account_number() function.

    Ensure that card or account numbers are masked correctly based on the name.
    """
    masked_number = mask_card_or_account_number(card_number)
    assert masked_number == expected, error_message


@pytest.mark.parametrize(
    "operation, expected, error_message", GET_OPERATION_DATA
)
def test_get_operation_data(operation, expected, error_message):
    """
    Test the get_operation_data() function.

    Ensure that operation data is retrieved correctly.
    """
    operation_data = get_operation_data(operation)

    for i, arg in enumerate(operation_data.items()):
        assert arg[1] == expected[arg[0]], error_message[i]


def test_print_operation():
    """
    Test the print_operation() function.

    Ensure that the operation details are printed correctly.
    """
    captured_stdout = StringIO()
    sys.stdout = captured_stdout
    print_operation(OPERATION_DATA)

    printed_output = captured_stdout.getvalue()
    sys.stdout = sys.__stdout__

    expected_output = """2022-01-01 Test Operation
Credit Card Number 1234 56** **** 5678 -> Счет **5678
475 USD

"""
    assert printed_output == expected_output
