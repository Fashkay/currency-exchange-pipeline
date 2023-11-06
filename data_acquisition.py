import requests

def get_exchange_rate(base_currency, target_currency, api_key):
    url = 'https://api.exchangeratesapi.io/v1/'
    params = {
        'base_currency': USD,
        'target_currency': EUR,
        'api_key': 940a8603fffdd49ac7d242bc35b6f3bf
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['exchange_rate']
    else:
        print(f"Error: Unable to fetch exchange rate. Status code: {response.status_code}")
        return None


