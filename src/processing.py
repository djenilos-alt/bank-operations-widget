from datetime import datetime
from typing import List, Dict, Optional

def filter_by_state(
    transactions_list: List[Dict[str, str]],
    state_value: str = 'EXECUTED'
) -> List[Dict[str, str]]:
    """
    Фильтрует список транзакций по значению поля state.

    Args:
        transactions_list (List[Dict[str, str]]): Список словарей с транзакциями.
            Каждый словарь должен содержать ключ 'state'.
        state_value (str): Значение поля state для фильтрации.
            По умолчанию — 'EXECUTED'.

    Returns:
        List[Dict[str, str]]: Отфильтрованный список транзакций.
    """
    return [
        transaction
        for transaction in transactions_list
        if transaction.get('state') == state_value
    ]

def sort_by_date(
    transactions_list: List[Dict[str, str]],
    reverse_order: bool = True
) -> List[Dict[str, str]]:
    """
    Сортирует список транзакций по дате в указанном порядке.

    Args:
        transactions (list): Список транзакций с полем 'date'.
        reverse_order (bool): Если True — сортировка по убыванию, иначе по возрастанию.

    Returns:
        List[Dict[str, str]]: Отсортированный список транзакций.
    """
    def parse_transaction_date(date_string: str) -> Optional[datetime]:
        """Парсит строку даты в объект datetime."""
        try:
            return datetime.fromisoformat(date_string)
        except (ValueError, TypeError):
            return None

    # Фильтруем транзакции с корректными датами
    valid_transactions = [
        transaction
        for transaction in transactions_list
        if 'date' in transaction and parse_transaction_date(transaction['date']) is not None
    ]

    return sorted(
        valid_transactions,
        key=lambda x: parse_transaction_date(x['date']),
        reverse=reverse_order
    )

