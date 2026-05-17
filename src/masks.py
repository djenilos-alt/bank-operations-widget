import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    "logs/masks.log",
    mode="w",
    encoding="utf-8"
)

file_formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(file_formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    cleaned = card_number.replace(" ", "")

    logger.debug("Начало маскировки карты")

    if not cleaned.isdigit():
        logger.error("Номер карты содержит не только цифры")
        raise ValueError("Card number must contain only digits")

    if len(cleaned) < 13 or len(cleaned) > 19:
        logger.error("Некорректная длина номера карты")
        raise ValueError("Card number must be 13-19 digits long")

    result = f"{cleaned[:4]} {cleaned[4:6]}****** {cleaned[-4:]}"

    logger.info("Номер карты успешно замаскирован")

    return result


def get_mask_account(account_number: str) -> str:
    cleaned = account_number.replace(" ", "")

    logger.debug("Начало маскировки счета")

    if not cleaned.isdigit():
        logger.error("Номер счета содержит не только цифры")
        raise ValueError("Account number must contain only digits")

    if len(cleaned) != 20:
        logger.error("Некорректная длина номера счета")
        raise ValueError("Account number must be exactly 20 digits long")

    result = f"**{cleaned[-4:]}"

    logger.info("Номер счета успешно замаскирован")

    return result
