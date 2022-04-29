from random import randint


class House:
    """
        Базовый класс. Описывающий дом семьи.

        Attributes:
            __money (int): количество денег семьи
            __food (int): количество еды в доме
            __cat_food (int): количество кошачьей еды в доме
            __dirt (int): уровень грязи в доме (при 90+ падает счастье)
            __family (list): список членов семьи

    """
    def __init__(self):
        self.__money = 100
        self.__food = 50
        self.__cat_food = 30
        self.__dirt = 0
        self.__family = []

    def __str__(self):
        return '[Денег: {0}][Еды: {1}][К.Еды: {2}][Грязь: {3}]'.format(
                self.get_money(),
                self.get_food(),
                self.get_cat_food(),
                self.get_dirt()
            )

    def info(self):
        """
        Выдаёт информацию

        о статистике дома и всех членов семьи
        """
        print(self)
        [print(member) for member in self.__family]

    def get_family(self):
        """
        Геттер для получения списка членов семьи

        :return: список семьи
        :rtype: list
        """
        return self.__family

    def get_money(self):
        """
        Геттер для получения кол-ва денег в доме

        :return: деньги
        :rtype: int
        """
        return self.__money

    def get_food(self):
        """
        Геттер для получения кол-ва еды в доме

        :return: еда
        :rtype: int
        """
        return self.__food

    def get_cat_food(self):
        """
        Геттер для получения кол-ва кошачьей ды в доме

        :return: кошачья еда
        :rtype: int
        """
        return self.__cat_food

    def get_dirt(self):
        """
        Геттер для получения уровня грязи в доме

        :return: уровень грязи
        :rtype: int
        """
        return self.__dirt

    def set_money(self, money: int):
        """
        Сеттер для установления кол-ва денег семьи

        :param money: кол-во денег
        :type: int
        """
        self.__money = money

    def set_food(self, food: int):
        """
        Сеттер для установления кол-ва еды в доме

        :param food: кол-во еды
        :type: int
        """
        self.__food = food

    def set_cat_food(self, cat_food: int):
        """
        Сеттер для установления кол-ва кошачьей еды в доме

        :param cat_food: кол-во кошачьей еды
        :type: int
        """
        self.__cat_food = cat_food

    def set_dirt(self, dirt: int):
        """
        Сеттер для установления уровня грязи в доме

        :param dirt: уровень грязи
        :type: int
        """
        self.__dirt = dirt

    def add_family(self, family_member):
        """
        Добавляет члена семьи в список дома

        :param family_member: член семьи
        :type: FamilyMember
        """
        self.__family.append(family_member)


class FamilyMember:
    """
        Базовый класс. Описывает члена семьи.

        Args:
            name (str): передаётся имя члена семьи
            house (House): передаётся привязываемый дом

        Attributes:
            __name (str): имя члена семьи
            __satiety (int): уровень сытости
            __home (House): привязанный дом


    """
    def __init__(self, name: str, house: House):
        self.__name = name
        self.__satiety = 30
        self.__home = house
        self.__home.add_family(self)

    def __str__(self):
        return '[{}][Сытость: {}]'.format(
            self.get_name(),
            self.get_satiety()
        )

    def get_home(self):
        """
        Геттер для получения дома

        :return: дом
        :rtype: House
        """
        return self.__home

    def get_name(self):
        """
        Геттер для получения имени

        :return: имя
        :rtype: str
        """
        return self.__name

    def get_satiety(self):
        """
        Геттер для получения сытости

        :return: уровень сытости
        :rtype: int
        """
        return self.__satiety

    def set_satiety(self, satiety: int):
        """
        Сеттер для установления уровня сытости

        :param satiety: сытость
        :type: int
        """
        self.__satiety = satiety

    def eat(self):
        """
        Член семьи ест,

        потребляя до 30 еды, тратит соответствующее количество еды,
        соответственно повышает уровень сытости.
        """
        eaten = 30
        if self.get_home().get_food() < eaten:
            eaten = self.get_home().get_food()
        self.set_satiety(self.get_satiety() + eaten)
        self.get_home().set_food(self.get_home().get_food() - eaten)
        print('{} поел'.format(self.get_name()))


