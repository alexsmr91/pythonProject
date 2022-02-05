class MyValueError(ValueError):
    def __init__(self, txt):
        print(txt)


class MyList:
    def __init__(self):
        self.lst = []

    def append(self, el):
        try:
            int(el)
        except ValueError:
            raise MyValueError('Можно вводить только числа')
        else:
            self.lst.append(int(el))

    def __str__(self):
        return f'{self.lst}'


if __name__ == '__main__':
    my_list = MyList()
    while True:
        st = input('Введите число: ')
        if st.lower() != 'stop':
            try:
                my_list.append(st)
            except MyValueError:
                pass
        else:
            break
    print(my_list)

