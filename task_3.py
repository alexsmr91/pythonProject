def thesaurus(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out = {}  # результирующий словарь значений
    for empl_name in args:
        frst_ltr = empl_name[:1].upper()
        if dict_out.get(frst_ltr) == None :
            new_entry = {frst_ltr: [empl_name]}
            dict_out.update(new_entry)
        else:
            dict_out[frst_ltr].append(empl_name)
    return dict_out


def sort_dict(dict_in: dict) -> dict:
    dict_out = {}
    for ele in sorted(dict_in):
        dict_out[ele] = dict_in[ele]
    return dict_out



names_dict = thesaurus("Иван", "Мария", "Петр", "илья", "Алексей", "Антон", "Ярослав", "Юрий", "Григорий", "Денис")
print(names_dict)
names_dict = sort_dict(names_dict)
print(names_dict)


