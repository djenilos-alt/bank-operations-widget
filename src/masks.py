def get_mask_card_number(card_number: str) -> str:
    cleaned = card_number.replace(" ", "")

    if not cleaned.isdigit():
        raise ValueError("Card number must contain only digits")

    if len(cleaned) < 13 or len(cleaned) > 19:
        raise ValueError("Card number must be 13-19 digits long")

    return f"{cleaned[:4]} {cleaned[4:6]}****** {cleaned[-4:]}"


def get_mask_account(account_number: str) -> str:
    cleaned = account_number.replace(" ", "")

    if not cleaned.isdigit():
        raise ValueError("Account number must contain only digits")

    if len(cleaned) != 20:
        raise ValueError("Account number must be exactly 20 digits long")

    return f"**{cleaned[-4:]}"
