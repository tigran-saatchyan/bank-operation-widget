from bank_operation_widget.utils import filter_executed_operations, \
    get_operation_data, load_data_from_file, print_operation


def display_recent_operations():
    data = load_data_from_file()
    operations = filter_executed_operations(data)
    recent_operations = operations[:5]

    for operation in recent_operations:
        operation_data = get_operation_data(operation)

        print_operation(operation_data)


display_recent_operations()
