def can_opener(array):
    result = []
    for argument in array:
        if isinstance(argument, list):
            result += can_opener(argument)
        else:
            result.append(argument)
    return result


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(can_opener(nice_list))