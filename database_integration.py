import psycopg2

def create_exchange_rates_table():
    try:
        connection = psycopg2.connect(
            database="your_database",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )

        cursor = connection.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id SERIAL PRIMARY KEY,
            base_currency VARCHAR(3),
            target_currency VARCHAR(3),
            exchange_rate DECIMAL(10, 5)
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")

    finally:
        if connection:
            connection.close()

def insert_exchange_rate(base_currency, target_currency, exchange_rate):
    try:
        connection = psycopg2.connect(
            database="your_database",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )

        cursor = connection.cursor()
        insert_query = f'''
        INSERT INTO exchange_rates (base_currency, target_currency, exchange_rate)
        VALUES ('{base_currency}', '{target_currency}', {exchange_rate});
        '''
        cursor.execute(insert_query)
        connection.commit()
        cursor.close()

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")

    finally:
        if connection:
            connection.close()
