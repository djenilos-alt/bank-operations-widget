from unittest.mock import patch

import pandas as pd

from src.readers import read_csv_transactions


@patch("src.readers.pd.read_csv")
def test_read_csv_transactions(mock_read_csv):
    """Тест чтения CSV-файла."""

    mock_df = pd.DataFrame([
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ])

    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("transactions.csv")

    assert result == [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]

    mock_read_csv.assert_called_once_with("transactions.csv")
