from random import randint


class Human:

    def __init__(self, name, home):
        self.home = home
        self.name = name
        self.satiation = 50
        self.alive = True

    def eat(self):
        if self.home.food >= 10:
            self.satiation += 30
            self.home.food -= 10
            print('Вы поели\n+30 сытости -10 еды.')
        else:
            print('Вам нечего есть!')
        self.stats()

    def work(self):
        self.satiation -= 15
        self.home.money += 15
        if self.satiation > 0:
            print('Вы отработали смену\n+15 денег -15 сытости.')
        else:
            self.alive = False
            print('Вы умерли от голода!')
        self.stats()

    def play(self):
        self.satiation -=10
        print('Вы играли несколько часов\n-10 сытости.')
        self.stats()

    def shop(self):
        if self.home.money >= 15:
            self.home.food += 20
            self.home.money -= 15
            print('Вы отправились в магазин за едой\n+20 еды -15 денег.')
        else:
            print('Вам не на что покупать еду!')
        self.stats()

    def stats(self):
        print('[{: ^7}][{: <2} еды][{: <2} сытости][{: <2} денег]\n\n'.format(
            self.name, self.home.food, self.satiation, self.home.money
        ))


class Home:

    def __init__(self, street):
        self.address = street
        self.food = 50
        self.money = 0


house = Home('Кировский пр. 25')
human_1 = Human('Гриша', house)
human_2 = Human('Юля', house)
family = [human_1, human_2]

for day in range(365):
    if not human_1.alive or not human_2.alive:
        break
    print(f'День {day + 1}-й\n==========')

    for human in family:
        dice = randint(1,6)
        if human.satiation < 20:
            human.eat()
        elif house.food < 10:
            human.shop()
        elif house.money < 50:
            human.work()
        elif dice == 1:
            human.work()
        elif dice == 2:
            human.eat()
        else:
            human.play()
