import pytest
from src.widget import mask_account_card

class TestWidget:
    @pytest.mark.parametrize(
        "input_string,expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79****** 6361"),
            ("Maestro 1596837868705199", "Maestro 1596 83****** 5199"),
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
        ["", "Visa Platinum", "Счет", "Счёт", "Visa", "12345"],
    )
    def test_mask_account_card_invalid(self, invalid_input):
        """Тест обработки некорректных входных данных."""
        result = mask_account_card(invalid_input)
        assert result == invalid_input

    def test_mask_account_card_with_spaces_in_number(self):
        """Тест маскировки номера с пробелами."""
        input_string = "Visa Platinum 7000 7922 8960 6361"
        expected = "Visa Platinum 7000 79****** 6361"
        result = mask_account_card(input_string)
        assert result == expected

    def test_mask_account_card_mixed_case(self):
        """Тест с разным регистром в названии карты."""
        input_string = "visa platinum 7000792289606361"
        expected = "visa platinum 7000 79****** 6361"
        result = mask_account_card(input_string)
        assert result == expected

    def test_mask_account_card_only_digits(self):
        """Тест ввода только цифр (без названия карты/счёта)."""
        input_string = "7000792289606361"
        expected = "7000 79****** 6361"
        result = mask_account_card(input_string)
        assert result == expected

    def test_mask_account_card_long_account_number(self):
        """Тест длинного номера счёта (более 20 цифр)."""
        input_string = "Счет 123456789012345678901"
        # Должен вернуть исходную строку, т.к. номер невалиден
        result = mask_account_card(input_string)
        assert result == input_string

    def test_mask_account_card_short_card_number(self):
        """Тест короткого номера карты (менее 13 цифр)."""
        input_string = "Visa 123456789"
        # Должен вернуть исходную строку, т.к. номер невалиден
        result = mask_account_card(input_string)
        assert result == input_string
