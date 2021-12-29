def convert_name_extract(list_in: list) -> list:
    i = 0
    while i < len(list_in):
        empl_name = list_in[i][list_in[i].rfind(" ")+1:]
        list_in[i] = f'Привет, {empl_name.capitalize()}'
        i += 1
    list_out = list_in
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
