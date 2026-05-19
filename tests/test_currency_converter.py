from unittest.mock import Mock
from unittest.mock import patch

import pytest
import requests

from src.currency_converter import convert_currency


class TestCurrencyConverter:
    """Тесты для функции конвертации валюты."""

    @patch('requests.get')
    def test_convert_currency_success(self, mock_get):
        """Тест успешной конвертации через эндпоинт convert."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "success": True,
            "result": 9250.0
        }
        mock_get.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "code": "USD"
                }
            }
        }

        result = convert_currency(transaction)

        assert isinstance(result, float)
        assert result == 9250.0

    @patch('requests.get')
    def test_api_request_failure(self, mock_get):
        """Тест ошибки при обращении к API."""
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        transaction = {
            "operationAmount": {
                "amount": 100,
                "currency": {"code": "USD"}
            }
        }

        result = convert_currency(transaction)

        assert result is None

    def test_none_transaction(self):
        """Тест передачи None вместо транзакции."""
        result = convert_currency(None)

        assert result is None

    def test_missing_operation_amount_key(self):
        """Тест отсутствия ключа 'operationAmount'."""
        transaction = {"amount": 100, "currency": "USD"}

        result = convert_currency(transaction)

        assert result is None

    def test_invalid_amount_type(self):
        """Тест некорректного типа данных для 'amount'."""
        transaction = {
            "operationAmount": {
                "amount": "not_a_number",
                "currency": {"code": "USD"}
            }
        }

        result = convert_currency(transaction)

        assert result is None

    @patch('requests.get')
    def test_api_response_missing_result(self, mock_get):
        """Тест ответа API без поля 'result'."""
        mock_response = Mock()
        mock_response.json.return_value = {"success": False, "error": {"info": "No rates available"}}
        mock_get.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": 100,
                "currency": {"code": "USD"}
            }
        }

        result = convert_currency(transaction)

        assert result is None

    def test_empty_transaction(self):
        """Тест пустой транзакции."""
        result = convert_currency({})

        assert result is None
