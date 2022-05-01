from typing import Callable, Any, Optional
import functools


def debug(func: Callable) -> Callable:
    """
    Декоратор-дебаггер, выдающая название, аргументы и возвращаемое значение и класс функции
    """
    @functools.wraps(func)
    def wrapping(*args, **kwargs) -> Any:

        result = func(*args, **kwargs)

        print()
        print('Название функции: ' + func.__name__)
        print('Аргументы: [' + '] ['.join(
            [arg for arg in args]
            + [f'{key}={str(kwarg)}' for key, kwarg in kwargs.items()])
            + ']'
              )
        print(f'Возвращает объекты класса: [{func.__annotations__["return"].__name__}]')
        print(f'Возвращает значение: {result}')
        print(' {:=^70} '.format('  Результат  '))

        return result

    return wrapping


@debug
def greeting(name: str, age: Optional[int] = None) -> str:
    """Функция, возвращающая приветствие

    Args:
        name (str): имя
        age (int): возраст

    :return: приветствие
    :rtype: str
    """
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print(greeting("Том"))
print(greeting("Миша", age=100))
print(greeting(name="Катя", age=16))

print(repr(greeting))
