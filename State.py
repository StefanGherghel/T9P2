from abc import ABC



#clasa state are metodele si proprietatea legata de pret, pe care le impartaseste u majoritatea starilor
class State(ABC):
    _price: int = 0
    def get_price(self):
        return self._price

    def modify_price(self, add:int):
        self._price = self._price + add

    def reset_state_price(self):
        self._price = 0
