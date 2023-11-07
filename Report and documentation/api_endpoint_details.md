# API Endpoint Details

## Endpoint URL

The Currency Exchange Rate Data Acquisition Pipeline interacts with the API using the following base URL:

https://openexchangerates.org/api/latest.json


## Supported Parameters

The API supports the following parameters:

- `base`: The base currency for exchange rate conversion.
- `symbols`: The target currency or currencies for which exchange rates are requested.

Example API Request:


https://openexchangerates.org/api/latest.json?base=USD&symbols=EUR,GBP