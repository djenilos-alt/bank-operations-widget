def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    cleaned = card_number.replace(' ', '')
    if len(cleaned) != 16 or not cleaned.isdigit():
        raise ValueError("Invalid card number")
    return f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"

def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта."""
    cleaned = account_number.replace(' ', '')
    if len(cleaned) != 20 or not cleaned.isdigit():
        raise ValueError("Invalid account number")
    return f"**{cleaned[-4:]}"
