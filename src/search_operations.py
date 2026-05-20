import re
from collections import Counter
from typing import Any
from typing import Counter as CounterType
from typing import Dict
from typing import List


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Ищет транзакции по строке в описании с использованием регулярных выражений.

    Args:
        data (List[Dict[str, Any]]): Список транзакций (словарей).
        search (str): Строка для поиска в поле 'description'.

    Returns:
        List[Dict[str, Any]]: Список транзакций, где в описании найдено совпадение.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result: List[Dict[str, Any]] = []
    for transaction in data:
        description = transaction.get('description', '')
        if pattern.search(description):
            result.append(transaction)
    return result


def process_bank_operations(
    data: List[Dict[str, Any]],
    categories: List[str]
) -> Dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям.

    Args:
        data (List[Dict[str, Any]]): Список транзакций.
        categories (List[str]): Список категорий для подсчёта.

    Returns:
        Dict[str, int]: Словарь с категориями и количеством операций.
    """
    counter: CounterType[str] = Counter()
    for transaction in data:
        desc = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in desc:
                counter[category] += 1
    return dict(counter)
