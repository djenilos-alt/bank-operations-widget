from collections.abc import Iterator
from typing import Any, List, Dict, Optional


def transaction_generator(
    transactions: List[Dict[str, Any]]
) -> Iterator[Dict[str, Any]]:
    """
    Генератор для последовательного получения транзакций.

    Args:
        transactions: Список транзакций в формате словаря.

    Yields:
        Каждая транзакция по очереди.

    Example:
        >>> transactions = [{'id': 1}, {'id': 2}]
        >>> gen = transaction_generator(transactions)
        >>> next(gen)
        {'id': 1}
    """
    for transaction in transactions:
        yield transaction


def filtered_transaction_generator(
    transactions: List[Dict[str, Any]],
    filter_key: str,
    filter_value: Any
) -> Iterator[Dict[str, Any]]:
    """
    Генератор транзакций с фильтрацией по заданному критерию.

    Args:
        transactions: Список транзакций для фильтрации.
        filter_key: Ключ для фильтрации (например, 'state').
        filter_value: Значение для фильтрации (например, 'EXECUTED').

    Yields:
        Транзакции, удовлетворяющие условию фильтрации.

    Example:
        >>> transactions = [
        ...     {'id': 1, 'state': 'EXECUTED'},
        ...     {'id': 2, 'state': 'CANCELED'}
        ... ]
        >>> gen = filtered_transaction_generator(transactions, 'state', 'EXECUTED')
        >>> next(gen)
        {'id': 1, 'state': 'EXECUTED'}
    """
    for transaction in transactions:
        if transaction.get(filter_key) == filter_value:
            yield transaction


def amount_generator(
    transactions: List[Dict[str, Any]],
    currency: Optional[str] = None
) -> Iterator[float]:
    """
    Генератор сумм транзакций с возможностью фильтрации по валюте.

    Args:
        transactions: Список транзакций.
        currency: Валюта для фильтрации (опционально).

    Yields:
        Суммы транзакций (преобразованные в float) по очереди.

    Example:
        >>> transactions = [
        ...     {'amount': '100.50', 'currency': 'руб.'},
        ...     {'amount': '200.00', 'currency': 'USD'}
        ... ]
        >>> gen = amount_generator(transactions, 'руб.')
        >>> next(gen)
        100.5
    """
    for transaction in transactions:
        # Проверяем валюту, если она указана
        if currency and transaction.get('currency') != currency:
            continue

        try:
            # Преобразуем строку в число
            amount = float(transaction['amount'])
            yield amount
        except (ValueError, KeyError):
            # Пропускаем транзакции с некорректными суммами
            continue


def date_generator(
    transactions: List[Dict[str, Any]]
) -> Iterator[str]:
    """
    Генератор дат транзакций в формате ISO.

    Args:
        transactions: Список транзакций с полем 'date'.

    Yields:
        Даты транзакций в исходном формате.

    Example:
        >>> transactions = [
        ...     {'date': '2023-01-01T10:00:00'},
        ...     {'date': '2023-02-01T12:30:00'}
        ... ]
        >>> gen = date_generator(transactions)
        >>> next(gen)
        '2023-01-01T10:00:00'
    """
    for transaction in transactions:
        date_str = transaction.get('date', '')
        if date_str:
            yield date_str
