def init():
    chat_data = 'chat_data.txt'
    main(login(), chat_data)


def login():
    nickname = input('Введите имя пользователя: ')
    print('X', '-'*88, 'X')
    print('|{: ^90}|'.format('Добрый день,'))
    print('|{: ^90}|'.format(nickname))
    print('X', '-' * 88, 'X')
    return nickname


def main(nickname, chat_data):
    while True:
        print('1) Посмотреть текущий текст чата.\n'
              '2) Отправить сообщение.')
        ask = int(input())
        if ask == 1:
            read_chat(chat_data)
        elif ask == 2:
            write_chat(nickname, chat_data)


def read_chat(chat_data):
    print('X {:-^88} X'.format(' chat v.1.0 '))
    with open(chat_data, 'r', encoding='utf-8') as chat:
        for line in chat:
            print(line, end='')

    print('X', '-' * 88, 'X')
    print()


def write_chat(name, chat_data):
    with open(chat_data, 'a', encoding='utf-8') as chat:
        chat.write('[{}]: {}\n'.format(name, input('>')))


init()
