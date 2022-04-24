import os


def get_stat(data):
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    stat = {}
    for line in data:
        for letter in line:
            if letter.lower() in alphabet:
                if letter in stat:
                    stat[letter.lower()] += 1
                else:
                    stat[letter.lower()] = 1
    return stat


def convert_stat(data):
    sorted_data = {}
    total_symbols = sum(data.values())
    for key, val in data.items():
        data[key] = round(val / total_symbols, 3)
    sorted_keys = sorted(data, key=data.get, reverse=True)
    for symbol in sorted_keys:
        sorted_data[symbol] = data[symbol]
    return sorted_data


def write_file(file, data):
    file_path = os.path.abspath(file)
    file_data = open(file_path, 'w')
    for key, val in data.items():
        file_data.write(f'{key} {val}\n')
    file_data.close()


def read_file(file):
    file_path = os.path.abspath(file)
    file_data = open(file_path, 'r')
    stat = get_stat(file_data)
    file_data.close()
    stat = convert_stat(stat)
    return stat


text_input = 'text.txt'
analysis_output = 'analysis.txt'

statistics = read_file(text_input)
write_file(analysis_output, statistics)
