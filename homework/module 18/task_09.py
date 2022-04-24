text = str(input('Сообщение: '))

word = []
result = ''
for symb in text:
    if symb.isalpha():
        word.insert(0, symb)
    else:
        result += ''.join(word) + symb
        word = []

print('\nНовое сообщение: ', result)
