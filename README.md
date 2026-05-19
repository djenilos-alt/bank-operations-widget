 ## Тестирование

Проект имеет покрытие тестами более 85 %.

### Структура тестов

* `tests/test_masks.py` — тесты для модуля маскировки данных (карты и счета);
* `tests/test_widget.py` — тесты для виджета отображения операций;
* `tests/test_processing.py` — тесты для обработки транзакций;
* `tests/conftest.py` — фикстуры для тестовых данных.

### Покрытие кода

* Модуль `masks`: 90 %

## Новая функциональность

Добавлена поддержка чтения финансовых операций из разных форматов файлов:

* **JSON** — существующий формат (`read_json_file`)
* **CSV** — новый формат (`read_csv_file`)
* **Excel (.xlsx)** — новый формат (`read_excel_file`)

### Использование

```python
from src.utils import read_json_file
from src.file_readers import read_csv_file, read_excel_file

# Чтение из JSON
json_transactions = read_json_file("data/operations.json")

# Чтение из CSV
csv_transactions = read_csv_file("transactions.csv")

# Чтение из Excel
excel_transactions = read_excel_file("transactions_excel.xlsx")
