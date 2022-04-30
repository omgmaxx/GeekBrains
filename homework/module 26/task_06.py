from typing import Optional, Any
from _collections_abc import Iterable


class LinkedList:
    """
    Структура данных. Односвязный список

    Каждый узел имеет значение и привязку к следующему узлу

    Attributes:
        self.__head (Node): головной узел
        self.length (int): длина списка

    """
    def __init__(self) -> None:
        self.__head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.__head is not None:
            current = self.__head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList []'

    def __iter__(self) -> Iterable[str]:
        self.index = 0
        return self

    def __next__(self) -> str:
        cur_node = self.__head
        cur_index = 0
        if self.length == 0 or self.length < self.index:
            raise StopIteration

        while cur_node is not None:
            if cur_index == self.index:
                break
            cur_node = cur_node.next
            cur_index += 1

        self.index += 1

        if cur_node.next:
            return f'Узел {cur_node.value}, следующий узел {cur_node.next.value}'
        else:
            return f'Замыкающий узел: {cur_node.value}'

    def append(self, element: Any) -> None:
        """
        Метод, добавляющий новый узел в конец списка

        :param element: добавляемый элемент
        :return: None
        :type: Any
        """
        new_node = Node(element)
        if self.__head is None:
            self.__head = new_node
            return
        last = self.__head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index) -> None:
        """
        Метод, удаляющий объект под указанным индексом

        Перепривязывает соседние элементы

        :param index: индекс удаляемого объекта
        :return: None
        :type: int
        """
        cur_node = self.__head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.__head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.length -= 1

    def get(self, index) -> Any:
        """
        Метод, возвращающий объект под указанным индексом

        :param index: индекс возвращаемого объекта
        :return: объект
        :rtype: Any
        """
        cur_node = self.__head
        cur_index = 0

        if self.length == 0 or self.length < index:
            raise IndexError

        while cur_node is not None:
            if cur_index == index:
                break
            cur_node = cur_node.next
            cur_index += 1

        return cur_node


class Node:
    """
    Узел структуры данных LinkedList

    Args:
        self.next (Optional[Node]): следующий элемент
        self.value (Optional[None]): содержание узла

    """
    def __init__(self, value: Optional[None] = None, next_node: Optional['Node'] = None) -> None:
        self.next = next_node
        self.value = value

    def __str__(self) -> str:
        return 'Node [{value}]'.format(value=str(self.value))


my_list = LinkedList()
my_list.append(10)
my_list.append(30)
my_list.append(3)
my_list.append(0)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print(my_list.length)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
print()
for x in my_list:
    print(x)
