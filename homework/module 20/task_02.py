def is_prime(prime_list):
    answer = []
    for list_i, list_value in enumerate(prime_list):
        if list_i >= 2:
            for i in range(2, list_i // 2 + 1):
                if list_i % i == 0:
                    break
            else:
                answer.append(list_value)
    return answer


print(
    is_prime([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
)

print(
    is_prime('О Дивный Новый мир!')
)
