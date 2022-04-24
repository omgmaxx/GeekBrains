text = str(input('Первая строка: '))
text2 = str(input('Вторая строка: '))

text = list(text)
counter = 0

for _ in range(len(text)-1):

    if text == list(text2):
        print(f'\nПервая строка получается из второй со сдвигом {counter}.')
        break

    text.insert(len(text), text[0])
    text.pop(0)
    counter += 1

else:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