class Cat(FamilyMember):
    """
        Класс Кот. Родитель: FamilyMember

        Args:
            name (str): передаётся имя члена семьи
            house (House): передаётся привязываемый дом

        Attributes:
            self.__name (str): имя члена семьи
            self.__satiety (int): уровень сытости
            self.__home (House): привязанный дом


    """
    def __init__(self, name: str, house: House):
        super().__init__(name, house)

    def __str__(self):
        return '[Кот]' + super(Cat, self).__str__()

    def eat(self):
        """
        Кот ест,

        потребляя до 30 еды, тратит соответствующее количество еды,
        повышает уровень сытости двух кратно затраченной еде.
        """
        eaten = 10
        if self.get_home().get_cat_food() < eaten:
            eaten = self.get_home().get_cat_food()
        self.set_satiety(self.get_satiety() + eaten * 2)
        self.get_home().set_cat_food(self.get_home().get_cat_food() - eaten)
        print('{} поел'.format(self.get_name()))

    def sleep(self):
        """
        Кот спит

        ..
        """
        self.set_satiety(self.get_satiety() - 10)
        print('{} поспал'.format(self.get_name()))

    def tear_wallpaper(self):
        """
        Кот дерёт обои,

        уровень грязи в доме повышается на 5
        """
        self.get_home().set_dirt(self.get_home().get_dirt() + 5)
        self.set_satiety(self.get_satiety() - 10)
        print('{} подрал обои, +5 грязи'.format(self.get_name()))


class Human(FamilyMember):
    """
        Класс Человек. Родитель: FamilyMember

        Args:
            name (str): передаётся имя члена семьи
            house (House): передаётся привязываемый дом

        Attributes:
            self.__name (str): имя члена семьи
            self.__satiety (int): уровень сытости
            self.__home (House): привязанный дом

            __happiness (int): уровень счастья человека


    """
    def __init__(self, name: str, house: House):
        super().__init__(name, house)
        self.__happiness = 100

    def __str__(self):
        return super(Human, self).__str__() + '[Счастье: {}]'.format(str(self.get_happy()))

    def get_happy(self):
        """
        Геттер для получения уровня счастья человека

        :return: уровень счастья
        :rtype: int
        """
        return self.__happiness

    def set_happy(self, happy: int):
        """
        Сеттер для установления уровня счастья человека

        :param happy: уровень счастья
        :type: int
        """
        self.__happiness = happy
        if self.get_happy() > 100:
            self.__happiness = 100

    def pet_cat(self):
        """
        Человек гладит кота,

        счастье повышается на 5
        """
        self.set_happy(self.get_happy() + 5)
        self.set_satiety(self.get_satiety() - 10)
        print('{} погладил(а) кота, +5 счастья'.format(self.get_name()))


class Wife(Human):
    """
        Класс Жена. Родитель: Human

        Args:
            name (str): передаётся имя члена семьи
            house (House): передаётся привязываемый дом

        Attributes:
            self.__name (str): имя члена семьи
            self.__satiety (int): уровень сытости
            self.__home (House): привязанный дом
            self.__happiness (int): уровень счастья человека


    """
    def __init__(self, name: str, house: House):
        super().__init__(name, house)

    def buy_food(self):
        """
        Жена покупает еду,

        пока запасы не будут равны или больше 50,
        затем покупает кошачью еду, пока запасы не будут 30 или выше.
        При этом, закупается так, чтобы хватило хотя бы на одну порцию кошачьей еды.
        """
        while self.get_home().get_food() < 50 and self.get_home().get_money() > 20:
            self.get_home().set_money(self.get_home().get_money() - 10)
            self.get_home().set_food(self.get_home().get_food() + 10)
        while self.get_home().get_cat_food() < 80 and self.get_home().get_money() > 10:
            self.get_home().set_money(self.get_home().get_money() - 10)
            self.get_home().set_cat_food(self.get_home().get_cat_food() + 10)
        self.set_satiety(self.get_satiety() - 10)
        print('{} купила еду'.format(self.get_name()))

    def buy_coat(self):
        """
        Жена покупает шубу,

        что повышает уровень счастья на 60,
        тратит на это 350 денег.
        """
        self.set_happy(self.get_happy() + 60)
        self.get_home().set_money(self.get_home().get_money() - 350)
        self.set_satiety(self.get_satiety() - 10)
        print('{} купила шубу, +60 счастья -350 денег'.format(self.get_name()))

    def clean(self):
        """
        Жена убирает дом,

        опуская уровень грязи не более, чем на 100 единиц.
        """
        self.get_home().set_dirt(self.get_home().get_dirt() - 100)
        if self.get_home().get_dirt() < 0:
            self.get_home().set_dirt(0)
        self.set_satiety(self.get_satiety() - 10)
        print('{} сделала уборку'.format(self.get_name()))


