guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
    ask = str(input('Гость пришёл или ушёл? '))

    if ask == 'пришёл' or ask == 'Пришёл':
        newcomer = str(input('Имя гостя: '))

        if len(guests) < 6:
            guests.append(newcomer)
        else:
            print(f'Прости, {newcomer}, но мест нет.')

    elif ask == 'ушёл' or ask == 'Ушёл':
        leaver = str(input('Имя гостя: '))

        if guests.count(leaver) > 0:
            guests.remove(leaver)
        else:
            print(f'Никого с именем {leaver} здесь нет')

    elif ask == 'Пора спать' or ask == 'пора спать':
        break

    else:
        print('Ошибка ввода')


print('\nВечеринка закончилась, все легли спать.')