site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def site_view(site_dict, phone, level=0):
    if level == 0:
        print('site = {')
    level += 1
    for x, y in site_dict.items():
        print(level * 4 * ' ', end='')
        if isinstance(y, dict):
            print(f"{x}: "+'{')
            site_view(y, phone, level)
        else:
            print(f"{x}: '{y}'".replace('iPhone', phone).replace('телефон', phone))
    print((level-1)*3*' ', '}')
    return


phone_names = []
amt = int(input('Сколько сайтов: '))
for _ in range(amt):
    phone_names.append(str(input('Введите название продукта для нового сайта: ')))
    for name in phone_names:
        print('Сайт для {}: '.format(name))
        site_view(site, name)
        print()
