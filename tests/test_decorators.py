import pytest
from src.decorators import log


class TestLogDecorator:
    @pytest.fixture
    def temp_log_file(self, tmp_path):
        """Фикстура для временного файла логов."""
        file_path = tmp_path / "test_log.txt"
        yield file_path
        # Очистка после теста
        if file_path.exists():
            file_path.unlink()

    def test_log_to_console_success(self, capsys):
        """Тест логирования успешного выполнения в консоль."""
        @log()
        def add(a, b):
            return a + b

        result = add(5, 3)
        captured = capsys.readouterr()

        assert "Вызов функции add(5, 3)" in captured.out
        assert "успешно выполнена за" in captured.out
        assert "Результат: 8" in captured.out
        assert result == 8

    def test_log_to_file_success(self, temp_log_file):
        """Тест логирования успешного выполнения в файл."""
        @log(filename=str(temp_log_file))
        def multiply(x, y):
            return x * y

        multiply(4, 7)

        with open(temp_log_file, 'r', encoding='utf-8') as f:
            content = f.read()

        assert "Вызов функции multiply(4, 7)" in content
        assert "успешно выполнена за" in content
        assert "Результат: 28" in content

    def test_log_exception_to_console(self, capsys):
        """Тест логирования исключений в консоль."""
        @log()
        def divide(a, b):
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

        captured = capsys.readouterr()
        assert "Ошибка в функции divide" in captured.out
        assert "ZeroDivisionError" in captured.out
        assert "Аргументы: 10, 0" in captured.out

    def test_log_exception_to_file(self, temp_log_file):
        """Тест логирования исключений в файл."""
        @log(filename=str(temp_log_file))
        def problematic_function(value):
            if value < 0:
                raise ValueError("Отрицательное значение")
            return value ** 2

        with pytest.raises(ValueError):
            problematic_function(-5)

        with open(temp_log_file, 'r', encoding='utf-8') as f:
            content = f.read()

        assert "Ошибка в функции problematic_function" in content
        assert "ValueError: Отрицательное значение" in content
        assert "Аргументы: -5" in content

    def test_function_with_kwargs(self, capsys):
        """Тест функции с именованными аргументами."""
        @log()
        def greet(name, greeting="Привет"):
            return f"{greeting}, {name}!"

        result = greet("Анна", greeting="Здравствуйте")
        captured = capsys.readouterr()
        assert "Вызов функции greet('Анна', greeting='Здравствуйте')" in captured.out
        assert "Результат: 'Здравствуйте, Анна!'" in captured.out
        assert result == "Здравствуйте, Анна!"

    def test_empty_arguments(self, capsys):
        """Тест функции без аргументов."""
        @log()
        def get_random():
            import random
            return random.randint(1, 100)

        result = get_random()
        captured = capsys.readouterr()

        assert "Вызов функции get_random()" in captured.out
        assert f"Результат: {result!r}" in captured.out

    def test_multiple_calls_same_function(self, temp_log_file):
        """Тест множественных вызовов одной функции."""
        @log(filename=str(temp_log_file))
        def square(x):
            return x ** 2

        square(2)
        square(3)
        square(4)

        with open(temp_log_file, 'r', encoding='utf-8') as f:
            content = f.read()

        assert content.count("Вызов функции square") == 3
        assert "Результат: 4" in content
        assert "Результат: 9" in content
        assert "Результат: 16" in content

    def test_nested_decorated_functions(self, capsys):
        """Тест вложенных декорированных функций."""
        @log()
        def outer_function(x):
            @log()
            def inner_function(y):
                return y * 2
            return inner_function(x) + 1

        result = outer_function(5)
        captured = capsys.readouterr()

        assert "Вызов функции outer_function(5)" in captured.out
        assert "Вызов функции inner_function(5)" in captured.out
        assert "Результат: 11" in captured.out
        assert result == 11

    def test_decorator_with_none_filename(self, capsys):
        """Тест декоратора с filename=None."""
        @log(filename=None)
        def test_func():
            return "test"

        test_func()
        captured = capsys.readouterr()

        assert "Вызов функции test_func()" in captured.out
        assert "Результат: 'test'" in captured.out
