import requests

def get_exchange_rate(base_currency, target_currency, api_key):
    url = f"https://api.exchangeratesapi.io/v1/latest?base={base_currency}&symbols={target_currency}"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        exchange_rate = data['rates'][target_currency]
        return exchange_rate
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch data. {e}")
        return None
