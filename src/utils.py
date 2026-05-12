import json
from typing import List, Dict, Any


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON‑файл и возвращает список транзакций.

    Args:
        file_path (str): Путь к JSON‑файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями или пустой список.

    Examples:
        >>> read_json_file("data/operations.json")
        [{'id': 1, 'amount': 100, 'currency': 'руб.'}, ...]
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
