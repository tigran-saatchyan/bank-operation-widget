from unittest.mock import call, patch

from bank_operation_widget.app import display_recent_operations


@patch('bank_operation_widget.app.load_data_from_file')
@patch('bank_operation_widget.app.filter_executed_operations')
@patch('bank_operation_widget.app.get_operation_data')
@patch('bank_operation_widget.app.print_operation')
def test_display_recent_operations(
    mock_print_operation,
    mock_get_operation_data,
    mock_filter_executed_operations,
    mock_load_data_from_file,
    mock_data,
    mock_operations,
    mock_operation_data
):
    data = mock_data
    operations = mock_operations
    operation_data = mock_operation_data

    mock_load_data_from_file.return_value = data
    mock_filter_executed_operations.return_value = operations
    mock_get_operation_data.side_effect = lambda operation: operation_data

    # Call the function
    display_recent_operations()

    # Assert that the expected calls were made
    assert mock_load_data_from_file.called
    assert mock_filter_executed_operations.called

    expected_calls = [
        call(mock_operations[0]),
        call(mock_operations[1]),
        call(mock_operations[2]),
        call(mock_operations[3])
    ]
    assert mock_get_operation_data.call_args_list == expected_calls

    expected_print_calls = [
        call(mock_operation_data)
    ]
    assert mock_print_operation.call_args_list[0] == expected_print_calls[0]
