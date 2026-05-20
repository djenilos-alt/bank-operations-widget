import pytest
from src.search_operations import process_bank_search, process_bank_operations

def test_process_bank_search():
    data = [
        {"id": 1, "description": "Перевод в магазин"},
        {"id": 2, "description": "Оплата услуг"},
        {"id": 3, "description": "Перевод другу"}
    ]
    result = process_bank_search(data, "перевод")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3

def test_process_bank_operations():
    data = [
        {"id": 1, "description": "Покупка в супермаркете"},
        {"id": 2, "description": "Оплата кафе"},
        {"id": 3, "description": "Супермаркет покупки"}
    ]
    categories = ["супермаркет", "кафе"]
    result = process_bank_operations(data, categories)
    assert result["супермаркет"] == 2
    assert result["кафе"] == 1
