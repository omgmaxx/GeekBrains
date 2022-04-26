from random import randint


class Student:

    def __init__(self, name, surname, group, grades):
        self.nm_srnm = ' '.join((name, surname))
        self.group = group
        self.grades = list(grades)

    def info(self):
        print('{:<30} || {:^9} || {:>25}'.format(
            f'Студент: {self.nm_srnm}',
            f'Группа: {self.group}',
            f'Оценки: {self.grades}')
        )


names = ['Олег', 'Ваня', 'Максим', 'Никита', 'Дмитрий']
surnames = ['Смирнов', 'Иванов', 'Зайцев', 'Кузнецов', 'Краснов']

students = {index: Student(                 # генерация списка студентов
    names[randint(0, 4)],
    surnames[randint(0, 4)],
    randint(1, 2),
    [randint(1, 5) for _ in range(5)])

    for index in range(1, 11)
}

for _ in range(2):                           # отчисления
    students[randint(1, 10)] = ''

for std in students.values():
    if isinstance(std, Student):
        std.info()
    else:
        print('X {:-^68} X'.format('  Отчислен  '))
