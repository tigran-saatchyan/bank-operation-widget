import json
import os


def load_data_from_file():
    file_path = os.path.join(
        os.path.dirname(__file__), 'operations.json'
    )
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def filter_executed_operations(data):
    operations = sorted(
        (operation for operation in data if
         operation.get('state', 'CANCELED') == 'EXECUTED'),
        key=lambda operation: operation['date'],
        reverse=True
    )
    return operations


def mask_credit_card_number(card_number):
    return '{} {}** **** {}'.format(
        card_number[:4], card_number[4:6], card_number[-4:]
    )


def mask_account_number(account_number):
    return '**{}'.format(account_number[-4:])


def mask_card_or_account_number(account_number):
    name, number = account_number.rsplit(' ', 1)
    is_account = "счет" in name.lower()
    masked_number = mask_account_number(number) \
        if is_account else mask_credit_card_number(number)

    return ' '.join([name, masked_number])


def get_operation_data(operation):
    from_account = operation.get('from', '')
    to_account = operation['to']

    operation_data = {
        "date": operation['date'].split('T')[0],
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

    operation_data.update()
    return operation_data


def print_operation(operation_data):
    print(f'{operation_data["date"]} {operation_data["description"]}')
    print(
        f'{operation_data["masked_from_account"]}'
        f'{operation_data["masked_to_account"]}'
    )
    print(f'{operation_data["amount"]} {operation_data["currency"]}\n')
