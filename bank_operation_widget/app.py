import json


def display_recent_operations():
    # Загрузка данных из файла JSON
    with open('operations.json', 'r') as file:
        data = json.load(file)

    # Отфильтровать и отсортировать операции по дате
    operations = sorted(
        (operation for operation in data if
         operation.get('state', 'CANCELED') == 'EXECUTED'),
        key=lambda operation: operation['date'],
        reverse=True
    )

    # Получить последние 5 операций
    recent_operations = operations[:5]

    # Вывести операции в заданном формате
    for operation in recent_operations:
        date = operation['date'].split('T')[0]
        description = operation['description']
        from_account = operation.get('from', '')
        to_account = operation['to']
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        if from_account:

            from_account_name, from_account_number = from_account.rsplit(
                ' ', 1
            )
            is_account = "счет" in from_account_name.lower()
            if is_account:
                masked_number = '**{}'.format(from_account_number[-4:])
                masked_from_account = ' '.join(
                    [
                        from_account_name,
                        masked_number,
                        "-> "
                    ]
                )
            else:
                masked_number = '{} {}** **** {}'.format(
                    from_account_number[:4],
                    from_account_number[4:6],
                    from_account_number[-4:]
                )
                masked_from_account = ' '.join(
                    [
                        from_account_name,
                        masked_number,
                        "-> "
                    ]
                )
        else:
            masked_from_account = ""

        to_account_name, to_account_number = to_account.rsplit(' ', 1)
        is_account = "счет" in to_account_name.lower()
        if is_account:
            masked_number = '**{}'.format(to_account_number[-4:])
            masked_to_account = ' '.join(
                [
                    to_account_name,
                    masked_number
                ]
            )
        else:
            masked_number = '{} {}** **** {}'.format(
                to_account_number[:4],
                to_account_number[4:6],
                to_account_number[-4:]
            )
            masked_to_account = ' '.join(
                [
                    to_account_name,
                    masked_number
                ]
            )

        print(f'{date} {description}')
        print(f'{masked_from_account}{masked_to_account}')
        print(f'{amount} {currency}\n')


display_recent_operations()
