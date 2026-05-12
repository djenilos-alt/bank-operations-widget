from unittest.mock import mock_open, patch
from src.utils import read_json_file


class TestReadJsonFile:
    def test_valid_json_list(self):
        mock_data = '[{"id": 1, "amount": 100}]'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = read_json_file('test.json')
            assert result == [{'id': 1, 'amount': 100}]

    def test_empty_file(self):
        with patch('builtins.open', mock_open(read_data='')):
            result = read_json_file('empty.json')
            assert result == []

    def test_not_a_list_json(self):
        mock_data = '{"key": "value"}'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = read_json_file('not_list.json')
            assert result == []

    def test_file_not_found(self):
        result = read_json_file('nonexistent.json')
        assert result == []
