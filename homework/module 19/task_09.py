number_dict = {
    1:'первая',
    2:'вторая',
    3:'третья',
    4:'четвёртая',
    5:'пятая',
    6:'шестая',
    7:'седьмая',
    8:'восьмая',
    9:'девятая',
}

family_dict = dict()
amount = int(input('Введите количество человек: ')) - 1
while amount > 10:
    amount = int(input('Введите количество человек меньше 11: '))


for n in range(amount):
    name1, name2 = input(f'{number_dict[n+1].capitalize()} пара: ').split()
    if n == 0:                                                                       # выбор нулевого предка
        family_dict[0] = [name2]
        family_dict[1] = [name1]
    else:
        for pos in family_dict:
            if name2 in family_dict[pos] :
                if pos + 1 not in family_dict:                                       # добавление "уровня"
                    family_dict[pos + 1] = [name1]
                    break
                else:
                    family_dict[pos + 1].append(name1)
                    break

print('\n«Высота» каждого члена семьи:')
value_names = [name for group in family_dict.values() for name in group]            # упорядочивание имён
for member in sorted(value_names):                                                  # вывод "древа"
    for x in family_dict:
        if member in family_dict[x]:
            print(member, x)

