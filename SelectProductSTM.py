from Observable import Observable
from State import State

class SelectProductSTM(Observable):


    def __init__(self):

        self.__select_product_state = SelectProduct(self)
        self.__coca_cola_state = CocaCola(self)
        self.__coca_cola_state.set_price(50)
        self.__pepsi_state = Pepsi(self)
        self.__sprite_state = Sprite(self)
        self.__current_state = self.__select_product_state

    def choose_another_product(self):
        self.__select_product_state.choose()
        #self.notifyAll()

    def setSpriteState(self):
        self.__current_state = self.__sprite_state

    def setColaState(self):
        self.__current_state = self.__coca_cola_state

    def setPepsiState(self):
        self.__current_state = self.__pepsi_state


    def return_current_state(self):
        return self.__current_state


class SelectProduct(State):
    __state_machine: SelectProductSTM


    def __init__(self, SPSTM):
        self.__state_machine = SPSTM
    def choose(self):
        optiune = input('Introduceti optiunea: COLA/SPRITE/PEPSI')
        if(optiune == "COLA"):
            self.__state_machine.setColaState()
        if (optiune == "PEPSI"):
            self.__state_machine.setPepsiState()
        if (optiune == "SPRITE"):
            self.__state_machine.setSpriteState()

    def set_price(self, price):
        self._price = price

class CocaCola(State):
    __state_machine: SelectProductSTM

    def __init__(self, SPSTM):
        self.__state_machine = SPSTM

    def set_price(self, price):
        self._price = price



class Pepsi(State):
    __state_mchine: SelectProductSTM

    def __init__(self, SPSTM):
        self.__state_machine = SPSTM

    def set_price(self, price):
        self._price = price

class Sprite(State):
    __state_mchine: SelectProductSTM


    def __init__(self, SPSTM):
        self.__state_machine = SPSTM

    def set_price(self, price):
        self._price = price

