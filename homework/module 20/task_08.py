def adding():
    contact_name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    contact_number = input('Введите номер телефона: ')
    list_of_contacts[contact_name] = contact_number
    print('Текущий словарь контактов:', list_of_contacts)


def searching():
    search = input('Введите имя/фамилию для поиска: ')
    for name, num in list_of_contacts.items():
        if search.lower() in name[0][:len(search)].lower() \
                or search.lower() in name[1][:len(search)].lower():
            print(' '.join(name), num)


def init():
    print('\nВведите номер действия:\n'
          '1. Добавить контакт\n'
          '2. Найти человека ')
    task = input()

    if task == '1':
        adding()
    elif task == '2':
        searching()
    else:
        print('Ошибка ввода')


list_of_contacts = {}


while True:
    init()
