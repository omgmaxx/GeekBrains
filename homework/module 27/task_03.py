from typing import Callable, Any
import functools
import datetime


def logging(func: Callable) -> Callable:
    """Декоратор, логгирующий название, документацию и время вызова функции

    Записывает отчёт об ошибке в файл function_errors.log"""

    @functools.wraps(func)
    def wrapping(*args, **kwargs) -> Any:
        time = datetime.datetime.now().isoformat(' ', 'seconds')

        print('{0}\n'
              '{1}\n'
              'Время вызова функции: {2}'.format(func.__name__, func.__doc__, time))

        try:

            result = func(*args, **kwargs)
            print('=' * 50)
            return result

        except Exception as e:

            with open('function_errors.log', 'a', encoding='utf-8') as log:
                log.write(f'[Error] При вызове функции {func.__name__} возникла ошибка: {e}.'
                          f'\nВремя запроса: {time}\n\n')
                print('+' * 50)
                print(f'[Error] Возникла ошибка: {e}.')
                print('+' * 50)

    return wrapping


@logging
def test_function(num: int) -> float:
    """
    Функция, возвращающая число, поделенное на 10

    Args:
        num (int): делимое число

    :return: результат деления
    :rtype: float
    """
    x = 10 / num
    return x


test_function(10)
test_function(0)
test_function([15, 5])
