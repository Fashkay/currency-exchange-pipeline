# Database Schema

The Currency Exchange Rate Data Acquisition and Preprocessing Pipeline uses a PostgreSQL database to store exchange rate data. The schema consists of a single table named `exchange_rates` with the following structure:

## Table: `exchange_rates`

| Column Name      | Data Type   | Description                                  |
|------------------|-------------|----------------------------------------------|
| id               | SERIAL      | Unique identifier for each exchange rate entry|
| base_currency    | VARCHAR(3)  | The base currency for conversion              |
| target_currency  | VARCHAR(3)  | The target currency for which rate is provided|
| exchange_rate    | DECIMAL(10, 6) | The exchange rate value                      |
| timestamp        | TIMESTAMP   | The timestamp when the data was acquired      |

### Description

- `id`: A unique identifier automatically generated for each exchange rate entry.

- `base_currency`: The currency being converted from (e.g., USD for US Dollar).

- `target_currency`: The currency being converted to (e.g., EUR for Euro).

- `exchange_rate`: The exchange rate value representing the conversion rate from the base currency to the target currency.

- `timestamp`: The date and time when the data was acquired.

## Indexes

- An index on the `base_currency` column for efficient retrieval of exchange rates based on the base currency.

- An index on the `target_currency` column for efficient retrieval of exchange rates based on the target currency.

## Example Data

| id | base_currency | target_currency | exchange_rate | timestamp           |
|----|---------------|----------------|--------------|---------------------|
| 1  | USD           | EUR            | 0.845678     | 2023-11-06 12:34:56 |
| 2  | USD           | GBP            | 0.750912     | 2023-11-06 12:35:02 |
| 3  | EUR           | JPY            | 133.521789   | 2023-11-06 12:36:12 |
| 4  | EUR           | USD            | 1.182345     | 2023-11-06 12:37:24 |
| 5  | GBP           | EUR            | 1.330456     | 2023-11-06 12:38:15 |

### Usage

The `exchange_rates` table is used to store and retrieve exchange rate data acquired from the API. It allows for efficient storage and retrieval of currency conversion information.



# Database Setup Instructions

Follow these steps to set up the PostgreSQL database for the Currency Exchange Rate Data Acquisition Pipeline:

1. **Install PostgreSQL**:
   - Download and install PostgreSQL from the official website.

2. **Create a New Database**:
   - Open the PostgreSQL command prompt or use a GUI tool like pgAdmin.
   - Run the following command to create a new database:
     ```
     CREATE DATABASE currency_exchange_db;
     ```

3. **Connect to the Database**:
   - Use the following command to connect to the newly created database:
     ```
     \c currency_exchange_db;
     ```

4. **Execute SQL Scripts**:
   - Run the SQL scripts provided (`create_schema.sql`, `insert_data.sql`, etc.) to set up the necessary tables and initial data.

5. **Configure Database Credentials**:
   - In the `database_integration.py` file, replace the placeholders with your actual database credentials.

6. **Ensure PostgreSQL Service is Running**:
   - Make sure the PostgreSQL service is running to enable database interactions.

