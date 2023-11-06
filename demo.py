from data_acquisition import get_exchange_rate
from preprocessing import normalize_exchange_rate
import database_integration

def main():
    base_currency = "USD"
    target_currency = "EUR"
    api_key = "940a8603fffdd49ac7d242bc35b6f3bf"

    # Step 1: Acquire exchange rate
    exchange_rate = get_exchange_rate(base_currency, target_currency, api_key)

    if exchange_rate is not None:
        print(f"Exchange rate ({base_currency} to {target_currency}): {exchange_rate}")

        # Step 2: Normalize exchange rate
        normalized_exchange_rate = normalize_exchange_rate(exchange_rate)
        print(f"Normalized exchange rate: {normalized_exchange_rate}")

        # Step 3: Store in database
        database_integration.create_exchange_rates_table()
        database_integration.insert_exchange_rate(base_currency, target_currency, normalized_exchange_rate)
        print("Exchange rate data stored in database.")

if __name__ == "__main__":
    main()
