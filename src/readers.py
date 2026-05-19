import pandas as pd


def read_csv_transactions(path: str) -> list[dict]:
    """Считывает финансовые операции из CSV-файла.

    Args:
        path: Путь к CSV-файлу.

    Returns:
        Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(path)
        return df.to_dict(orient="records")
    except Exception:
        return []


def read_excel_transactions(path: str) -> list[dict]:
    """Считывает финансовые операции из Excel-файла.

    Args:
        path: Путь к Excel-файлу.

    Returns:
        Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient="records")
    except Exception:
        return []
