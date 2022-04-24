def fibbo(target, num=1, last_num=0):
    if target == 0:
        return last_num
    target -= 1
    new_num = num + last_num
    return fibbo(target, new_num, num)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(fibbo(num_pos))
