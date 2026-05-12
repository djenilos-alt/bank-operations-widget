import functools
import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Записывает в лог:
    - вызов функции с аргументами;
    - время выполнения;
    - результат или ошибку.

    Args:
        filename (Optional[str]): Имя файла для записи логов.
            Если None, логи выводятся в консоль.

    Returns:
        Callable: Обёрнутая функция с логированием.

    Examples:
        >>> @log()
        ... def add(a, b):
        ...     return a + b
        >>> add(2, 3)
        Вызов функции add(2, 3)
        Функция add успешно выполнена за 0.0001 сек. Результат: 5

        >>> @log("app.log")
        ... def divide(a, b):
        ...     return a / b
        >>> divide(10, 2)
        # Логи будут записаны в файл app.log
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Форматируем аргументы для логирования
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            log_message = f"Вызов функции {func.__name__}({signature})\n"

            # Определяем, куда выводить логи
            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(log_message)
            else:
                print(log_message)

            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time

                success_message = (
                    f"Функция {func.__name__} успешно выполнена за {execution_time:.4f} сек. "
                    f"Результат: {result!r}\n"
                )

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(success_message)
                else:
                    print(success_message)

                return result

            except Exception as e:
                end_time = time.time()
                execution_time = end_time - start_time
                error_message = (
                    f"Ошибка в функции {func.__name__}: {type(e).__name__}: {e}. "
                    f"Аргументы: {signature}. Время выполнения: {execution_time:.4f} сек.\n"
                )

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(error_message)
                else:
                    print(error_message)

                raise  # Перебрасываем исключение дальше

        return wrapper
    return decorator
