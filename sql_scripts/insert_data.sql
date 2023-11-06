-- insert_data.sql

-- Insert sample exchange rate data
INSERT INTO exchange_rates (base_currency, target_currency, exchange_rate, timestamp)
VALUES 
    ('USD', 'EUR', 0.845678, '2023-11-06 12:34:56'),
    ('USD', 'GBP', 0.750912, '2023-11-06 12:35:02'),
    ('EUR', 'JPY', 133.521789, '2023-11-06 12:36:12'),
    ('EUR', 'USD', 1.182345, '2023-11-06 12:37:24'),
    ('GBP', 'EUR', 1.330456, '2023-11-06 12:38:15');
