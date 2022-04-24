alphebet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = str(input('Введите сообщение: '))
index = int(input('Введите сдвиг: '))
decode = []
output = ""

for symb in message:
    if symb == ' ':
        decode.append([' '])
    else:
        decode.append(
            [alphebet[(ref + index) % len(alphebet)]
             for ref in range(len(alphebet))
             if symb == alphebet[ref]]
        )

for letter in decode:
    output += letter[0]

print(f'Зашифрованное сообщение: {output}.')
