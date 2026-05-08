import pytest
from src.widget import mask_account_card


class TestMasks:

    def test_placeholder(self):
        """Placeholder test to avoid IndentationError."""
        assert True

    @pytest.mark.parametrize(
    "input_string,expected", [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("счёт 64686473678894779589", "счёт **9589"),
    ]
)


    def test_mask_account_card_valid(self, input_string, expected):
        result = mask_account_card(input_string)
        # Нормализуем: приводим к одному регистру и заменяем ё→е
        result_norm = result.lower().replace('ё', 'е')
        expected_norm = expected.lower().replace('ё', 'е')
        assert result_norm == expected_norm
