from data_acquisition import get_exchange_rate

# 
api_key = '08b645705f5343e691c1ee0f05661bde'
base_currency = "USD"
target_currency = "EUR"

try:
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
    print(f"The exchange rate from {base_currency} to {target_currency} is: {exchange_rate}")
except Exception as e:
    print(e)
