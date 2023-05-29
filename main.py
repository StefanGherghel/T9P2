from SelectProductSTM import SelectProductSTM
from VendingMachineSTM import  VendingMachineSTM
from TakeMoneSTM import TakeMoneySTM


if __name__ == '__main__':
    print('Incepem programul')


    vending = VendingMachineSTM()

    vending.turn_it_on()
    on = True
    while(on):
        x= int (input("1. Proceed to check out      2. Exit"))
        if(x==1):
            vending.proceed_to_checkout()
        if(x==2):
            on = False


    #decim am facut o clasa SelectProductSTM in care am implementat toate clasele necesare pentru automatul SelectProduct
    #am adaugat functii ajutatoare de setare a starii curente
    #plus functie de returnare a starii curente

    #in functia choose another product se apleaza functia choose ce apartine SelectProduct si ar trebui sa dau notify observatorului


    #in starea SelectProduct, metoda choose:
        #daca se alege o anumita optiune se da update la starea curenta: (cola, sprite)


    #in automatul TakeMoneySTM
    #adaug doua stari: Waiting si Insert
    #adaug si observatorul de display al sumei
    #am adaugat la implementare si functii de setare a starii curente

    #metoda add money adauga banii la variabila money si apeleaza metoda de update care ar trebui sa dea notify observatorului?
    #metoda add money este apelata de fiecare data cand se da call la una dintre metodele insert

    #in metodele insert dau call la metoda add si adaug la price (adica la cati bani au fost introdusi) noua valoare
    #acest price al lui insert ma ajuta sa fac checkout-ul, deoarece compar valoarea unui produs cu valoare inserata pana intr un moment

    #cum fac update -ul observatorilor?

