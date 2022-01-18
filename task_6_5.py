

def prepare_file(path_users_file: str, path_hobby_file: str, path_output_file: str):
    with open(path_hobby_file, 'r', encoding='utf-8') as f1,\
            open(path_users_file, 'r', encoding='utf-8') as f2,\
            open(path_output_file, 'w', encoding='utf-8') as f3:
        for line in f2:
            hobby = f1.readline().strip()
            if hobby:
                f3.write(f'{line.strip()}: {hobby}\n')
            else:
                f3.write(f'{line.strip()}: None\n')
        hobby = f1.readline()
        if hobby:
            sys.exit(1)
    return None



def main(argv):
    program, path_users_file, path_hobby_file, path_output_file = argv
    prepare_file(path_users_file, path_hobby_file, path_output_file)



if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4:
        exit(main(sys.argv))
    else:
        raise TypeError("Ожидались аргументы: <адрес_файла_с_именами_пользователей> <адрес_файла_с_хобби> <адрес_выходного_файла>")



