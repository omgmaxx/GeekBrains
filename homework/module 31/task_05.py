import itertools


if __name__ == '__main__':
    for res in itertools.permutations(range(10), 4):
        print(res)
