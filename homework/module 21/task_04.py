site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_key(site_dict, key, limit):
    if limit == 0:
        return None
    if key in site_dict:
        return site_dict[key]
    limit -= 1
    for sub_dict in site_dict.values():
        if isinstance(sub_dict, dict):
            result = search_key(sub_dict, key, limit)
            if result:
                break
    else:
        result = None
    return result


search_for = input('Введите искомый ключ: ')
check = input('Хотите ввести максимальную глубину? Y/N: ')
if check.lower() == 'y':
    search_in = int(input('Введите максимальную глубину: '))
else:
    search_in = 100

value = search_key(site, search_for, search_in)

print('Значение ключа:', value)