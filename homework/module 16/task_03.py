shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500],['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

while True:
    x = str(input('Название детали: '))
    count = 0
    price = 0

    for list in shop:
        if list[0] == x:
            count += 1
            price += list[1]

    if count > 0:
        print('Кол-во деталей —', count)
        print('Общая стоимость —', price, end='\n\n')
    else:
        print('Таких деталей нет\n')
