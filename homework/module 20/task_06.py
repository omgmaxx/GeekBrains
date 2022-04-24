import random
random_list = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список:', random_list)                                        # составление случайного списка


fst_list = []                                                                                         # способ №1
sec_list = []
for index, value in enumerate(random_list):
    if index % 2 == 0:
        fst_list.append(value)
    else:
        sec_list.append(value)
grouped_list = zip(fst_list, sec_list)
print('Новый список (Способ №1):', list(grouped_list))


grouped_list2 = [(random_list[x], random_list[x + 1]) for x in range(0, len(random_list), 2)]       # способ №2
print('Новый список (Способ №2):', grouped_list2)


grouped_list3 = []                                                                                  # способ №3
temp_list = -1
for num in random_list:
    if temp_list >= 0:
        grouped_list3.append(tuple([temp_list, num]))
        temp_list = -1
    else:
        temp_list = num
print('Новый список (Способ №3):', grouped_list3)
