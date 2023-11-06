# Acquiring Data via API

The process of acquiring data via an API is a critical step in the Data Acquisition and Preprocessing Pipeline. In this project, we utilize the [Exchange Rates API](https://api.exchangeratesapi.io/v1/latest) to obtain currency exchange rate data.

## API Endpoint

The API endpoint used in this project is:

- Endpoint: `https://api.exchangeratesapi.io/v1/latest`

This endpoint provides access to the latest exchange rates for various currencies.

## Parameters

To retrieve specific exchange rate data, we include the following parameters in our API request:

- Base Currency: USD
- Target Currency: EUR

These parameters define the base currency (USD) and the target currency (EUR) for which we want to obtain the exchange rate.

## Authentication

To access the Exchange Rates API, an API key is required for authentication. The API key is included in the request headers to authorize the API call.

## HTTP Request

We use the `requests` library in Python to send an HTTP GET request to the API endpoint. The response contains the exchange rate data in JSON format.

```python
import requests

# Define API parameters
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
