sticks = int(input('Количество палок: '))
throws = int(input('Количество бросков: '))
output = ['I']*sticks

for i in range(throws):
    print(f'Бросок {i + 1}. ', end='')
    left_i = int(input('Сбиты палки с номера ')) - 1
    right_i = int(input('по номер ')) - 1

    if 0 <= left_i <= right_i < sticks:
        output = [('.' if left_i <= x <= right_i else output[x])
                  for x in range(sticks)]
    else:
        print('Ошибка ввода.')

text = ""     #list => str
for symb in output:
    text += symb

print('\nРезультат: ', text)