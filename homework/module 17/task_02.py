list_length = list(range(int(input('Введите длину списка: '))))

result_list = [(1 if x % 2 == 0 else x % 5) for x in list_length]

print('Результат:', result_list)
