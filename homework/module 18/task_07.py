ip = str(input('Введите IP: ')).split('.')


if len(ip) != 4:
    print('Адрес — это четыре числа, разделённые точками.')
else:
    for group in ip:

        if not group.isdigit():
            print(group, '— это не целое число.')
            break

        if int(group) > 255:
            print(group, 'превышает 255.')
            break

    else:
        print('IP-адрес корректен.')
