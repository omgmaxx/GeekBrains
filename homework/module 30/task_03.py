if __name__ == '__main__':
    primes_1 = list(filter(lambda num: all(num % divider != 0 for divider in range(2, num)), list(range(1, 1001))))

    primes_2 = [x for x in range(1, 1001)
                if all(x % y != 0 for y in range(2, x))]

    primes_3 = []
    for x in range(1, 1001):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            primes_3.append(x)

    print(primes_1)
    print(primes_2)
    print(primes_3)
