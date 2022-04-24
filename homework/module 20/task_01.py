students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests_namelen(stud_dict):
    interests = {x for i in stud_dict.keys() for x in stud_dict[i]['interests']}
    names_length = len([x for i in stud_dict.keys() for x in stud_dict[i]['surname']])
    return interests, names_length


id_age = [(index, student_info['age']) for index, student_info in students.items()]


print('Результат работы программы:')
print('Список пар "ID студента — возраст"', id_age)
print('Полный список интересов всех студентов:', interests_namelen(students)[0])
print('Общая длина всех фамилий студентов:', interests_namelen(students)[1])

