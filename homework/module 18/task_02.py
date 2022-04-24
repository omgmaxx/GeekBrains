text = str(input('Введите строку: '))
text = text.split()
longest = ''
for word in text:
    if len(word) > len(longest):
        longest = word

print('Самое длинное слово:', longest)
print('Длина этого слова:', len(longest))
