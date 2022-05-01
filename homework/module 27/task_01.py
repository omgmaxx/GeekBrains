from typing import Callable
import functools


def how_are_you(func: Callable) -> Callable:
    """Декоратор, спрашивающий, как дела"""
    print('Как дела? Хорошо.')
    print('А у меня не очень! Ладно, держи свою функцию.')

    # можно было без обёртки, но по заданию нужен functools
    @functools.wraps(func)
    def wrapping():
        return func()
    return wrapping


@how_are_you
def test() -> None:
    """Функция, в которой что-то происходит"""
    print('<Тут что-то происходит...>')


test()
