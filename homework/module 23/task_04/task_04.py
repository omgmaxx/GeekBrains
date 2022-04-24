def main_func():
    open('registrations_bad.log', 'w').close()
    open('registrations_good.log', 'w').close()             # очищение логов

    with open('registrations.txt', 'r', encoding='utf-8') as input_txt:
        for line in input_txt:
            line = line.split()
            exceptions(line)


def exceptions(line):
    message = ''
    try:
        checks(line)
    except IndexError:
        message = 'НЕ присутствуют все три поля: IndexError.'
    except NameError:
        message = 'Поле имени содержит НЕ только буквы: NameError.'
    except SyntaxError:
        message = 'Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.'
    except ValueError:
        message = 'Поле «Возраст» НЕ является числом от 10 до 99: ValueError.'
    finally:
        sent_out(message, line)


def checks(line):
    if len(line) != 3:
        raise IndexError
    if not line[0].isalpha():
        raise NameError
    if '@' not in line[1] or '.' not in line[1]:
        raise SyntaxError
    if int(line[2]) < 10 or int(line[2]) > 99:
        raise ValueError


def sent_out(message, line):
    log_type = 'good'
    if message:
        log_type = 'bad'
    with open('registrations_'+log_type+'.log', 'a', encoding='utf-8') as log_file:
        line = ' '.join(line)
        log_file.write('{: <40}{: <80}\n'.format(line, message))


main_func()
