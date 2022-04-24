import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


def calculations(source, destination):
    open(destination, 'w').close()                                             # Очистка результатов
    fun_numb = 0
    line_numb = 0

    with open(source, 'r') as file:
        for line in file:
            line_numb += 1
            try:
                nums_list = line.split()
                fun_numb = 1
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                fun_numb = 2
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)
                with open(destination, 'a') as file_2:
                    my_list = sorted([res1, res2, number])
                    file_2.write(' '.join((str(my_list), '\n')))
            except ZeroDivisionError:
                print(f'Деление на ноль в {line_numb} ряду чисел, {fun_numb}-й функции!')
            except ValueError:
                print(f'Неверные вводные данные в {line_numb} ряду чисел!')


source_file = 'coordinates.txt'
target_file = 'result.txt'
calculations(source_file, target_file)
