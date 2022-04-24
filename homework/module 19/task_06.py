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


pairs = int(input('Введите количество пар слов: '))
while pairs > 9:
    pairs = int(input('Введите количество меньше 10 пар слов: '))

pairs_dict = dict(str(input(f'{number_dict[x+1].capitalize()} пара: ')).lower().split(' — ', maxsplit=1) for x in range(pairs))
print()


while True:
    check = input('Введите слово: ').lower()

    if check in pairs_dict.keys():
        print('Синоним:', pairs_dict.get(check).capitalize())

    else:
        for index in pairs_dict.keys():
            if check == pairs_dict[index]:
                print('Синоним:', index.capitalize())
                break

        else:
            print('Такого слова в словаре нет.')

