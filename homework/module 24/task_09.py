class Cell:
    states = {'-': "пустая", 'x': "Крестик", 'o': "Нолик"}

    def __init__(self, index, state='-'):
        self.pos = index
        self.state = state


class Board:

    def __init__(self):
        self.game_count = 0
        self.cells = []
        self.new_game()

    def new_game(self):
        self.game_count += 1
        print('\nНачинается игра №{}:'.format(self.game_count))
        self.cells = [[Cell([x, y]) for x in range(3)] for y in range(3)]

    def show_board(self):
        for row in self.cells:
            for col in row:
                print(col.state, end='')
            print()

    def check_states(self, name, side):
        for y in range(3):
            if all([self.cells[y][x].state == side for x in range(3)]):
                self.end_game(name, side)

        for x in range(3):
            if all([self.cells[y][x].state == side for y in range(3)]):
                self.end_game(name, side)

        if all([self.cells[x][x].state == side for x in range(3)]):
            self.end_game(name, side)

        if all([self.cells[x][2-x].state == side for x in range(3)]):
            self.end_game(name, side)

        if all([self.cells[y][x].state != '-' for x in range(3) for y in range(3)]):
            self.end_game(name, '-')

    def end_game(self, name, side):
        side_name = {'x': 'крестиках', 'o': 'ноликах'}
        if side != '-':
            print('Игрок {} на {} победил!'.format(name, side_name[side]))
        else:
            print('Ходы кончились - ничья!')

        self.new_game()


class Player:
    sides = ['x', 'o']
    cntr = [0]

    def __init__(self, name, game):
        self.name = name
        self.side = self.sides[self.cntr[0]]
        self.cntr[0] += 1
        self.game = game
        self.info()

    def info(self):
        print(self.name, self.side)

    def take(self):
        pos = input(f'Ходит {self.name}: ').split(maxsplit=1)
        try:
            if self.game.cells[int(pos[1]) - 1][int(pos[0]) - 1].state == '-':
                self.game.cells[int(pos[1]) - 1][int(pos[0]) - 1].state = self.side
            else:
                raise IndexError('Поле занято!')
        except IndexError:
            print('Нелигитимный ход, попробуйте ещё раз:')
            self.take()

    def turn(self):
        self.take()
        self.game.show_board()
        self.game.check_states(self.name, self.side)


game_one = Board()
player_one = Player('Вася', game_one)
player_two = Player('Лёша', game_one)

while True:
    player_one.turn()
    player_two.turn()
