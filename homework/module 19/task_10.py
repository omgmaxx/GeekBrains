def makeDictOf(fword):
    word_dict = dict()
    for letter in fword:
        if letter not in word_dict:
            word_dict[letter] = 1
        else:
            word_dict[letter] += 1
    return word_dict


def possiblePalindrom(word_dict):
    count = 0
    for value in word_dict.values():
        if value % 2 == 1:
            count += 1
    if count <= 1:
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')


word = input('Введите строку: ')

possiblePalindrom(makeDictOf(word))

