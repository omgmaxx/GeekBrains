class MyDict:
    """
    Базовый класс, представляющий собой словарь

    Args:
        **kwargs: кортеж ключей=значений

    Attributes:
        __my_dict (dict): аттрибут, содержащий в себе объекты словаря
    """
    def __init__(self, **kwargs):
        self.__my_dict = {}
        for key, value in kwargs.items():
            self.__my_dict[key] = value

    def __str__(self):
        return '{'+', '.join({f"'{key}': {value}" for key, value in self.__my_dict.items()})+'}'

    def get(self, __key: str):
        """
        Геттер для получения значения ключа

        если ключа нет - возвращает 0

        :param __key:
        :return: значение
        :type: str
        :rtype: str
        """
        if __key in self.__my_dict:
            return self.__my_dict[__key]
        else:
            return 0

    def items(self):
        """
        Метод, возвращающий список кортежей (ключ, значение) словаря

        :return: список кортежей (ключ, значение)
        :rtype: list
        """
        return [(key, value) for key, value in self.__my_dict.items()]

    def keys(self):
        """
        Метод, возвращающий список ключей словаря

        :return: список ключей
        :rtype: list
        """
        return [key for key in self.__my_dict.keys()]

    def values(self):
        """
        Метод, возвращающай список значений словаря

        :return: список значений
        :rtype: list
        """
        return [value for value in self.__my_dict.values()]

    def pop(self, __key: str):
        """
        Метод, опустошающий значение по ключу

        возвращает значение ключа

        :param __key: ключ
        :return: значение
        :type: key
        :rtype: list
        """
        return self.__my_dict.pop(__key)


custom_dictionary = MyDict(c=3, d=4)
print(custom_dictionary)
print(custom_dictionary.get('c'))
print(custom_dictionary.get('a'))
