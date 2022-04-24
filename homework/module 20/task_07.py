def list_sort(orig_list):
    new_list = [num for num in range(min(orig_list), max(orig_list) + 1) if num in orig_list]
    return new_list


print(
    list_sort((6, 3, -1, 8, 4, 10, -5))
)
