import requests
from typing import Dict, Optional
import os
import json  # необходим для обработки JSONDecodeError

def convert_currency(transaction: Dict) -> Optional[float]:
    """
    Конвертирует валюту по данным из транзакции, используя эндпоинт convert API Apilayer.
    Возвращает только сумму типа float или None в случае ошибки.
    """
    # 1. Проверка на None
    if transaction is None:
        print("Ошибка: транзакция не предоставлена (None)")
        return None

    # 2. Проверка обязательных ключей
    if 'operationAmount' not in transaction:
        print("Ошибка: отсутствует ключ 'operationAmount' в транзакции")
        return None

    operation_amount = transaction['operationAmount']

    if 'amount' not in operation_amount:
        print("Ошибка: отсутствует ключ 'amount' в 'operationAmount'")
        return None
    if 'currency' not in operation_amount:
        print("Ошибка: отсутствует ключ 'currency' в 'operationAmount'")
        return None

    currency_data = operation_amount['currency']
    if 'code' not in currency_data:
        print("Ошибка: отсутствует ключ 'code' в 'currency'")
        return None

    # 3. Извлечение данных
    try:
        original_amount = float(operation_amount['amount'])
        original_currency = currency_data['code'].upper()
    except (ValueError, TypeError) as e:
        print(f"Ошибка преобразования данных: {e}")
        return None

    target_currency = 'RUB'

    # 4. Запрос к API через эндпоинт convert
    try:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        params = {
            "from": original_currency,
            "to": target_currency,
            "amount": original_amount
        }
        headers = {
            "apikey": os.getenv("APILAYER_API_KEY")
        }

        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        # 5. Извлечение готовой суммы из ответа API
        if data.get("success") and "result" in data:
            return float(data["result"])
        else:
            # Безопасная обработка ошибки: проверяем тип data
            if isinstance(data, dict) and "error" in data:
                error_info = data["error"].get("info", "Неизвестный ответ API")
            else:
                error_info = "Некорректный формат ответа API"
            print(f"Ошибка API: {error_info}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при обращении к API: {e}")
        return None
    except (KeyError, ValueError, TypeError) as e:
        print(f"Ошибка обработки ответа API: {e}")
        return None
    except json.JSONDecodeError as e:  # Обработка не-JSON ответов
        print(f"Ошибка парсинга JSON: {e}")
        return None
