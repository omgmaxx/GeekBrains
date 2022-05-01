from typing import Callable, Any
import functools
from time import sleep


def wait(func: Callable) -> Callable:
    """Декоратор, добавляющий задержку перед исполнением функции"""
    @functools.wraps(func)
    def wrapping(*args, **kwargs) -> Any:
        sleep(1)
        result = func(*args, **kwargs)
        return result

    return wrapping


@wait
def test(num: int) -> int:
    """
    Функция, возвращающая число возведённым в 10 степень

    Args:
        num (int): число, возводимое в степень

    :return: результат возведения
    :rtype: int
    """
    return num ** 10


for _ in range(10):
    print(test(10))
