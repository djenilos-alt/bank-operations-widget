import requests
import os
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

API_KEY = os.getenv('EXCHANGE_API_KEY')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'


def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    """
    amount = float(transaction.get('amount', 0))
    currency = transaction.get('currency', 'руб.')

    if currency == 'руб.':
        return amount

    try:
        params = {'access_key': API_KEY, 'symbols': currency, 'base': 'RUB'}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        rates = response.json().get('rates', {})

        if currency in rates:
            rate = rates[currency]
            return amount * rate
        else:
            raise ValueError(f"Unsupported currency: {currency}")
    except requests.RequestException as e:
        raise ValueError(f"API error: {e}")
