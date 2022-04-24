given_range = int(input('Введите максимальное число: '))
print()
variants = set(range(1, given_range + 1))

while True:
    if len(variants) == 1:
        print("Игра окончена! Загаданное число:", ' '.join([str(n) for n in variants]))
        break
    elif len(variants) < 1:
        print("Игра окончена! Кто-то мухлюет.")
        break

    ask = input('Нужное число есть среди вот этих чисел: ')

    if ask == "Помогите!":
        print('Артём мог загадать следующие числа:', ' '.join([str(n) for n in variants]))
        break

    else:
        ask = set(map(int, ask.split()))
        answer = input('Ответ Артёма: ')

        if answer == "Да":
            variants &= ask
        elif answer == "Нет":
            variants -= ask
        else:
            print("Ответ неясен")
    print()
