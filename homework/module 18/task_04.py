text = str(input('Введите строку: '))
text = text.split()
text_formatted = ''.join([word[0].upper() + word[1:] + ' ' for word in text])

print(text_formatted)
