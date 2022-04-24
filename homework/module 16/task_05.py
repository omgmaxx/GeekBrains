violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
playlist = []
playtime = 0

amount = int(input('Сколько песен выбрать? '))

for i in range(amount):
    song = str(input(f'Название {i + 1}-й песни: '))
    for i in violator_songs:
        if song == i[0]:
            index = i.index(song)
            playlist.append(i[0])
            playtime += i[1]

print('\nОбщее время звучания песен: ', round(playtime, 2))



