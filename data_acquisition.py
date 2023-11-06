import requests

# Define API URL and parameters
base_url = "https://api.exchangeratesapi.io/v1/latest"
api_key = "940a8603fffdd49ac7d242bc35b6f3bf"
base_currency = "USD"
target_currency = "EUR"

# Construct API request URL
api_request_url = f"{base_url}?base={base_currency}&symbols={target_currency}"
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Send API request and retrieve response
response = requests.get(api_request_url, headers=headers)

if response.status_code == 200:
    # Extract exchange rate from response JSON
    exchange_rate = response.json()["rates"][target_currency]
    print(f"The exchange rate from {base_currency} to {target_currency} is: {exchange_rate}")
else:
    print(f"Error: Unable to retrieve exchange rate. Status code: {response.status_code}")
