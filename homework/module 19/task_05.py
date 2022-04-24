text = input('Введите текст: ').capitalize()


freq = dict()        # Составление словаря
for letter in text:
    if not freq.get(letter):
        freq[letter] = 1
    else:
        freq[letter] += 1


freq2 = dict()        # Ревёрс
for pos1 in freq:

    if not freq2.get(freq[pos1]):
        freq2[freq[pos1]] = []
    freq2[freq[pos1]].append(pos1)


print('Оригинальный словарь частот:')          # Вывод
for pos in sorted(freq):
    print(f'{pos}: {freq[pos]}')

print('\nИнвертированный словарь частот:')
for line in sorted(freq2):
    print(f'{line}: {freq2[line]}')