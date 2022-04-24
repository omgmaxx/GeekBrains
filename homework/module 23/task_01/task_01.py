def symb_cnt_three_long_names(file_name):
    line_cnt = 0
    full_len = 0

    with open(file_name, 'r', encoding='utf-8') as text:

        for line in text:
            line_cnt += 1

            line = line.replace('\n', '')

            try:
                if len(line) < 3:
                    raise TypeError
                full_len += len(line)

            except TypeError:
                print(f'Ошибка: менее трёх символов в строке {line_cnt}.')

    return full_len


file = 'people.txt'
length = symb_cnt_three_long_names(file)
print('Общее количество символов: ', length)
