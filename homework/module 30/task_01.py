from typing import List
from functools import reduce

if __name__ == '__main__':
    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

    floats_new = list(map(lambda num: round(num ** 3, 3), floats))
    names_new = list(filter(lambda name: len(name) >= 5, names))
    numbers_new = reduce(lambda a, b: a * b, numbers)

    print(floats_new)
    print(names_new)
    print(numbers_new)