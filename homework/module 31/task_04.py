import re


if __name__ == '__main__':
    numbers_list = ['9999999999', '999999-999', '99999x9999']

    for x in numbers_list:
        if re.match(r'\b[89]\d{9}\b', x):
            print(x+': всё в порядке')
        else:
            print(x+': не подходит')
