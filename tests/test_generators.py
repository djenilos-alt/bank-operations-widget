import pytest
from src.generators import (
    transaction_generator,
    filtered_transaction_generator,
    amount_generator,
    date_generator
)


class TestGenerators:
    @pytest.fixture
    def sample_transactions(self):
        """Фикстура с тестовыми транзакциями."""
        return [
            {'id': 1, 'state': 'EXECUTED', 'amount': '100.50',
             'currency': 'руб.', 'date': '2023-01-01T10:00:00'},
            {'id': 2, 'state': 'CANCELED', 'amount': '200.00',
             'currency': 'USD', 'date': '2023-02-01T12:30:00'},
            {'id': 3, 'state': 'EXECUTED', 'amount': '300.75',
             'currency': 'руб.', 'date': '2023-03-01T09:15:00'},
        ]

    def test_transaction_generator(self, sample_transactions):
        """Тест базового генератора транзакций."""
        gen = transaction_generator(sample_transactions)

        assert next(gen) == sample_transactions[0]
        assert next(gen) == sample_transactions[1]
        assert next(gen) == sample_transactions[2]

        with pytest.raises(StopIteration):
            next(gen)

    def test_filtered_transaction_generator_executed(self, sample_transactions):
        """Тест фильтрации транзакций по статусу 'EXECUTED'."""
        gen = filtered_transaction_generator(
            sample_transactions, 'state', 'EXECUTED'
        )

        result1 = next(gen)
        result2 = next(gen)

        assert result1['id'] == 1
        assert result2['id'] == 3

        with pytest.raises(StopIteration):
            next(gen)

    def test_filtered_transaction_generator_canceled(self, sample_transactions):
        """Тест фильтрации транзакций по статусу 'CANCELED'."""
        gen = filtered_transaction_generator(
            sample_transactions, 'state', 'CANCELED'
        )

        result = next(gen)
        assert result['id'] == 2

        with pytest.raises(StopIteration):
            next(gen)

    def test_amount_generator_rub(self, sample_transactions):
        """Тест генератора сумм в рублях."""
        gen = amount_generator(sample_transactions, 'руб.')

        assert next(gen) == 100.5
        assert next(gen) == 300.75

        with pytest.raises(StopIteration):
            next(gen)

    def test_amount_generator_usd(self, sample_transactions):
        """Тест генератора сумм в долларах."""
        gen = amount_generator(sample_transactions, 'USD')

        assert next(gen) == 200.0

        with pytest.raises(StopIteration):
            next(gen)

    def test_amount_generator_all_currencies(self, sample_transactions):
        """Тест генератора всех сумм без фильтрации по валюте."""
        gen = amount_generator(sample_transactions)

        assert next(gen) == 100.5
        assert next(gen) == 200.0
        assert next(gen) == 300.75

        with pytest.raises(StopIteration):
            next(gen)

    def test_amount_generator_invalid_amount(self):
        """Тест обработки некорректных сумм."""
        transactions = [
            {'amount': 'invalid', 'currency': 'руб.'},
            {'amount': '150.25', 'currency': 'руб.'}
        ]
        gen = amount_generator(transactions, 'руб.')

        # Первая транзакция пропускается из‑за некорректной суммы
        assert next(gen) == 150.25

        with pytest.raises(StopIteration):
            next(gen)

    def test_date_generator(self, sample_transactions):
        gen = date_generator(sample_transactions)
        assert next(gen) == '2023-01-01T10:00:00'
        assert next(gen) == '2023-02-01T12:30:00'
        assert next(gen) == '2023-03-01T09:15:00'

        # Проверяем, что генератор исчерпан
        with pytest.raises(StopIteration):
            next(gen)
