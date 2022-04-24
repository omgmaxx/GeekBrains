list_one = []
list_two = []


for x in range(3):
    num_one = int(input(f'Введите {x + 1}-е число для первого списка: '))
    list_one.append(num_one)

for y in range(7):
    num_two = int(input(f'Введите {y + 1}-е число для второго списка: '))
    list_two.append(num_two)

list_one.extend(list_two)

for num in list(list_one):
    while list_one.count(num) > 1:
        list_one.remove(num)

print(list_one)