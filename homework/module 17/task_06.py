import random


num_amt = int(input('Количество чисел в списке: '))

randomized_list = [random.randint(0, 2) for _ in range(num_amt)]
num_list = [x for x in randomized_list if x != 0]

print('Список до сжатия:', randomized_list)
print('Список после сжатия:', num_list)