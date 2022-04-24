def slicer(group, num):
    return group[group.index(num):group.index(num, 2)+1]


print(
    slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2)
)
