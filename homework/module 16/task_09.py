friends = int(input('Кол-во друзей: '))
oblig_amt = int(input('Долговых расписок: '))
data = [0] * friends           #создание ячеек


for i in range(oblig_amt):
    print(f'\n{i+1}-я расписка: ')
    target = int(input('Кому: ')) - 1
    sender = int(input('От кого: ')) - 1

    if friends > target >= 0 and friends > sender >= 0:        #проверка, в интервале ли участники
        money = int(input('Сколько: '))
        data[target] -= money
        data[sender] += money
    else:
        print('Участники расписки указаны неверно, расписка недействительна')


print('\nБаланс друзей: ')
for money_out in range(friends):
    print(f'{money_out + 1}: {data[money_out]}')
