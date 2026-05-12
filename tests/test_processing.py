import pytest
from src.processing import filter_by_state, sort_by_date

class TestProcessing:

    @pytest.mark.parametrize("state_value,expected_count", [
        ('EXECUTED', 2),
        ('CANCELED', 1),
        ('PENDING', 0),
        ('FAILED', 0)
    ])
    def test_filter_by_state_parametrized(self, sample_transactions, state_value, expected_count):
        """Параметризованный тест фильтрации по статусу."""
        result = filter_by_state(sample_transactions, state_value)
        assert len(result) == expected_count

    def test_filter_by_state_empty_list(self):
        """Тест фильтрации пустого списка."""
        result = filter_by_state([])
        assert result == []

    @pytest.mark.parametrize("reverse_order,expected_order", [
        (True, ['2019-08-26', '2019-07-03', '2018-06-30']),
        (False, ['2018-06-30', '2019-07-03', '2019-08-26'])
    ])
    def test_sort_by_date_parametrized(self, sample_transactions, reverse_order, expected_order):
        """Параметризованный тест сортировки по дате."""
        result = sort_by_date(sample_transactions, reverse_order)
        dates = [
