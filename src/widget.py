import re
from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счёта.
    При невалидных данных возвращает исходную строку.
    """

    if not data.strip():
        return data

    digits = re.sub(r"\D", "", data)
    name = re.sub(r"[\d\s]+$", "", data).strip()

    try:
        # Счёт
        if name.lower() in ["счет", "счёт"]:
            return f"{name} {get_mask_account(digits)}".strip()

        # Карта или просто номер карты
        if digits:
            masked = get_mask_card_number(digits)

            if name:
                return f"{name} {masked}".strip()

            return masked

    except ValueError:
        return data

    return data


def get_date(date_string: str) -> str:
    """
    Преобразует дату из ISO-формата в DD.MM.YYYY
    """

    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
