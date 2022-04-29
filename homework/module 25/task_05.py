import math

class Car:
    """
        Базовый класс, описывающий машину

        Args:
            __coords (list): Координаты [x, y]
            __angle (int): Угол поворота

    """
    def __init__(self, coord_x: int, coord_y: int, angle: int):
        self.__coords = [coord_x, coord_y]
        self.__angle = angle

    def __str__(self):
        return 'Машина расположена на координатах {}, с углом {}'.format(
            self.get_coords(),
            self.get_angle()
        )

    def get_coords(self):
        """
        Геттер для получения координат машины

        :return: координаты [x, y]
        :rtype: list
        """
        return self.__coords

    def get_angle(self):
        """
        Геттер для получения угла направления машины

        :return: угол (в градусах)
        :rtype: int
        """
        return self.__angle

    def set_coords(self, coord_x: int, coord_y: int):
        """
        Сеттер для установления координат машины

        :param coord_x: координата X
        :param coord_y: координата Y
        :type: int -> list
        """
        self.__coords = [coord_x, coord_y]

    def set_angle(self, angle: int):
        """
        Сеттер для установления угла направления машины

        :param angle: угол (в градусах)
        :type: int
        """
        old_angle = self.get_angle()
        self.__angle = (old_angle + angle) % 360

    def move(self, move: int):
        """
        Перемещение машины в единицах длины в зависимости
        от нынешнего угла поворота

        :param move: движение в единицах длины
        :type: int
        """
        [x, y] = self.get_coords()
        angle = self.get_angle()
        x = round(x + move * math.cos(math.radians(angle)), 2)
        y = round(y + move * math.sin(math.radians(angle)), 2)
        self.set_coords(x, y)


class Bus(Car):
    """
        Класс автобус. Родитель: Car

        Args:
            __coords (list): Координаты [x, y]
            __angle (int): Угол поворота

            __passengers (int): Количество пассажиров
            __money (int): Выручка автобуса

    """
    def __init__(self, coord_x: int, coord_y: int, angle: int):
        super().__init__(coord_x, coord_y, angle)
        self.__passengers = 0
        self.__money = 0

    def __str__(self):
        return ''.join((super().__str__(), '\nЗагрузка - {} человек.\tЗаработано {}'.format(
            self.get_passengers(),
            self.get_money()
        )))

    def get_passengers(self):
        """
        Геттер для получения пассажиров

        :return: пассажиры
        :rtype: int
        """
        return self.__passengers

    def get_money(self):
        """
        Геттер для получения выручки автобуса

        :return: выручка
        :rtype: int
        """
        return self.__money

    def set_money(self, money: int):
        """
        Сеттер для установления выручки

        :param money: выручка
        :type: int
        """
        self.__money += money

    def pas_enter(self, pas_amt: int):
        """
        Вход пассажиров в автобус

        :param pas_amt: количество пассажиров
        :type: int
        """
        if self.__passengers < 10:
            self.__passengers += pas_amt
            if self.__passengers > 10:
                self.__passengers = 10
                print('Все пассажиры не поместились.')
        else:
            print('Автобус переполнен!')

    def pas_exit(self):
        """
        Выход пассажиров из автобуса
        """
        if self.get_passengers() > 0:
            self.__passengers = 0
        else:
            print('Пассажиров нет.')

    def move(self, move: int):
        """
        Перемещение машины в единицах длины в зависимости
        от нынешнего угла поворота,

        выручка от количества
        пассажиров, в зависимости от дальности перемещения

        :param move: движение в единицах длины
        :type: int
        """
        super().move(move)
        self.set_money(self.get_passengers() * move * 10)


bus = Bus(0, 0, 0)
print(bus)
bus.pas_enter(10)
bus.move(100)
print(bus)
bus.pas_exit()
print(bus)
bus.pas_enter(1)
bus.set_angle(50)
bus.move(1000)
print(bus)
