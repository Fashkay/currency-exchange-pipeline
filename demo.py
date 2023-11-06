from data_acquisition import get_exchange_rate
from preprocessing import normalize_exchange_rate
from database_integration import create_exchange_rates_table, insert_exchange_rate

# Define API parameters
base_currency = "USD"
target_currency = "EUR"
api_key = "940a8603fffdd49ac7d242bc35b6f3bf"

# Step 1: Data Acquisition
exchange_rate = get_exchange_rate(base_currency, target_currency, api_key)

# Step 2: Preprocessing and Transformation
normalized_exchange_rate = normalize_exchange_rate(exchange_rate)

# Step 3: Database Integration
create_exchange_rates_table()  # Create the 'exchange_rates' table if not exists
insert_exchange_rate(base_currency, target_currency, normalized_exchange_rate)  # Insert data into the table
