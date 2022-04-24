rollers_list = []
users_list = []

rollers_amount = int(input('Кол-во коньков: '))
for i in range(rollers_amount):
    rollers_list.append(int(input(f'Размер {i + 1}-й пары: ')))

users_amount = int(input('\nКол-во людей: '))
for y in range(users_amount):
    users_list.append(int(input(f'Размер ноги {y + 1}-го человека: ')))


users_list.sort()
rollers_list.sort()
users_list.reverse()

for user in range(len(users_list)):
    for roller in range(len(rollers_list)):
        if rollers_list[roller] >= users_list[user] and rollers_list[roller] != 0 and users_list[user] != 0:
            users_list[user] = 0
            rollers_list[roller] = 0


print('\nНаибольшее кол-во людей, которые могут взять ролики:', users_list.count(0))