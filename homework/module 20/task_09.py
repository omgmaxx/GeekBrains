game_results = {
    1: ['Name', 0],
    2: ['Name', 0],
    3: ['Name', 0]
}

game_amt = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
for i in range(game_amt):
    score, name = input(f'{i + 1}-я запись: ').split()
    score = int(score)

    for res_i, res_stat in game_results.items():                                   # Проверка на имя + счёт
        if name == res_stat[0] and score > res_stat[1]:
            game_results[res_i] = [name, score]
            break

    else:
        for res_i, res_stat in game_results.items():                               # Последовательная проверка на счёт
            if score > res_stat[1]:

                for res2_i, res2_stat in game_results.items():                     # Перестановка сдвинутого
                    if res_stat[1] > res2_stat[1]:
                        game_results[res2_i] = [res_stat[0], res_stat[1]]
                        break

                game_results[res_i] = [name, score]
                break


print('\n\nИтоги соревнований:')
for key in game_results:
    print(f'{key}-е место. {game_results[key][0]} ({game_results[key][1]})')
