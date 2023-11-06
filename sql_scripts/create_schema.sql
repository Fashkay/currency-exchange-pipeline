-- create_schema.sql

-- Create the 'exchange_rates' table
CREATE TABLE IF NOT EXISTS exchange_rates (
    id SERIAL PRIMARY KEY,
    base_currency VARCHAR(3) NOT NULL,
    target_currency VARCHAR(3) NOT NULL,
    exchange_rate DECIMAL(10, 6) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

-- Create indexes for efficient retrieval
CREATE INDEX IF NOT EXISTS base_currency_index ON exchange_rates (base_currency);
CREATE INDEX IF NOT EXISTS target_currency_index ON exchange_rates (target_currency);
