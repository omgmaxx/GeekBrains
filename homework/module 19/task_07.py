number_dict = {
    1:'первый',
    2:'второй',
    3:'третий',
    4:'четвёртый',
    5:'пятый',
    6:'шестой',
    7:'седьмой',
    8:'восьмой',
    9:'девятый',
}


orders = int(input('Введите количество заказов: '))
while orders > 9:
    orders = int(input('Введите количество меньше 10 заказов: '))

data = dict()
for x in range(orders):
    name, pizza, amount = input(f'{number_dict[x+1].capitalize()} заказ: ').lower().split(maxsplit=2)
    amount = int(amount)
    if name in data:
        if pizza in data[name]:
            data[name][pizza] += amount
        else:
            data[name].update({pizza: amount})
    else:
        data[name] = {pizza: amount}

print()
for name in sorted(data):
    print(f'{name.capitalize()}:')
    for pizza in sorted(data[name]):
        print(f'        {pizza.capitalize()}: {data[name][pizza]}')