<h1 style="text-align: center; ">BANK OPERATION WIDGET</h1>

# Bank Widget Backend Data Preparation Algorithm

![alt text](https://img.shields.io/badge/Python-v3.10.6-green?style=for-the-badge&logo=appveyor "Python")
[![Pylint](https://github.com/tigran-saatchyan/bank-operation-widget/actions/workflows/pylint.yml/badge.svg)](https://github.com/tigran-saatchyan/bank-operation-widget/actions/workflows/pylint.yml)
***


This project involves the IT department of a large bank developing a new feature for the client's personal account. 
The feature is a widget that displays several recent successful banking operations performed by the client. 
Your responsibility is to implement the algorithm that prepares the data on the backend for display in the new widget.

## Features

- Fetches the necessary banking operation data for a client
- Filters out unsuccessful operations
- Sorts the operations by their timestamp in descending order
- Prepares the data for display in the widget

## Requirements

To run this project, you need:

- Backend development environment
- Access to the bank's database or API or JSON-file for retrieving client banking operation data

## Installation

1. Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/tigran-saatchyan/bank-operation-widget.git
   ```

2. Configure the necessary environment variables such as database credentials or API keys.

3. Install the required dependencies by running the following command:

   ```
   poetry install
   ```

## Usage

1. Ensure that you have properly configured the environment variables with the required credentials.

2. Run the application using the following command:

   ```
   python3 app.py
   ```

3. The backend algorithm will retrieve the client's banking operation data, filter out unsuccessful operations, sort them by timestamp in descending order, and prepare the data for display in the widget.

4. The prepared data can now be integrated into the front-end widget for display to the client.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
