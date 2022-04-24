import os


def writing(path, text):
    new_file = open(path, 'w', encoding='utf-8')
    new_file.write(text)
    new_file.close()


def combining_path(u_path, f_path):
    for i in u_path:
        f_path = os.path.join(f_path, i)  # Соединяем путь
    return f_path


def writing_checks(path, text):
    if os.path.isdir(path):
        file_path = os.path.join(path, input('Введите имя файла: ') + '.txt')  # Создаём имя файла
        if os.path.isfile(file_path):
            check = input('Вы действительно хотите перезаписать файл? ').lower()
            if check == 'да':
                writing(file_path, text)
                print('Файл успешно перезаписан!')
            else:
                print('В перезаписи отказано.')
        else:
            writing(file_path, text)
            print('Файл успешно сохранён!')
    else:
        print('Такой папки не существует')


user_text = input('Введите строку: ')
disk = os.path.abspath('.')[:3]             # Получаем диск
print('Куда хотите сохранить документ? Введите последовательность папок (через пробел): \n' + disk, end='')
user_path = input().split()

full_path = combining_path(user_path, disk)
writing_checks(full_path, user_text)
