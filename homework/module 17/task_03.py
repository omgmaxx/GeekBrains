import random

def rndm_list():
    return [round(random.uniform(5, 10), 2) for _ in range(20)]

def cmprsn(x, y):
    return [team1[x] if team1[x] > team2[x] else team2[x] for x in range(20)]

team1 = rndm_list()
team2 = rndm_list()

print('Первая команда:', team1)
print('\nВторая команда:', team2)
print('\nПобедители тура:', cmprsn(team1, team2))