class Husband(Human):
    """
        Класс Муж. Родитель: Human

        Args:
            name (str): передаётся имя члена семьи
            house (House): передаётся привязываемый дом

        Attributes:
            self.__name (str): имя члена семьи
            self.__satiety (int): уровень сытости
            self.__home (House): привязанный дом
            self.__happiness (int): уровень счастья человека


    """
    def __init__(self, name: str, house: House):
        super().__init__(name, house)

    def play(self):
        """
        Муж играет,

        Повышая уровень счастья
        """
        self.set_happy(self.get_happy() + 20)
        self.set_satiety(self.get_satiety() - 10)
        print('{} поиграл, +20 счастья'.format(self.get_name()))

    def work(self):
        """
        Муж работает,

        чем приносит 150 денег
        """
        self.get_home().set_money(self.get_home().get_money() + 150)
        self.set_satiety(self.get_satiety() - 10)
        print('{} поработал, +150 денег'.format(self.get_name()))


def death_check(house: House):
    """
    Проверка на условия смерти

    :param house: дом
    :return: bool
    """
    for family_member in house.get_family():
        if family_member.get_satiety() < 0:
            print('{} умер(ла) от голода'.format(family_member.get_name()))
            return True
        if isinstance(family_member, Human) and family_member.get_happy() < 10:
            print('{} умер(ла) от депрессии'.format(family_member.get_name()))
            return True


def dirt_check(house: House):
    """
    Проверка и начисления грязи

    :param house: дом
    """
    house.set_dirt(house.get_dirt() + 5)
    if house.get_dirt() > 90:
        for family_member in house.get_family():
            if isinstance(family_member, Human):
                family_member.set_happy(family_member.get_happy() - 10)


def daily_deeds(house):
    """
    Ежедневные действия членов семьи

    Жена:
        1) купить еды (еды в доме < 30 или кошачьей еды < 20)
        2) поесть (сытость < 40 и еды в доме > 0)
        3) купить шубу (денег > 400)
        4) убраться (1 к 5 или грязь > 90)
        5) погладить кота

    Муж:
        1) поесть (сытость < 40 и еды в доме > 0)
        2) работать (денег < 100)
        3) играть (счастье < 60)
        4) погладить кота (1 к 5)
        5) работать

    Кот:
        1) поесть (сытость < 20 и еды в доме > 0)
        2) подрать обои (1 к 4)
        3) спать

    :param house: дом
    """
    for family_member in house.get_family():

        # действие жены
        if isinstance(family_member, Wife):
            if house.get_food() < 30 or house.get_cat_food() < 20:
                family_member.buy_food()
            elif family_member.get_satiety() < 40 and house.get_food() > 0:
                family_member.eat()
            elif house.get_money() > 400:
                family_member.buy_coat()
            elif randint(1, 5) == 1 or house.get_dirt() > 90:
                family_member.clean()
            else:
                family_member.pet_cat()

        # действие мужа
        if isinstance(family_member, Husband):
            if family_member.get_satiety() < 40 and house.get_food() > 0:
                family_member.eat()
            elif house.get_money() < 100:
                family_member.work()
            elif family_member.get_happy() < 60:
                family_member.play()
            elif randint(1, 5) == 1:
                family_member.pet_cat()
            else:
                family_member.work()

        # действие кота
        if isinstance(family_member, Cat):
            if family_member.get_satiety() < 20 and house.get_cat_food() > 0:
                family_member.eat()
            elif randint(1, 4) == 1:
                family_member.tear_wallpaper()
            else:
                family_member.sleep()


home = House()
vasya = Husband(name='Вася', house=home)
lena = Wife(name='Лена', house=home)
snejok = Cat(name='Снежок', house=home)
barsik = Cat(name='Барсик', house=home)
murzik = Cat(name='Мурзик', house=home)
rizjik = Cat(name='Рыжик', house=home)
home.info()

# цикл дня
for day in range(365):
    print(f"\nDay {day + 1}")
    dirt_check(home)
    daily_deeds(home)
    home.info()
    if death_check(home):
        break
