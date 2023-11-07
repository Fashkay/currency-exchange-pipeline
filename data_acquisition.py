import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    """
    Get the exchange rate from the Open Exchange Rates API.

    Args:
        api_key (str): Your API key for authentication.
        base_currency (str): The base currency for conversion.
        target_currency (str): The target currency for which the exchange rate is requested.

    Returns:
        float: The exchange rate.
    """
    base_url = "https://openexchangerates.org/api/latest.json"
    params = {
        "app_id": api_key,
        "base": base_currency,
        "symbols": target_currency
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()["rates"][target_currency]
    else:
        raise Exception(f"Error: Unable to retrieve exchange rate. Status code: {response.status_code}")
