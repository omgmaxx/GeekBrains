def super_summ(*args):
    result = 0
    for argument in args:
        if isinstance(argument, list):
            for element in argument:
                result += super_summ(element)
        else:
            result += argument
    return result


print(super_summ([[1, 2, [3]], [1], 3]))

print(super_summ(1, 2, 3, 4, 5))