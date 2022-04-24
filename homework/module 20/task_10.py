list1 = 'abcd'
list2 = (10, 20, 30, 40)

length = max(len(list1), len(list2))
result = ((list1[x], list2[x]) for x in range(length))


print('Пример:'
      '\nСтрока:', list1,
      '\nКортеж чисел:', list2)

print('\n\nРезультат:')
print(result)
for x in result:
    print(x)
