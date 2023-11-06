# Artefact and Code Listing

## Main Code Files

1. **Data Acquisition Module** (`data_acquisition.py`):

```python
import requests

def get_exchange_rate(base_currency, target_currency, api_key):
    # Implementation of get_exchange_rate function...
}

def normalize_exchange_rate(exchange_rate):
    # Implementation of normalize_exchange_rate function...
}

import psycopg2

def create_exchange_rates_table():
    # Implementation of create_exchange_rates_table function...

def insert_exchange_rate(base_currency, target_currency, exchange_rate):
    # Implementation of insert_exchange_rate function...

def get_exchange_rates():
    # Implementation of get_exchange_rates function...
}

from data_acquisition import get_exchange_rate
from preprocessing import normalize_exchange_rate
import database_integration

def main():
    # Implementation of main function...
}

if __name__ == "__main__":
    main()
