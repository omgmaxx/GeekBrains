import re


if __name__ == '__main__':
    numbers_list = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

    owned_autos = re.findall(r'\b\w\d{3}\w{2}\d{2,3}\b', numbers_list)
    taxi_autos = re.findall(r'\b\w{2}\d{3}\d{2,3}\b', numbers_list)

    print('Список номеров частных автомобилей:', owned_autos,
          '\nСписок номеров такси:', taxi_autos)
