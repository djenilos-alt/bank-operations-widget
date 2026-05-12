impimport pytest
from src.masks import get_mask_account
from src.masks import get_mask_card_number


class TestMasks:

    @pytest.mark.parametrize("card_number,expected", [
        ("1234567890123456", "1234 56** **** 3456"),
        ("4000008000000000", "4000 00** **** 0000")
    ])
    def test_get_mask_card_number_valid(self, card_number, expected):
        """Тест корректной маскировки номера карты."""
        result = get_mask_card_number(card_number)
        assert result == expected

    @pytest.mark.parametrize("account_number,expected", [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589")
    ])
    def test_get_mask_account_valid(self, account_number, expected):
        """Тест корректной маскировки номера счёта."""
        result = get_mask_account(account_number)
        assert result == expected
