from src.readers import read_csv_transactions
from src.readers import read_excel_transactions
from src.search_operations import process_bank_search


def main() -> None:
    """Запускает пользовательский интерфейс программы обработки транзакций."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    data = []

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        # Логика обработки JSON
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        data = read_csv_transactions("transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        data = read_excel_transactions("transactions.xlsx")
    else:
        print("Неверный выбор. Завершение программы.")
        return

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные статусы: {', '.join(valid_statuses)}")

        status = input("Пользователь: ").upper()

        if status in valid_statuses:
            print(f'Операции отфильтрованы по статусу "{status}"')

            filtered_data = [
                transaction
                for transaction in data
                if transaction.get("status", "").upper() == status
            ]
            break

        print(f'Статус операции "{status}" недоступен.')

    sort_choice = input(
        "Отсортировать операции по дате? Да/Нет\nПользователь: "
    ).lower()

    if sort_choice == "да":
        order = input(
            "Отсортировать по возрастанию или по убыванию?\nПользователь: "
        ).lower()

        reverse = order == "по убыванию"

        filtered_data.sort(
            key=lambda transaction: transaction.get("date", ""),
            reverse=reverse,
        )

    rub_choice = input(
        "Выводить только рублевые транзакции? Да/Нет\nПользователь: "
    ).lower()

    if rub_choice == "да":
        filtered_data = [
            transaction
            for transaction in filtered_data
            if "руб" in str(transaction.get("amount", "")).lower()
        ]

    search_choice = input(
        "Отфильтровать список транзакций по слову в описании? Да/Нет\n"
        "Пользователь: "
    ).lower()

    if search_choice == "да":
        search_term = input("Введите слово для поиска:\nПользователь: ")

        filtered_data = process_bank_search(
            filtered_data,
            search_term,
        )

    print("Распечатываю итоговый список транзакций...")

    if not filtered_data:
        print(
            "Не найдено ни одной транзакции, "
            "подходящей под условия фильтрации."
        )
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_data)}")

        for transaction in filtered_data:
            description = transaction.get("description", "Неизвестно")
            amount = transaction.get("amount", "Неизвестно")

            print(f"\n{description}")
            print(f"Сумма: {amount}")


if __name__ == "__main__":
    main()
