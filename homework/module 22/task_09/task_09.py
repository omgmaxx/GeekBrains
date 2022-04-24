import os

import os
import zipfile


def get_stat(data):
    stat = {}
    for line in data:
        line = line.decode('utf-8')
        for letter in line:
            if str(letter).isalpha():
                if letter in stat:
                    stat[letter] += 1
                else:
                    stat[letter] = 1
    return stat


def convert_stat(data):
    sorted_data = {}
    total_symbols = sum(data.values())
    for key, val in data.items():
        data[key] = round(val / total_symbols, 8)
    sorted_keys = sorted(data, key=data.get, reverse=True)
    for symbol in sorted_keys:
        sorted_data[symbol] = data[symbol]
    return sorted_data


def write_file(file, data):
    file_path = os.path.abspath(file)
    file_data = open(file_path, 'w', encoding='utf-8')
    for key, val in data.items():
        file_data.write(f'{key} {val}\n')
    file_data.close()


def read_file(file):
    zipped = zipfile.ZipFile(os.path.abspath(file), 'r')
    text = zipped.open('voina-i-mir.txt', 'r')
    stat = get_stat(text)
    zipped.close()
    stat = convert_stat(stat)
    return stat


text_input = 'voina-i-mir.zip'
analysis_output = 'analysis.txt'

statistics = read_file(text_input)
write_file(analysis_output, statistics)
