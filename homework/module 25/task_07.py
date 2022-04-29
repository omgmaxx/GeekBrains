class Stack:
    """
    Базовый класс, представляющий собой стэк

    Args:
        *args: список объектов в порядке складывания стэка

    Attributes:
        __layers (list): аттрибут, содержащий в себе объекты стэка

    """
    def __init__(self, *args):
        self.__layers = []
        for arg in args:
            self.__layers.append(arg)

    def __str__(self):
        if len(self.__layers) > 0:
            return '|' * len(self.__layers) + str(self.__layers[-1])
        else:
            return 'None'

    def add(self, arg):
        """
        Метод, добавляющий объект на верх стэка

        :param arg: добавляемый объект
        :type: any
        """
        self.__layers.append(arg)

    def remove(self):
        """
        Метод, удаляющий верхний объект стэка

        :return: удаляемый объект
        """
        return self.__layers.pop(-1)


class TaskManager:
    """
    Базовый класс, представляющий собой менеджер задач

    Attributes:
        __tasks (dict): аттрибут, содержащий в себе объекты менеджера

    """
    def __init__(self):
        self.__tasks = {}

    def __str__(self):
        return '\n'.join('{} {}'.format(
            str(key),
            '; '.join(self.get_priority(key))
        )
                         for key in sorted(self.__tasks.keys())
                         )

    def new_task(self, task: str, priority: int):
        """
        Метод, добавляющий задачу на определённый приоритет

        Если задача повторяется - она игнорируется

        :param task: задача
        :param priority: приоритет
        """
        for task_list in self.__tasks.values():
            if task in task_list:
                return

        if self.__tasks.get(priority):
            self.__tasks[priority].append(task)
        else:
            self.__tasks[priority] = [task]

    def clear(self, priority: int):
        """
        Метод, очищающий задачи по приоритету

        :param priority: приоритет
        :type: int
        """
        self.__tasks.pop(priority)

    def remove(self, task: str):
        """
        Метод, удаляющий задачу

        если приоритет остаётся пустым - убирает его

        :param task: задача
        :type: str
        """
        for key, task_list in self.__tasks.items():
            if task in task_list:
                task_list.remove(task)
                if not task_list:
                    self.clear(key)
                    return

    def get_priority(self, priority: int):
        """
        Геттер для получения задач по приоритету

        :param priority: приоритет
        :type: int
        """
        return self.__tasks.get(priority)


stack = Stack()
for x in range(1, 6):
    stack.add(x)
    print(stack)
print()
for _ in range(5):
    stack.remove()
    print(stack)

print('=========')

manager = TaskManager()
manager.new_task('сделать уборку', 4)
manager.new_task('помыть посуду', 4)
manager.new_task('отдохнуть', 1)
manager.new_task('отдохнуть', 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
print()

manager.clear(4)
manager.remove('поесть')
manager.remove('отдохнуть')
print(manager)
