import json
import logging
import os
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List

# Создаём папку logs в корне проекта, если её нет
logs_dir = Path(__file__).parent.parent / "logs"
logs_dir.mkdir(exist_ok=True)

# Создаём логер для модуля utils
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Настраиваем обработчик для записи в файл
file_handler = logging.FileHandler(
    logs_dir / "utils.log",
    mode='w',  # Перезаписываем при каждом запуске
    encoding='utf-8'
)
file_handler.setLevel(logging.DEBUG)

# Форматировщик: время, модуль, уровень, сообщение
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логеру (если ещё не добавлен)
if not logger.handlers:
    logger.addHandler(file_handler)


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON‑файл и возвращает список транзакций.

    Args:
        file_path (str): Путь к JSON‑файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями или пустой список.
    Examples:
        >>> read_json_file("data/operations.json")
        [{'id': 1, 'amount': 100, 'currency': 'руб.'}, ...]
    """
    logger.debug(f"Попытка чтения JSON‑файла: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Успешно прочитан JSON‑файл: {file_path}, найдено {len(data)} транзакций")
                return data
            else:
                logger.warning(f"JSON‑файл {file_path} содержит данные не в формате списка, возвращаем пустой список")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []
    except Exception as e:
        logger.critical(f"Неожиданная ошибка при чтении файла {file_path}: {e}")
        return []
