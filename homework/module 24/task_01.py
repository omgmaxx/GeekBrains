from random import randint


class Warrior:

    def __init__(self, name):
        self.health = 100
        self.damage = 20
        self.name = str(name)

    def hit(self, target):
        target.health -= self.damage
        print('Воин {0} нанёс воину {1} {2} урона.\nУ воина {1} осталось {3} здоровья.\n'.format(
            self.name,
            target.name,
            self.damage,
            target.health
        ))

    def hp(self):
        print('У воина {} осталось {} здоровья'.format(
            self.name,
            self.health
        ))


warrior1 = Warrior('Джордж')
warrior2 = Warrior('Кремень')

while True:                                             # битва
    x = randint(1, 2)

    if x == 1:
        warrior2.hit(warrior1)
    else:
        warrior1.hit(warrior2)

    if warrior1.health <= 0:                            # финал
        print(f'{warrior2.name} победил!')
        break
    elif warrior2.health <= 0:
        print(f'{warrior1.name} победил!')
        break
