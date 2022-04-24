violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

number_dict = {
    1:'первой',
    2:'второй',
    3:'третьей',
    4:'четвёртой',
    5:'пятой',
    6:'шестой',
    7:'седьмой',
    8:'восьмой',
    9:'девятой'
}

time = 0
picked = []
amount = int(input('Сколько песен выбрать? '))


for index in range(amount):
    song = input(f'Название {number_dict[index+1]} песни: ')

    while song in picked:
        song = input(f'Песня уже в списке, повторите название {number_dict[index + 1]} песни: ')

    else:
        while song not in violator_songs:
            song = input(f'Такой песни нету, повторите название {number_dict[index+1]} песни: ')

        else:
            time += violator_songs.get(song)
            picked.append(song)


print(f'\nОбщее время звучания песен: {str(round(time, 2))}')
