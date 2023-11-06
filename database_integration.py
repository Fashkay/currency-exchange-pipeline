import psycopg2

# Define database connection parameters
dbname = "your_database_name"
user = "your_database_user"
password = "your_database_password"
host = "your_database_host"
port = "your_database_port"

def create_exchange_rates_table():
    """
    Create the 'exchange_rates' table in the PostgreSQL database if it does not already exist.
    """
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cur = conn.cursor()

    # Define the SQL query to create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS exchange_rates (
        id SERIAL PRIMARY KEY,
        base_currency VARCHAR(3) NOT NULL,
        target_currency VARCHAR(3) NOT NULL,
        exchange_rate DECIMAL(10, 6) NOT NULL,
        timestamp TIMESTAMP NOT NULL
    );
    """

    cur.execute(create_table_query)
    conn.commit()

    cur.close()
    conn.close()

def insert_exchange_rate(base_currency, target_currency, exchange_rate):
    """
    Insert exchange rate data into the 'exchange_rates' table.

    Args:
        base_currency (str): The base currency for conversion.
        target_currency (str): The target currency for which the exchange rate is requested.
        exchange_rate (float): The normalized exchange rate.
    """
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cur = conn.cursor()

    # Define the SQL query to insert data
    insert_query = """
    INSERT INTO exchange_rates (base_currency, target_currency, exchange_rate, timestamp)
    VALUES (%s, %s, %s, NOW());
    """

    # Provide values for the query
    data = (base_currency, target_currency, exchange_rate)
    cur.execute(insert_query, data)
    conn.commit()

    cur.close()
    conn.close()
