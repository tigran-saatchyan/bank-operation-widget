""" Main APP module """

from bank_operation_widget.utils import filter_executed_operations, \
    get_operation_data, load_data_from_file, print_operation


def display_recent_operations():
    """
    Display the recent operations by loading data from a file,
    filtering executed operations, and printing the operation details.
    """
    data: dict = load_data_from_file()
    operations: list[dict] = filter_executed_operations(data)
    recent_operations: list[dict] = operations[:5]

    for operation in recent_operations:
        operation_data: dict = get_operation_data(operation)

        print_operation(operation_data)


if __name__ == '__main__':
    display_recent_operations()
