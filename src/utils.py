import json
import logging
from typing import Any


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    "logs/utils.log",
    mode="w",
    encoding="utf-8"
)

file_formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(file_formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def read_json_file(filename: str) -> list[dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей.
    """

    try:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
