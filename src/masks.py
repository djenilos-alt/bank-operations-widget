import logging
import os

# Создаём папку logs, если её нет
os.makedirs('logs', exist_ok=True)

# Создаём логер для модуля masks
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Настраиваем обработчик для записи в файл
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Форматировщик: время, модуль, уровень, сообщение
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты: первые 6 цифр + 6 звёздочек + последние 4 цифры."""
    logger.debug(f"Получение маски для номера карты: {card_number}")
    cleaned = card_number.replace(" ", "")
    if not cleaned.isdigit():
        error_msg = "Card number must contain only digits"
        logger.error(error_msg)
        raise ValueError(error_msg)
    if len(cleaned) < 13 or len(cleaned) > 19:
        error_msg = "Card number must be 13-19 digits long"
        logger.error(error_msg)
        raise ValueError(error_msg)

    masked = cleaned[:6] + "******" + cleaned[-4:]
    parts = [masked[i:i+4] for i in range(0, len(masked), 4)]
    result = " ".join(parts)
    logger.info(f"Маска карты успешно создана: {result}")
    return result


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта: последние 4 цифры с префиксом **."""
    logger.debug(f"Получение маски для номера счёта: {account_number}")
    cleaned = account_number.replace(" ", "")
    if not cleaned.isdigit():
        error_msg = "Account number must contain only digits"
        logger.error(error_msg)
        raise ValueError(error_msg)
    if len(cleaned) != 20:
        error_msg = "Account number must be exactly 20 digits long"
        logger.error(error_msg)
        raise ValueError(error_msg)
    result = f"**{cleaned[-4:]}"
    logger.info(f"Маска счёта успешно создана: {result}")
    return result
