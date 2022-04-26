import random


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.value = 0

    def take(self, deck):
        if deck.cards[0].rank == 'jack' or deck.cards[0].rank == 'queen' or deck.cards[0].rank == 'king':
            self.value += 10
        elif deck.cards[0].rank == 'ace':
            if self.value < 21:
                self.value += 11
            else:
                self.value += 1
        else:
            self.value += int(deck.cards[0].rank)
        self.cards.append(deck.cards.pop(0))

    def hand(self):
        print(f'Игрок - {self.name}')
        for card in self.cards:
            print(card.suit, card.rank)
        print('Суммарно {} очков\n'.format(self.value))


class Deck:
    suits = ['hearts', 'spade', 'diamond', 'club']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


def final_score(player_1, player_2):
    print('Ваши {} против {} дилера. '.format(player_1.value, player_2.value), end='')


def game(player_1, player_2):
    deck = Deck()
    deck.shuffle()
    starting_hand(player_1, deck)
    starting_hand(player_2, deck)

    while True:
        if player_1.value == 21:
            print('Ровно 21 очко! Вы выиграли!')
            break
        action = input('1. Взять карту\n2. Остановиться. ')
        print()
        if action == '1':
            player_1.take(deck)
            player_1.hand()
            if player_1.value > 21:
                print('Более 21 очка! Вы проиграли!')
                break

        else:
            if player_1.value > player_2.value:
                final_score(player_1, player_2)
                print('Вы выиграли!')
            elif player_1.value == player_2.value:
                final_score(player_1, player_2)
                print('Ничья!')
            else:
                final_score(player_1, player_2)
                print('Вы проиграли!')
            break


def starting_hand(player, deck):
    for _ in range(2):
        player.take(deck)
    player.hand()


player_user = Player('Даня')
dealer = Player('Дилер')


game(player_user, dealer)

