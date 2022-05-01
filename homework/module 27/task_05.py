from typing import Callable, Any
import functools


def counter(func: Callable, f_counter: dict = {}) -> Callable:
    """Декоратор, ведущий счёт вызовов обёрнутой функции"""

    @functools.wraps(func)
    def wrapping(*args, **kwargs) -> Any:
        if not f_counter.get(func.__name__):
            f_counter[func.__name__] = 1
        else:
            f_counter[func.__name__] += 1
        print('Функция [{}] вызвана {} раз'.format(func.__name__, f_counter[func.__name__]))

        result = func(*args, **kwargs)

        return result

    return wrapping


@counter
def test(num: int) -> int:
    """
    Функция, возвращающая данное число

    Args:
        num (int): число

    :return: число
    :rtype: int
    """
    return num


@counter
def test2(num: int) -> int:
    """
    Функция, возвращающая результат целочисленного деления числа на 10

    Args:
        num (int): делимое число

    :return: результат деления
    :rtype: int
    """
    return num // 10


for _ in range(15):
    print(test(999))

for _ in range(5):
    print(test2(999))

print(test(10))
