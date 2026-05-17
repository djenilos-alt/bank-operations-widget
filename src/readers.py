from typing import Any

import pandas as pd


def read_csv_transactions(file_path: str) -> list[dict[str, Any]]:
    """
    Читает финансовые операции из CSV-файла.
    """

    try:
        df = pd.read_csv(file_path)

        records = df.to_dict(orient="records")

        return [
            {str(key): value for key, value in record.items()}
            for record in records
        ]

    except Exception:
        return []


def read_excel_transactions(file_path: str) -> list[dict[str, Any]]:
    """
    Читает финансовые операции из Excel-файла.
    """

    try:
        df = pd.read_excel(file_path)

        records = df.to_dict(orient="records")

        return [
            {str(key): value for key, value in record.items()}
            for record in records
        ]

    except Exception:
        return []
