""" Tests for App module """

from unittest.mock import call, patch

from bank_operation_widget.app import display_recent_operations
from tests.conftest import MOCK_DATA, MOCK_OPERATIONS, MOCK_OPERATION_DATA


@patch('bank_operation_widget.app.load_data_from_file')
@patch('bank_operation_widget.app.filter_executed_operations')
@patch('bank_operation_widget.app.get_operation_data')
@patch('bank_operation_widget.app.print_operation')
def test_display_recent_operations(
    mock_print_operation,
    mock_get_operation_data,
    mock_filter_executed_operations,
    mock_load_data_from_file,
):
    """
    Test the display_recent_operations() function.

    Ensure that the function calls the expected methods
    and makes the expected calls.
    """
    data = MOCK_DATA
    operations = MOCK_OPERATIONS
    operation_data = MOCK_OPERATION_DATA

    mock_load_data_from_file.return_value = data
    mock_filter_executed_operations.return_value = operations
    mock_get_operation_data.side_effect = lambda operation: operation_data

    display_recent_operations()

    assert mock_load_data_from_file.called
    assert mock_filter_executed_operations.called

    expected_calls = [
        call(operations[0]),
        call(operations[1]),
        call(operations[2]),
        call(operations[3])
    ]
    assert mock_get_operation_data.call_args_list == expected_calls

    expected_print_calls = [
        call(operation_data)
    ]
    assert mock_print_operation.call_args_list[0] == expected_print_calls[0]
