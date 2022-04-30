from _collections_abc import Iterable


class Squares:
    """
    Итератор, выдающий квадраты чисел до целевого

    Args:
        target (int): целевое значение

    Attributes:
        __target (int): целевое значение
        __count (int): счётчик

    """
    def __init__(self, target: int) -> None:
        self.__target = target
        self.__count = 0

    def __iter__(self) -> Iterable[int]:
        self.__count = 0
        return self

    def __next__(self) -> int:
        self.__count += 1
        if self.__count > self.__target:
            raise StopIteration
        return self.__count ** 2


def squares(target: int) -> Iterable[int]:
    """
    Генератор, выдающий квадраты чисел до целевого

    :param target: целевое значение
    :return: квадраты чисел
    :rtype: Iterable[int]
    """
    for numb in range(1, target+1):
        yield numb ** 2


numbers_limit = int(input('Введите число, до которого умножать: '))

for x in Squares(numbers_limit):
    print(x, end=' ')

print()
for x in squares(numbers_limit):
    print(x, end=' ')

print()
[print(x ** 2, end=' ') for x in range(1, numbers_limit + 1)]
