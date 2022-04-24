goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}


store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

endings = {
    1: 'а',
    2: 'и',
    3: ''
}


for naming in goods.keys():
    q_summ = []
    p_summ = []

    for x in range(len(store[goods[naming]])):
        q_summ.append(store[goods[naming]][x]['quantity'])
        p_summ.append(store[goods[naming]][x]['price'] * store[goods[naming]][x]['quantity'])

    q_summ = sum(q_summ)
    p_summ = sum(p_summ)

    if q_summ % 10 == 1:                                                                 # динамические окончания
        end = endings[1]
    elif 5 > q_summ % 10:
        end = endings[2]
    else:
        end = endings[3]

    if p_summ > 9999:                                                                    # разнос тысячных
        print(f'{naming} — {q_summ} штук{end}, стоимость ', end='')
        print(f'{p_summ:,} рублей'.replace(",", " "))
    else:
        print(f'{naming} — {q_summ} штук{end}, стоимость {p_summ} рублей')
