nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

list1 = [nice_list[x // 9][(x % 9) // 3][x % 3]
         for x in range(18)]

print('Ответ:', list1)


