import pytest
from unittest.mock import patch
import pandas as pd

from src.readers import (
    read_csv_transactions,
    read_excel_transactions,
)


class TestFileReaders:

    @patch('src.readers.pd.read_csv')
    def test_read_csv_file_success(self, mock_read_csv):
        """Тест успешного чтения CSV-файла."""

        mock_df = pd.DataFrame([
            {"id": 1, "amount": 100, "currency": "руб."},
            {"id": 2, "amount": 200, "currency": "руб."},
        ])

        mock_read_csv.return_value = mock_df

        result = read_csv_transactions("transactions.csv")

        assert isinstance(result, list)
        assert len(result) == 2
        assert result == [
            {"id": 1, "amount": 100, "currency": "руб."},
            {"id": 2, "amount": 200, "currency": "руб."}
        ]

        mock_read_csv.assert_called_once_with("transactions.csv")

    @patch('src.readers.pd.read_csv')
    def test_read_csv_file_empty(self, mock_read_csv):
        """Тест чтения пустого CSV-файла."""

        mock_df = pd.DataFrame()
        mock_read_csv.return_value = mock_df

        result = read_csv_transactions("empty.csv")

        assert isinstance(result, list)
        assert len(result) == 0

        mock_read_csv.assert_called_once_with("empty.csv")

    @patch('src.readers.pd.read_csv')
    def test_read_csv_file_error(self, mock_read_csv):
        """Тест обработки ошибки при чтении CSV-файла."""

        mock_read_csv.side_effect = Exception("File not found")

        result = read_csv_transactions("nonexistent.csv")

        assert isinstance(result, list)
        assert len(result) == 0

        mock_read_csv.assert_called_once_with("nonexistent.csv")

    @patch('src.readers.pd.read_excel')
    def test_read_excel_file_success(self, mock_read_excel):
        """Тест успешного чтения Excel-файла."""

        mock_df = pd.DataFrame([
            {"id": 1, "amount": 150, "category": "Продукты"},
            {"id": 2, "amount": 300, "category": "Транспорт"},
        ])

        mock_read_excel.return_value = mock_df

        result = read_excel_transactions("transactions_excel.xlsx")

        assert isinstance(result, list)
        assert len(result) == 2
        assert result == [
            {"id": 1, "amount": 150, "category": "Продукты"},
            {"id": 2, "amount": 300, "category": "Транспорт"}
        ]

        mock_read_excel.assert_called_once_with("transactions_excel.xlsx")

    @patch('src.readers.pd.read_excel')
    def test_read_excel_file_error(self, mock_read_excel):
        """Тест обработки ошибки при чтении Excel-файла."""

        mock_read_excel.side_effect = Exception("Invalid file format")

        result = read_excel_transactions("invalid.xlsx")

        assert isinstance(result, list)
        assert len(result) == 0

        mock_read_excel.assert_called_once_with("invalid.xlsx")
