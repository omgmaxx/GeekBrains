class Person:
    """
    Базовый класс, описывающий человека

    Args:
        self.__name (str): Имя
        self.__surname (str): Фамилия
        self.__age (int): Возраст

    """
    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return '{} {}'.format(self.get_name(), self.get_surname())

    def get_name(self):
        """
        Геттер для получении имени

        :return: имя
        :rtype: str
        """
        return self.__name

    def get_surname(self):
        """
        Геттер для получения фамилии

        :return: фамилия
        :rtype: str
        """
        return self.__surname

    def get_age(self):
        """
        Геттер для получения возраста

        :return: возраст
        :rtype: int
        """
        return self.__age


class Employee(Person):
    """
    Класс Работник. Родитель: Person

    Args:
        self.__name (str): Имя
        self.__surname (str): Фамилия
        self.__age (int): Возраст

    """
    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname, age)

    def calc_salary(self):
        """
        Метод, возвращающий зарплату работника

        :return: зарплата
        :rtype: int/float
        """
        pass


class Manager(Employee):
    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname, age)

    def calc_salary(self):
        """
        Метод, возвращающий зарплату работника

        :return: зарплата
        :rtype: int/float
        """
        return 13000


class Agent(Employee):
    def __init__(self, name: str, surname: str, age: int, sales: int):
        super().__init__(name, surname, age)
        self.__sales = sales

    def get_sales(self):
        """
        Геттер для получения продаж агента

        :return: продажи
        :rtype: int
        """
        return self.__sales

    def set_sales(self, sales: int):
        """
        Сеттер для установления продаж агента

        :param sales: продажи
        :type sales: int
        """
        self.__sales = sales

    def calc_salary(self):
        """
        Метод, возвращающий зарплату работника

        :return: зарплата
        :rtype: int/float
        """
        return round(5000 + 0.05 * self.get_sales())


class Worker(Employee):
    def __init__(self, name: str, surname: str, age: int, hours: int):
        super().__init__(name, surname, age)
        self.__hours = hours

    def get_hours(self):
        """
        Сеттер для установления рабочих часов работника

        :return: часы
        :rtype: int
        """
        return self.__hours

    def set_hours(self, hours: int):
        """
        Сеттер для установления рабочих часов работника

        :param hours: часы
        :type hours: int
        """
        self.__hours = hours

    def calc_salary(self):
        """
        Метод, возвращающий зарплату работника

        :return: зарплата
        :rtype: int/float
        """
        return 100 * self.get_hours()


worker_vasya = Worker(name="Вася", surname="Смирнов", age=34, hours=176)
worker_oleg = Worker(name="Олег", surname="Кузнецов", age=45, hours=150)
worker_petya = Worker(name="Петя", surname="Гребенщиков", age=26, hours=122)

agent_nina = Agent(name="Нина", surname="Лебедева", age=33, sales=120000)
agent_misha = Agent(name="Михаил", surname="Третьяков", age=42, sales=180000)
agent_andrey = Agent(name="Андрей", surname="Поляков", age=55, sales=115000)

manager_nadya = Manager(name="Надя", surname="Воронова", age=22)
manager_ivan = Manager(name="Иван", surname="Жуков", age=37)
manager_alisa = Manager(name="Алиса", surname="Власова", age=46)

for employee in [
    worker_vasya, worker_petya, worker_oleg,
    agent_nina, agent_andrey, agent_misha,
    manager_nadya, manager_alisa, manager_ivan
]:
    print('{} заработал {:,} за месяц'.format(
        employee,
        employee.calc_salary())
    )
