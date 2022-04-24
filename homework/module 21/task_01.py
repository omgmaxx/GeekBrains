def adding(target):
    if 0 == target:
        return
    target -= 1
    adding(target)
    print(target + 1)
    return target


adding(10)
