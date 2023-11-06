-- create_schema.sql

CREATE TABLE exchange_rates (
    id SERIAL PRIMARY KEY,
    currency_pair VARCHAR(6) NOT NULL,
    exchange_rate DECIMAL(10, 5) NOT NULL
);
