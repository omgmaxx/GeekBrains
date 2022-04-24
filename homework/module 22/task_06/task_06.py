import os


def encrypt(i_file, o_file):
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    shift = 0
    for line in in_file:
        result = ''
        shift += 1
        line = line.replace('\n', '')
        for letter in line:
            if letter.isupper():  # Проверка на регистр
                result += ''.join(alphabet[alphabet.index(letter.lower()) - abs(26 - shift)]).upper()
            else:
                result += ''.join(alphabet[alphabet.index(letter.lower()) - abs(26 - shift)])
        line = result
        out_file.write(line + '\n')


in_file = open(os.path.abspath('text.txt'), 'r')
out_file = open(os.path.abspath('cipher_text.txt'), 'w')
encrypt(in_file, out_file)
