# Implementation

## Data Acquisition Module

The Data Acquisition module (`data_acquisition.py`) is responsible for interfacing with the chosen API and retrieving currency exchange rate data. It includes the following key components:

- `get_exchange_rate(base_currency, target_currency, api_key)`: This function takes three parameters - `base_currency`, `target_currency`, and `api_key`. It constructs an API request URL with these parameters and sends a GET request to the API. If the request is successful (status code 200), it processes the JSON response and returns the exchange rate. If not, it handles the error gracefully.

## Preprocessing and Transformation Module

The Preprocessing and Transformation module (`preprocessing.py`) focuses on normalizing the acquired exchange rates and ensuring data quality. It includes the following component:

- `normalize_exchange_rate(exchange_rate)`: This function takes an `exchange_rate` as input and rounds it to a fixed number of decimal places (2 in this case). The normalized exchange rate is then returned.

## Database Integration Module

The Database Integration module (`database_integration.py`) manages interactions with the database. It includes the following components:

- Database Connection: Establishes a connection to the database using the configured credentials.
- `create_exchange_rates_table()`: Creates the `exchange_rates` table with appropriate columns (id, currency_pair, exchange_rate).
- `insert_exchange_rate(base_currency, target_currency, exchange_rate)`: Inserts a new exchange rate entry into the database.
- `get_exchange_rates()`: Retrieves all exchange rate entries from the database.

## Demonstration Script

The Demonstration Script (`demo.py`) provides a user-friendly interface for executing the pipeline. It guides users through the following steps:

1. Acquiring exchange rate data by prompting for base currency, target currency, and API key.
2. Preprocessing the acquired data by normalizing the exchange rate.
3. Storing the data in the database.

The script provides informative prompts and feedback at each step to enhance user experience.

## SQL Scripts

The `sql_scripts/` folder contains the following SQL scripts:

- `create_schema.sql`: Defines the database schema, creating the `exchange_rates` table with appropriate columns and constraints.
- `insert_data.sql`: Inserts initial exchange rate data for demonstration purposes.
- `manage_database.sql`: Placeholder script for potential future database management tasks.

## Sample Code Snippets

The `documentation/sample_code_snippets.md` file provides useful code snippets for reference and guidance in utilizing different components of the pipeline.

This section provides an overview of the implementation details for each module and component of your pipeline. It helps readers understand how the code functions and how the different pieces fit together.

Feel free to customize and expand upon this content based on your specific project details.

If you have any further questions or if there's another aspect you'd like to address, please let me know!
