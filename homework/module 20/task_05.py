def look_for(search):
    for name, age in family.items():
        if search.lower() in name[0][:len(search)].lower():
            print(' '.join(name), age)


family = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидоров", "Павел"): 10,
    ("Смирнов", "Андрей"): 21,
    ("Смирнова", "Андрей"): 21,
    ("Алексеев", "Олег"): 40
}


while True:
    search_for = input('\nВведите фамилию: ')
    look_for(search_for)


