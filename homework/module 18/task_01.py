text = str(input('Доступное меню: '))
text = text.split(';')
result = ', '.join(text)

print('\nНа данный момент в меню есть:', result)
