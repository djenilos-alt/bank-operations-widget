from datetime import datetime
from typing import Dict
from typing import List


def filter_by_state(
    transactions_list: List[Dict[str, str]],
    state_value: str = 'EXECUTED'
) -> List[Dict[str, str]]:
    """
    Фильтрует список транзакций по значению поля state.
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
    Сортирует список транзакций по дате.
    """

    def parse_transaction_date(date_string: str) -> datetime:
        return datetime.fromisoformat(date_string)

    valid_transactions = [
        transaction
        for transaction in transactions_list
        if 'date' in transaction
    ]

    return sorted(
        valid_transactions,
        key=lambda x: parse_transaction_date(x['date']),
        reverse=reverse_order
    )
