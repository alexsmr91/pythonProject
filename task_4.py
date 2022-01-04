

def sort_dict(dict_in: dict) -> dict:
    dict_out = {}
    for ele in sorted(dict_in):
        dict_out[ele] = dict_in[ele]
    return dict_out



def thesaurus_adv(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out = {}  # результирующий словарь значений
    for empl_name in args:
        frst_ltr_surn = empl_name.split(' ')[1][:1].upper()
        frst_ltr_name = empl_name[:1].upper()
        if dict_out.get(frst_ltr_surn) == None:
            new_entry = {frst_ltr_surn: {frst_ltr_name:[empl_name]}}
            dict_out.update(new_entry)
        elif dict_out[frst_ltr_surn].get(frst_ltr_name) == None:
            new_entry = {frst_ltr_name:[empl_name]}
            dict_out[frst_ltr_surn].update(new_entry)
        else:
            dict_out[frst_ltr_surn][frst_ltr_name].append(empl_name)
    return dict_out



def surn_out(dict_in:dict)-> str:
    str_out = ""
    for entr in dict_in:
        str_out = f"{str_out}Фамилии на букву {entr}\n{name_out(sort_dict(dict_in[entr]))}\n"
    return str_out



def name_out (dict_in: dict)-> str:
    str_out = ""
    for entr in dict_in:
        str_out = f"{str_out}    Имена на букву {entr}\n"
        for nam in dict_in[entr]:
            str_out = f"{str_out}        {nam}\n"
    return str_out



surn_dict = thesaurus_adv("Иван Сергеев", "инна серова", "Петр Алексеев", "Илья Иванов",
                          "Анна Савельева", "Ирина Иванова", "Эльмира Башмакова", "Леонид Тагиров",
                          "Анатолий Торф", "наталья шабанова", "Денис аксаков", "Тигран Мышкин")
surn_dict = sort_dict(surn_dict)
print(surn_dict)
print(surn_out(surn_dict))

