from unittest.mock import patch, Mock
from src.external_api import convert_to_rubles


class TestConvertToRubles:
    @patch('requests.get')
    def test_usd_to_rub(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'USD': 90.0}}
        mock_get.return_value = mock_response

        transaction = {'amount': '100', 'currency': 'USD'}
        result = convert_to_rubles(transaction)
        assert result == 9000.0

    @patch('requests.get')
    def test_eur_to_rub(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'EUR': 100.0}}
        mock_get.return_value = mock_response

        transaction = {'amount': '50', 'currency': 'EUR'}
        result = convert_to_rubles(transaction)
        assert result == 5000.0

    def test_rub_no_conversion(self):
        transaction = {'amount': '1000', 'currency': 'руб.'}
        result = convert_to_rubles(transaction)
        assert result == 1000.0
