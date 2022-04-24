excludes = tuple(list('@№$%^&*()'))
formats = tuple(['.txt', '.docx'])

text = str(input('Название файла: '))
print()

if text.endswith(formats):
    if not text.startswith(excludes):
        print('Файл назван верно.')
    else:
        print('Ошибка: название начинается на один из специальных символов.')
else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
