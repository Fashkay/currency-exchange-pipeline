# Implementation Details

This section provides an in-depth overview of the implementation details of the Data Acquisition and Preprocessing Pipeline.

## Data Acquisition

The data acquisition process involves retrieving currency exchange rate data from the [Exchange Rates API](https://api.exchangeratesapi.io/v1/latest) using a Python script. The following steps outline the implementation:

1. **API Endpoint and Parameters**:
   - The API endpoint `https://api.exchangeratesapi.io/v1/latest` is used to fetch the latest exchange rates.
   - The base currency is set to USD, and the target currency is set to EUR.

2. **Authentication**:
   - An API key is provided as part of the request headers for authentication.

3. **HTTP Request**:
   - The `requests` library is used to send an HTTP GET request to the API endpoint.

4. **Response Handling**:
   - The response is checked for a status code of 200 to ensure a successful request.
   - The JSON response is parsed to extract the exchange rate.

## Preprocessing and Transformation

The preprocessing step involves normalizing the exchange rate data to two decimal places. This ensures consistency and accuracy in the stored data.

The `preprocessing.py` module contains a `normalize_exchange_rate()` function, which takes the raw exchange rate as input and returns the normalized value.

## Database Integration

The data acquired and preprocessed is then integrated into a PostgreSQL database. The `database_integration.py` module provides functions for creating the necessary table and inserting the data.

1. **Database Connection**:
   - The module establishes a connection to the PostgreSQL database using the provided credentials.

2. **Table Creation**:
   - The `create_exchange_rates_table()` function creates the `exchange_rates` table if it does not already exist.

3. **Data Insertion**:
   - The `insert_exchange_rate()` function inserts exchange rate data into the table.

## Demonstration Script

The `demo.py` script showcases the complete pipeline by orchestrating the data acquisition, preprocessing, and database integration steps.

## SQL Scripts

The project includes SQL scripts for creating the database schema (`create_schema.sql`), inserting sample data (`insert_data.sql`), and managing the database (`manage_database.sql`).

---

This section provides a detailed explanation of how each component of the Data Acquisition and Preprocessing Pipeline is implemented. It covers the processes of data acquisition, preprocessing, database integration, and includes a demonstration script along with accompanying SQL scripts.
