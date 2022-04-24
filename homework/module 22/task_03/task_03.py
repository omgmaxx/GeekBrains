def max_letter(text):
    dct = {}
    for letter in text:
        if letter.isalpha():
            if letter not in dct:
                dct[letter] = 1
            else:
                dct[letter] += 1
    max_l = max(dct, key=dct.get)
    return max_l, dct[max_l]


def line_cnt(text):
    lines = 0
    for _ in text.split("\n"):
        lines += 1
    return lines


def word_cnt(text):
    words = 0
    for line in text.split():
        for _ in line.split():
            words += 1
    return words


def letter_cnt(text):
    letters = 0
    for letter in text:
        if letter.isalpha():
            letters += 1
    return letters


def stats_txt(txt_input):
    text_file = open(txt_input, 'r')
    imported_text = text_file.read()
    text_file.close()

    max_i, max_v = max_letter(imported_text)

    print('Количество букв в файле: {0}\n'
          'Количество слов в файле: {1}\n'
          'Количество строк в файле: {2}\n'
          'Наиболее редкая буква: "{3}" ({4})'
          .format(line_cnt(imported_text),
                  word_cnt(imported_text),
                  letter_cnt(imported_text),
                  max_i, max_v))


source = "zen.txt"
stats_txt(source)
