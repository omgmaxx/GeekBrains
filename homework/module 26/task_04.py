from _collections_abc import Iterable


class QHofstadter:
    """
    Итератор, возвращающий лист последовательности Хофштадтера

    Args:
        self.__given_list (list[int]): лист с двумя изначальными числами последовательности
        self.__length (int): требуемая длина последовательности

    """
    def __init__(self, given_list: list[int], length: int):
        self.__given_list = given_list
        self.__length = length - 2

    def __iter__(self) -> Iterable[list[int]]:
        self.__counter = 1
        return self

    def __next__(self) -> list[int]:
        if self.__counter > self.__length:
            raise StopIteration
        self.__counter += 1
        self.__given_list.append(
            self.__given_list[self.__counter - self.__given_list[self.__counter - 1]]
            + self.__given_list[self.__counter - self.__given_list[self.__counter - 2]]
        )
        return self.__given_list


def q_hofstadter(given_list: list[int], length: int) -> Iterable[list[int]]:
    """
    Генератор, возвращающий лист последовательности Хофштадтера

    :param given_list: лист с двумя изначальными числами последовательности
    :param length: требуемая длина последовательности
    :return: сгенерированная последовательность
    :rtype: Iterable[list[int]]
    """
    if given_list == [1, 1]:
        for count in range(2, length):
            given_list.append(
                given_list[count - given_list[count - 1]]
                + given_list[count - given_list[count - 2]]
            )
            yield given_list
        else:
            return str(given_list)
    else:
        return


q_start_2 = [1, 1]
for a in QHofstadter(q_start_2, 10):
    print(a)


q_start = [1, 1]
for y in q_hofstadter(q_start, 10):
    print(y)
