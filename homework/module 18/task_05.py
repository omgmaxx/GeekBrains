while True:
    upper_counter = 0
    num_counter = 0

    password = str(input('Придумайте пароль: '))

    if len(password) >= 8:
        for letter in password:
            if letter in str(list(range(10))):          # проверка на цифры
                num_counter += 1
            elif letter == letter.upper():              # проверка на заглавные
                upper_counter += 1
        if upper_counter >= 1 and num_counter >= 3:
            print('Это надёжный пароль!')
            break

    print('Пароль ненадёжный. Попробуйте ещё раз.')
