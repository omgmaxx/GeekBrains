text = str(input('Введите строку: '))
result = ''
counter = 0

for letter in range(len(text)):
    counter += 1
    if letter == len(text)-1:
        result += ''.join(text[letter] + str(counter))
    elif text[letter] != text[letter+1]:
        result += ''.join(text[letter] + str(counter))
        counter = 0


print('\nЗакодированная строка: ', result)
