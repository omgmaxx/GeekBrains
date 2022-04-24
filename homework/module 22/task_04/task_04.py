import os.path


def find_file(cur_path, fld_amt=0, fl_amt=0, weight=0):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isfile(os.path.join(path)):
            weight += os.path.getsize(path)
            fl_amt += 1
        if os.path.isdir(path):
            weight, fld_amt, fl_amt = find_file(path, fld_amt, fl_amt, weight)
            fld_amt += 1

    return weight, fld_amt, fl_amt


user_path = input('Введите путь до инспектируемой папки: ')
folder_bytes, folder_amt, file_amt = find_file(user_path)
folder_kb = round(folder_bytes / 1024, 8)


print('\n'+user_path)
print('Размер каталога (в Кб): {:,}\n'
      'Количество подкаталогов: {:,}\n'
      'Количество файлов: {:,}'.format(folder_kb, folder_amt, file_amt))
