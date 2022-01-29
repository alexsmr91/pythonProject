import time


class TrafficLight:
    __color = ''

    def running(self):
        colors = ('красный', 'жёлтый', 'зелёный')
        times = (4, 2, 3)
        for i in range(len(times)):
            self.__color = colors[i]
            print(f'{self.__color} {times[i]} сек')
            time.sleep(times[i])


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
