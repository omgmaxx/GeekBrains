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
    11:'первый',
    12:'второй',
    13:'третий'
}

countries = dict()
amount = int(input('Количество стран: '))


for x in range(amount):
    line = input(f'{number_dict[x+1].capitalize()} страна: ').split()
    countries[line[0]] = line[1:]

for index in range(3):
    pick = input(f'\n{number_dict[index+11].capitalize()} город: ')
    for country in countries:
        if pick in countries[country]:
            print(f'Город {pick} расположен в стране {country}.')
            break
    else:
        print(f'По городу {pick} данных нет.')
