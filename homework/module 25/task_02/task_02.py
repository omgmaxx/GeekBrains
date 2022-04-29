from random import randint
from time import sleep


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class Monk:
    """
    Базовый класс, описывающий программиста-буддиста

    exception_list: список ошибок, которые могут возникнуть вместо получения кармы за день

    Attributes:
        __karma (int): карма монаха
        __target_karma (int): требуемая карма
        __day (int): счётчик дней

    """
    exception_list = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]

    def __init__(self):
        self.__karma = 0
        self.__target_karma = 500
        self.__day = 0

    def __str__(self):
        return 'Day {}) {} karma'.format(self.get_day(), self.get_karma())

    def get_karma(self):
        """
        Геттер для получения кармы

        :return: карма монаха
        :rtype: int
        """
        return self.__karma

    def get_target_karma(self):
        """
        Геттер для получения целевой кармы

        :return: целевая карма
        :rtype: int
        """
        return self.__target_karma

    def get_day(self):
        """
        Геттер для получения дня

        :return: день
        :rtype: int
        """
        return self.__day

    def set_karma(self, karma):
        """
        Сеттер для установления кармы

        :param karma: карма монаха
        :type: int
        """
        self.__karma = karma

    def one_day(self):
        """
        Проведение результатов дня: либо начисление кармы, либо выдача ошибки.
        Создаёт karma.log со списком ошибок.

        :return: возвращает текст результатов дня в формате [день) карма]
        :rtype: str
        :raise Exception: возвращает случайную ошибку из списка с шансом 1 к 10
        """
        self.__day += 1
        try:
            if randint(1, 10) == 1:
                raise self.exception_list[randint(0, 4)]
            self.set_karma(self.get_karma() + randint(1, 7))
        except Exception as error:
            with open('karma.log', 'a') as log:
                log.write(
                    'Day {}) '.format(self.get_day())+(str(repr(error))+'\n')
                          )


open('karma.log', 'w').close()
buddist = Monk()
while True:
    sleep(0.03)
    if buddist.get_karma() >= buddist.get_target_karma():
        break
    buddist.one_day()
    print(buddist)
