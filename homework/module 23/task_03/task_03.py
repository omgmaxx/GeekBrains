import random


def random_check():
    r_except = [ValueError, TypeError, IndexError]
    if random.randint(1, 13) == 13:
        raise r_except[random.randint(0, 3)]


def add_to_total(total, destination):
    addition = int(input('Введите число: '))
    total += addition
    random_check()
    destination.write(str(addition)+'\n')
    return total


def lucky_num(file):
    total_number = 0

    try:
        with open(file, 'w') as out_file:
            while total_number < 777:
                total_number = add_to_total(total_number, out_file)

    except ValueError:
        print('Вас постигла неудача! (ValueError)')
    except TypeError:
        print('Вас постигла неудача! (TypeError)')
    except IndexError:
        print('Вас постигла неудача! (IndexError)')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')


output = 'out_file.txt'
lucky_num(output)
