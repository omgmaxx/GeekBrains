main_list = [1, 5, 3]
first_list = [1, 5, 1, 5]
second_list = [1, 3, 1, 5, 3, 3]

main_list.extend(first_list)
num_fives = main_list.count(5)

for _ in range(num_fives):
    main_list.remove(5)

main_list.extend(second_list)
num_threes = main_list.count(3)

print('Кол-во цифр 5 при первом объединении: ', num_fives)
print('Кол-во цифр 3 при первом объединении: ', num_threes)
print('Итоговый список: ', main_list)
