import pprint
import random


class MyValueError(ValueError):
    def __init__(self, txt):
        print(txt)


class OfficeEquipment:
    def __init__(self, tp: str, name: str, sn: str):
        self.tp = tp
        self.name = name
        self.sn = sn

    def __repr__(self):
        return f'{self.tp} {self.name} [s/n:{self.sn}]'


class Printer(OfficeEquipment):
    def __init__(self, tp: str, name: str, sn: str, color=False, laser=True):
        super().__init__(tp, name, sn)
        if isinstance(color, bool) and isinstance(laser, bool):
            self.color = color
            self.laser = laser
        else:
            raise MyValueError('Ошибка ввода, ожидался bool')

    def __repr__(self):
        return f'{super().__repr__()} ({("лазерный" if self.laser else "струйный")}, {("цветной" if self.color else "ч/б")})'


class Scanner(OfficeEquipment):
    def __init__(self, tp: str, name: str, sn: str, resolution_x: int, resolution_y: int):
        super().__init__(tp, name, sn)
        if isinstance(resolution_x, int) and isinstance(resolution_y, int):
            self.res_x = resolution_x
            self.res_y = resolution_y
        else:
            raise MyValueError('Ошибка ввода, ожидался int')

    def __repr__(self):
        return f'{super().__repr__()} ({self.res_x}x{self.res_y})'


class Copier(Scanner, Printer):
    def __init__(self, tp: str, name: str, sn: str, resolution_x: int, resolution_y: int, color=False, laser=True):
        Scanner.__init__(self, tp, name, sn, resolution_x, resolution_y)
        Printer.__init__(self, tp, name, sn, color, laser)

    def __repr__(self):
        return f'{Printer.__repr__(self)} ({self.res_x}x{self.res_y})'


class Warehouse:
    iid = 0

    def __init__(self, name: str):
        self.lst = []
        self.name = name

    def append(self, office_eq: OfficeEquipment):
        if isinstance(office_eq, OfficeEquipment):
            self.lst.append({'item': office_eq, 'id': self.iid, 'place': self.name})
            self.iid += 1
        else:
            raise MyValueError("Допустимо добавлять только объект класса OfficeEquipment")

    def move(self, dest: str, sn='', iid=-1):
        if -1 < iid < self.iid:
            for el in self.lst:
                if el['id'] == iid:
                    el['place'] = dest
                    break
        elif sn:
            for el in self.lst:
                if el['item'].sn == sn and el['place'] == self.name:
                    el['place'] = dest
                    break

    def available(self, dest='', ):
        lst = []
        if dest == '':
            dest = self.name
        for el in self.lst:
            if el['place'] == dest:
                lst.append(el)
        return lst


if __name__ == '__main__':
    wh = Warehouse('Склад №1')
    sns = []
    tps = ['Копир', 'Принтер', 'Сканер']
    nms = ['Xerox', 'HP', 'Canon', 'Brother', 'Epson']

    for _ in range(10):
        sns.append(str(random.randint(10000, 999999)))    #Рандомные серийные номера

    for i in range(3):                                    #Наполнение склада
        wh.append(Copier(tps[0], random.choice(nms), sns[i*3], 1200, 1600, color=True, laser=True))
        wh.append(Printer(tps[1], random.choice(nms), sns[i*3+1], color=False, laser=True))
        wh.append(Scanner(tps[2], random.choice(nms), sns[i*3+2], 2400, 3200))



    wh.move('Кабинет 305', iid=2)                      #Перемещение со склада в кабинет по инвентарному номеру
    wh.move('Кабинет 306', sn=sns[0])                  #Перемещение со склада в кабинет по серийнику
    pprint.pprint(wh.lst)                        #Список всей техники
    print("-"*50)
    pprint.pprint(wh.available('Кабинет 305'))   #Список техники в 305 кабинете
    print("-"*50)
    pprint.pprint(wh.available('Кабинет 306'))   #Список техники в 306 кабинете
    print("-"*50)
    pprint.pprint(wh.available())                #Список техники на складе

    print("-" * 50)
    try:
        wh.append(Copier(tps[0], random.choice(nms), sns[9], 1200, 'kk', laser='d'))
    except MyValueError:
        pass
