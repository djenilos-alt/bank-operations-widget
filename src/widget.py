from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(input_string: str) -> str:
    """Определяет тип и маскирует карту или счёт."""
    if 'Счёт' in input_string or 'счет' in input_string.lower():
        account_part = input_string.split()[-1]
        masked = get_mask_account(account_part)
        return f"Счёт {masked}" if 'Счёт' in input_string else f"счёт {masked}"
    else:
        card_part = input_string.split()[-1]
        masked = get_mask_card_number(card_part)
        return f"{input_string[:-16]}{masked}"

def get_date(date_string: str) -> str:
    """Преобразует дату из ISO в ДД.ММ.ГГГГ."""
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return date_string
