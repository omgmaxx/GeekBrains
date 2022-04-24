def sort(list):
    for i in range(len(list) - 1):
        min = list[i]
        count_index = i
        for j in range(i + 1, len(list)):
            if min > list[j]:
                min = list[j]
                count_index = j
        list[i], list[count_index] = list[count_index], list[i]
    return list


first_line = list(range(160, 177, 2))
second_line = list(range(162, 181, 3))

first_line.extend(second_line)

sort(first_line)

print('Отсортированный список учеников: ', first_line)
