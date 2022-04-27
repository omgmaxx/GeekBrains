from random import randint
from time import sleep


class Potato:
    states = {0: 'Только посажена', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            if randint(1, 3) != 1:
                self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self):
        self.potatoes = []

    def grow_all(self):
        print('\nКартошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            return False
        else:
            print('Вся картошка созрела - можно собирать!')
            return True


class Farmer:

    def __init__(self, name: str, garden: PotatoGarden):
        self.name = name
        self.garden = garden
        self.stockpile = 0

    def care(self, count=0):
        if not self.garden.potatoes:
            self.garden.potatoes = [Potato(index) for index in range(1, count + 1)]
            print('\n{} посадил {} картофелин.'.format(self.name, count))
        elif self.garden.are_all_ripe():
            self.reap()
        else:
            print('{} избавился от сорняков.'.format(self.name))
            self.garden.grow_all()

    def reap(self):
        for i_potato in self.garden.potatoes:
            if i_potato.state == 3:
                self.stockpile += 1
        self.garden.potatoes = []
        print('\n{} собрал урожай картошки. На складе сейчас {} картофелин.'.format(self.name, self.stockpile))


my_garden = PotatoGarden()
farmer = Farmer('Олег', my_garden)

while True:
    farmer.care(5)
    sleep(2)




