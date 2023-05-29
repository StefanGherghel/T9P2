from ChoiceObserver import ChoiceObserver
from SelectProductSTM import SelectProductSTM
from TakeMoneSTM import TakeMoneySTM


class VendingMachineSTM:

    rest: int = 0

    def __init__(self):
        self.__take_money_stm = TakeMoneySTM()
        self.__select_product_stm = SelectProductSTM()
        choice = ChoiceObserver()
        self.__select_product_stm.attach(choice)

    def proceed_to_checkout(self):


        if(self.__select_product_stm.return_current_state().get_price()<=self.__take_money_stm.get_insert_state().get_price()):
            print('Gata, ati introdus toata suma')
            print('1. Continua cumparaturile ')
            print('2. Incheie si returneaza-mi restul')
            x = int(input())
            if(x==1):
                self.__select_product_stm.choose_another_product()
                self.rest = self.rest + self.__take_money_stm.get_insert_state().get_price() - self.__select_product_stm.return_current_state().get_price()
                self.__take_money_stm.get_insert_state().reset_state_price()
            else:
                print("Aceste este restul dvs: " + str(self.rest))
                self.__take_money_stm.set_current_state_waiting()
        else:
            print('Inca nu ati introdus toti banii')
            print('Introduceti: 1. 10 bani\n 2.50 bani\n 3. 1leu\n 4. 5 lei\n 5. 10 lei')
            x = int (input())
            if(x==1):
                self.__take_money_stm.get_insert_state().insert_10bani()
            if (x == 2):
                self.__take_money_stm.get_insert_state().insert_50bani()
            if (x == 3):
                self.__take_money_stm.get_insert_state().insert_1leu()
            if (x == 4):
                self.__take_money_stm.get_insert_state().insert_5lei()
            if (x == 5):
                self.__take_money_stm.get_insert_state().insert_10lei()

    def turn_it_on(self):

        self.__select_product_stm.choose_another_product()



