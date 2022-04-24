text = str(input('Введите текст: '))
vowels = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
vowel_List = []

for y in list(text):
    vowel_List.extend([x for x in vowels if x == y])

print('\nСписок гласных букв:', vowel_List)
print('Длина списка:', len(vowel_List))