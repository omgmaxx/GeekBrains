def zipping(list1, list2, zipped):
    if not len(list1) or not len(list2):
        return
    list1 = list(list1)
    list2 = list(list2)
    zipped.append((list1.pop(0), list2.pop(0)))
    zipping(list1, list2, zipped)
    return zipped


zip_list = []
num_list = [10, 20, 30, 40, 55]
str_list = 'abcdeadsda'

zip_list = zipping(str_list, num_list, zip_list)
print(zip_list)
