from _collections_abc import Iterable


def look_for(list_1: list[int], list_2: list[int], to_find: int) -> Iterable[str]:
    """
    Генератор, находящий заданное число

    перемножая по очереди между собой числа из списков

    :param list_1: первый список
    :param list_2: второй список
    :param to_find: искомое число
    :return: выражения перемножений
    """
    for x in list_1:
        for y in list_2:
            result = x * y
            yield f'{x} * {y} = {result}'
            if result == to_find:
                yield 'Found!!!'
                return


list_one = [2, 5, 7, 10]
list_two = [3, 8, 4, 9]

lk_for = look_for(list_one, list_two, to_find=56)
for expression in lk_for:
    print(expression)
