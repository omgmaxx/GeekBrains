def main(file):
    meta_result = 0
    with open(file, 'r') as calc_text:
        for line in calc_text:
            try:
                line = line.replace('\n', '').split()
                meta_result += in_line(line)

            except (SyntaxError, ZeroDivisionError, IndexError, ValueError):
                error(line)

    print('\nСумма результатов: ', meta_result)


def in_line(line):
    if len(line) != 3:
        raise IndexError('Не три операнда')
    line[0] = int(line[0])
    line[2] = int(line[2])
    if line[1] not in '+ / * ^ - ** // %'.split():
        raise SyntaxError('Неверный знак')
    result = calculation(line)
    print('{} = {}'.format(
        ' '.join(str(x) for x in line),
        result))
    return result


def error(line):
    print('Обнаружена ошибка в строке: {}  '.format(
        ' '.join(str(x) for x in line)),
        end='')
    check = input('Хотите исправить? ')
    if check.lower() == 'да':
        line = input('Введите исправленную строку: ').split()
        in_line(line)


def calculation(line):
    if line[1] == '+':
        result = line[0] + line[2]
    elif line[1] == '/':
        result = line[0] / line[2]
    elif line[1] == '*':
        result = line[0] * line[2]
    elif line[1] == '^' or line[1] == '**':
        result = line[0] ** line[2]
    elif line[1] == '-':
        result = line[0] - line[2]
    elif line[1] == '//':
        result = line[0] // line[2]
    elif line[1] == '%':
        result = line[0] % line[2]
    else:
        raise SyntaxError
    return result


output_file = 'calc.txt'
main(output_file)
