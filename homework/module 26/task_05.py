import os
from _collections_abc import Iterable


def py_files_lines(given_dir: str) -> Iterable[str]:
    """
    Генератор, подсчитывающий количество строк

    в файлах с расширением .py в данной папке

    :param given_dir: путь до папки
    :return: итерация с количеством строк в каждом файле и суммарное
    :rtype: Iterable[str]

    """
    comment_area = False
    sum_count = 0
    for file in os.listdir(given_dir):
        line_count = 0
        if file[-3:] == '.py':
            with open(file, 'r', encoding='utf-8') as pyfile:
                for line in pyfile:
                    if '"""' in line and 'if' not in line:
                        if not comment_area:
                            comment_area = True
                        else:
                            comment_area = False
                            continue
                    if line != '\n' and line[0] != '#' and not comment_area:
                        line_count += 1
        sum_count += line_count
        yield f'{file}: {line_count} строк'
    yield f'Суммарно {sum_count} строк'


directory = os.path.abspath('.')
files = py_files_lines(directory)
for x in files:
    print(x)
