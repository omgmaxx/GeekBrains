from collections import deque, Counter


if __name__ == '__main__':
    # без лямбды
    # def can_be_poly(word):
    #     """Функция, проверяющая, можно ли сделать из строки палиндром"""
    #     if len(word) <= 1:
    #         return True
    #     word = deque(word)
    #     if word.popleft() == word.pop():
    #         res = can_be_poly(word)
    #         return res
    #     else:
    #         return False

    # из решения
    def can_be_poly(word):
        """Функция, проверяющая, можно ли сделать из строки палиндром"""
        return len(list(filter(lambda x: x % 2, Counter(word).values()))) <= 1


    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
