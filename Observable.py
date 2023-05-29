from typing import List


class Observable:
    __observers: List[object] = []

    def attach(self, observer):
        self.__observers.append(observer)
        print(len(self.__observers))

    def detach(self, observer):
        self.__observers.remove(observer)

    def notifyAll(self, money = None):
        for observer in self.__observers:
                observer.update()
