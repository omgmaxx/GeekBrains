import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator):
    def decorator_maker(*args, **kwargs):
        def wrapping(func):
            return decorator(func, *args, **kwargs)
        return wrapping
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs):
    @functools.wraps(func)
    def wrapping(*func_args, **func_kwargs):
        print(dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)
    return wrapping


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)