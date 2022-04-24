def calculating_math_func(num, data={}):
    result = 1
    if not data.get(num):
        data[num] = num
        for index in range(1, data[num] + 1):
            result *= index
        data[num] = result
    result = data[num] / num ** 3
    result = result ** 10
    return result


print(calculating_math_func(5))
print(calculating_math_func(5))
