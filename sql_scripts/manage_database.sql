-- manage_database.sql

-- Drop the 'exchange_rates' table if it exists
DROP TABLE IF EXISTS exchange_rates;

-- Create the 'exchange_rates' table
CREATE TABLE exchange_rates (
    id SERIAL PRIMARY KEY,
    base_currency VARCHAR(3) NOT NULL,
    target_currency VARCHAR(3) NOT NULL,
    exchange_rate DECIMAL(10, 6) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

-- Create indexes for efficient retrieval
CREATE INDEX base_currency_index ON exchange_rates (base_currency);
CREATE INDEX target_currency_index ON exchange_rates (target_currency);

-- Truncate the 'exchange_rates' table (remove all data)
TRUNCATE TABLE exchange_rates;

-- Add more statements as needed for database management
