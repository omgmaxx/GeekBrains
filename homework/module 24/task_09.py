class Cell:
    states = {'-': "пустая", 'x': "Крестик", 'o': "Нолик"}

    def __init__(self, index, state='-'):
        self.pos = index
        self.state = state


class Board:

    def __init__(self):
        self.cells = [[Cell([x, y]) for x in range(3)] for y in range(3)]

    def show_board(self):
        for row in game1.cells:
            for col in row:
                print(col.state, end='')
            print()

    # def check_states(self):
    #     # for x in range(3):
    #     #     if self.cells[x * 3].state == self.cells[x * 3 + 1].state == self.cells[x * 3 + 2].state or \
    #     #             self.cells[x].state == self.cells[x + 3].state == self.cells[x + 6].state or \
    #     #             self.cells[0].state == self.cells[4].state == self.cells[8].state or \
    #     #             self.cells[2].state == self.cells[4].state == self.cells[6].state:
    #     for x in range(3):
    #         all(self.cells[x][0].state) == 'x'
    #
    #             print('Игра окончена!')


class Player:
    sides = ['x', 'o']
    cntr = [0]

    def __init__(self, name, game):
        self.name = name
        self.side = self.sides[self.cntr[0]]
        self.cntr[0] += 1
        self.game = game

    def info(self):
        print(self.name, self.side)

    def take(self, pos):
        self.game.cells[int(pos[1]) - 1][int(pos[0]) - 1].state = self.side



game1 = Board()
game1.show_board()

player_1 = Player('Вася', game1)
player_2 = Player('Лёша', game1)
player_1.info()
player_2.info()

while True:
    player_1.take(input('Ходит первый игрок: ').split(maxsplit=1))
    game1.show_board()
    player_2.take(input('Ходит второй игрок: ').split(maxsplit=1))
    game1.show_board()

