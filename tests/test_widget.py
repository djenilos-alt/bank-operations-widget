import pytest

from src.widget import get_date
from src.widget import mask_account_card


class TestWidget:

    @pytest.mark.parametrize(
        "input_string,expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
            ("Счет 73654108430135874305", "Счет **4305"),
            ("счёт 64686473678894779589", "счёт **9589"),
        ],
    )
    def test_mask_account_card_valid(self, input_string, expected):
        """Тест корректной работы маскировки для карт и счетов."""
        result = mask_account_card(input_string)
        assert result == expected

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "",
            "Visa Platinum",
            "Счет",
        ],
    )
    def test_mask_account_card_invalid(self, invalid_input):
        """Тест обработки некорректных входных данных."""
        # Для пустых или неполных строк функция должна возвращать исходную строку
        result = mask_account_card(invalid_input)
        assert result == invalid_input

    @pytest.mark.parametrize(
        "date_string,expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2023-12-25T15:30:45.123456", "25.12.2023"),
            ("2022-01-01T00:00:00.000000", "01.01.2022"),
        ],
    )
    def test_get_date_valid(self, date_string, expected):
        """Тест корректного преобразования даты."""
        result = get_date(date_string)
        assert result == expected

    @pytest.mark.parametrize(
        "invalid_date",
        [
            "invalid-date-format",
            "",
            "2024/03/11",
        ],
    )
    def test_get_date_invalid(self, invalid_date):
        """Тест обработки некорректных форматов даты."""
        result = get_date(invalid_date)
        assert result == invalid_date
