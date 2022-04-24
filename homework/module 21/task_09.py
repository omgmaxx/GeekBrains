def move_report(disk, source, target):
    print(f'Переложить диск {disk[0]} со стержня номер {source} на стержень номер {target}')


def move_1(tower):
    if not tower[1] or tower[2] and tower[1][-1] > tower[2][-1]:
        move_report(tower[2][-1:], 2, 1)
        tower[1].append(tower[2].pop(-1))
    else:
        move_report(tower[1][-1:], 1, 2)
        tower[2].append(tower[1].pop(-1))


def move_2(tower):
    if tower[3] and tower[1][-1] > tower[3][-1]:
        move_report(tower[3][-1:], 3, 1)
        tower[1].append(tower[3].pop(-1))
    else:
        move_report(tower[1][-1:], 1, 3)
        tower[3].append(tower[1].pop(-1))


def move_3(tower):
    if tower[3] and tower[2][-1] > tower[3][-1]:
        move_report(tower[3][-1:], 3, 2)
        tower[2].append(tower[3].pop(-1))
    else:
        move_report(tower[2][-1:], 2, 3)
        tower[3].append(tower[2].pop(-1))


def odd_move(tower):
    print('======')
    move_2(tower)
    if not tower[1] and not tower[2]:
        return
    move_1(tower)
    move_3(tower)
    odd_move(tower)
    return


def even_move(tower):
    print('======')
    move_1(tower)
    move_2(tower)
    move_3(tower)
    if not tower[1] and not tower[2]:
        return
    even_move(tower)


def move_hanoi(tow_len, even=True):
    hanoi = {1: list(range(tow_len, 0, -1)), 2: [], 3: []}

    if len(hanoi[1]) % 2 == 1:
        even = False

    if even:
        even_move(hanoi)
    else:
        odd_move(hanoi)

    return


tower_length = int(input('Введите количество дисков: '))
move_hanoi(tower_length)


