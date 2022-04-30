import os
from _collections_abc import Iterable


def gen_files_path(target: str,
                   path=os.path.join('A:', os.path.sep)
                   ) -> Iterable[str]:
    """
    Генератор, ищущий целевой файл в указанной директории

    По умолчанию ищет в корневой папке диска

    :param target: целевой файл
    :param path: папка, в которой ведётся поиск
    :return: пути всех проверенных файлов
    :rtype: Iterable[str]

    """
    for root, dirs, files in os.walk(path):
        for name in files:
            yield os.path.join(root, name)
            if name == target:
                yield 'Файл найден'
                return
    else:
        print('Файл не найден')


file = 'task_01.py'
for x in gen_files_path(target=file):
    print(x)
