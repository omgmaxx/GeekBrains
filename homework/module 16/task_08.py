people_number = int(input('Кол-во человек: '))
people = list(range(1, people_number+1))
counter = int(input('Какое число в считалке? '))
next = 0
print()


while len(people) != 1:
    print(f'Текущий круг людей: {people}')
    print(f'Начало счёта с номера {people[next]}')
    print(f'Выбывает человек под номером {people[(counter % len(people) + next) % len(people) - 1]}\n')
    people.pop((counter % len(people) + next) % len(people) - 1)
    if (counter % (len(people)+1) + next) % (len(people)+1) == 0:
        next = 0
    else:
        next = (counter % (len(people)+1) + next) % (len(people)+1) - 1

print(f'Остался человек под номером {people[0]}')