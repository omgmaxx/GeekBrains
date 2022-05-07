import functools
import time
from typing import Callable
import datetime


def logging(func: Callable, date: str, name: str) -> Callable:
    def wrapped(*args, **kwargs):
        start_time = time.time()

        time_format = ''
        for x in date:
            if x.isalpha():
                time_format += '%'
            time_format += x

        print(f'Запускается {name}.{func.__name__}. Дата и время запуска: {datetime.datetime.utcnow().strftime(time_format)}')
        res = func(*args, **kwargs)
        print(f'Завершение {name}.{func.__name__}, время работы = {round(time.time() - start_time, 3)}s')

        return res
    return wrapped


def log_methods_decor(date: str) -> Callable:
    @functools.wraps(logging)
    def decorate(cls):
        for i_method in dir(cls):
            if not i_method.startswith('__'):
                method = getattr(cls, i_method)
                decorated_method = logging(method, date, cls.__name__)
                setattr(cls, i_method, decorated_method)
        return cls
    return decorate


@log_methods_decor("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods_decor("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
