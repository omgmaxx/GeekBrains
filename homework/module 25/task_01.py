class Property:
    """
    Базовый класс, описывающий Имущество

    Args:
        worth (int): передаётся стоимость имущества

    Attributes:
        __tax (float): налог на имущество (в дробях)

    """
    def __init__(self, worth: int):
        self.__worth = worth
        self.__tax = 0

    def get_worth(self):
        """
        Геттер для получения стоимости имущества

        :return: __worth
        :rtype: int
        """
        return self.__worth

    def get_tax(self):
        """
        Геттер для получения налога

        :return: __tax
        :rtype: float
        """
        return self.__tax

    def set_worth(self, new_worth):
        """
        Сеттер для установления стоимости им-ва

        :param new_worth: новая стоимость
        :type new_worth: int
        """
        self.__worth = new_worth

    def set_tax(self, tax):
        """
        Сеттер для установления налога

        :param tax: налог
        :type tax: float
        """
        self.__tax = tax

    def calc_tax(self):
        """
        Метод для подсчёта налога на объект имущества

        :return: налог на объект
        :rtype: float
        """
        return self.get_tax() * self.get_worth()


class Apartment(Property):
    """
    Класс Квартира. Родитель: Property

    Args:
        worth (int): передаётся стоимость имущества

    Attributes:
        self.__tax (float): налог на имущество (в дробях)

    """
    def __init__(self, worth):
        super().__init__(worth)
        self.set_tax(1 / 1000)


class Car(Property):
    """
    Класс Машина. Родитель: Property

    Args:
        worth (int): передаётся стоимость имущества

    Attributes:
        self.__tax (float): налог на имущество (в дробях)

    """
    def __init__(self, worth):
        super().__init__(worth)
        self.set_tax(1 / 200)


class ContryHouse(Property):
    """
    Класс Дача. Родитель: Property

    Args:
        worth (int): передаётся стоимость имущества

    Attributes:
        self.__tax (float): налог на имущество (в дробях)

    """
    def __init__(self, worth):
        super().__init__(worth)
        self.set_tax(1 / 500)


def ask_for_prop():
    """
    Запрашивает стоимость имущества, возвращает налог на него

    :return: налог на записанное имущество
    :rtype: float
    """
    total_tax = 0
    total_tax += Apartment(
        int(input('Стоимость квартиры: '))
    ).calc_tax()

    total_tax += Car(
        int(input('Стоимость машины: '))
    ).calc_tax()

    total_tax += ContryHouse(
        int(input('Стоимость дачи: '))
    ).calc_tax()
    return total_tax


def is_enough():
    """
    Метод, выводящий, достаточно ли денег для оплаты налога


    Запрашивает количество денег,
    сравнивает с налогом на указанное в функции ask_for_pop() налогом

    """
    money = int(input('Сколько у вас денег? '))
    tax = ask_for_prop()
    if money < tax:
        print("Недостаточно денег для оплаты налога!")
    else:
        money -= tax
        print("Денег хватило! Осталось:", money)


is_enough()
