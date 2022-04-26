class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.child_list = []

    def comfort(self, child):
        if child in self.child_list:
            child.is_calm = True
            print('Вы успокоили ребёнка по имени {}.\n'.format(child.name))
        else:
            print('{} - не ваш ребёнок. Не трогайте чужих детей.\n'.format(child.name))

    def feed(self, child):
        if child in self.child_list:
            child.is_fed = True
            print('Вы покормили ребёнка по имени {}.\n'.format(child.name))
        else:
            print('{} - не ваш ребёнок. Не кормите чужих детей.\n'.format(child.name))

    def info(self):
        print('Меня зовут {}\nМне {} лет\nМоих детей зовут: {}.\n'.format(
            self.name,
            self.age,
            ', '.join([x.name for x in self.child_list])
        ))


class Child:

    def __init__(self, name, age, parent):
        self.name = name
        self.age = age
        self.is_calm = False
        self.is_fed = False
        if self.age < parent.age - 18:
            parent.child_list.append(self)
        else:
            print('Судя по возрасту, {} явно не ребёнок человека по имени {}.\n'.format(
                self.name,
                parent.name
            ))

    def state(self):
        if self.is_fed and self.is_calm:
            print('С {} всё хорошо!'.format(self.name))

        if not self.is_fed:
            print(self.name, 'голоден')
        if not self.is_calm:
            print(self.name, 'плачет')
        print()


parent = Parent('Олег', 37)

parent.info()
child_1 = Child('Ваня', 10, parent)
child_2 = Child('Саша', 15, parent)
child_3 = Child('Гриша', 35, parent)
print(40*'-')

parent.info()
print(40*'-')

parent.comfort(child_1)
parent.feed(child_1)
parent.feed(child_2)
parent.feed(child_3)
print(40*'-')

child_1.state()
child_2.state()
child_3.state()
