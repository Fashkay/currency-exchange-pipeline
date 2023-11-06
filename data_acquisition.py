import requests

def get_exchange_rate(base_currency, target_currency, api_key):
    """
    Get the exchange rate from the API.

    Args:
        base_currency (str): The base currency for conversion.
        target_currency (str): The target currency for which the exchange rate is requested.
        api_key (str): The API key for authentication.

    Returns:
        float: The exchange rate.
    """
    base_url = "https://api.exchangeratesapi.io/v1/latest"
    api_request_url = f"{base_url}?base={base_currency}&symbols={target_currency}"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(api_request_url, headers=headers)

    if response.status_code == 200:
        return response.json()["rates"][target_currency]
    else:
        raise Exception(f"Error: Unable to retrieve exchange rate. Status code: {response.status_code}")
