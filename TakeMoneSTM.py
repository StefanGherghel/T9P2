from DisplayObserver import DisplayObserver

from Observable import Observable
from State import State



class TakeMoneySTM(Observable):

    __current_state: State
    __money: int = 0

    def __init__(self):
        self.__wait_state = WaitingForClient(self)
        self.__insert_money_state = InsertMoney(self)
        self.__current_state = self.__wait_state

        display = DisplayObserver
        self.attach(display)






    def set_current_state_waiting(self):
        self.__current_state = self.__wait_state

    def set_current_state_insert(self):
        self.__current_state = self.__insert_money_state

    def add_money(self, value: int):
        self.__money = self.__money + value
        self.update_amount_of_money(value)


    def update_amount_of_money(self, value:int):
        print('S-a introdus suma de ' + str (value))
        #self.notifyAll(value)

    def get_current_state(self):
        return self.__current_state
    def get_insert_state(self):
        return self.__insert_money_state

    def get_waiting_state(self):
        return self.__wait_state

class InsertMoney(State):
    __state_machine: TakeMoneySTM

    def __init__(self, take):
        self.__state_machine = take

    def insert_10bani(self):
        self.modify_price(10)
        self.__state_machine.add_money(10)

    def insert_50bani(self):
        self.__state_machine.add_money(50)
        self.modify_price(50)

    def insert_1leu(self):
        self.__state_machine.add_money(100)
        self.modify_price(100)

    def insert_5lei(self):
        self.__state_machine.add_money(500)
        self.modify_price(500)

    def insert_10lei(self):
        self.__state_machine.add_money(1000)
        self.modify_price(1000)


class WaitingForClient(State):
    __state_machine: TakeMoneySTM

    def __init__(self, take):
        self.__state_machine = take

    def client_arrived(self):
        self.__state_machine.set_current_state_insert()




