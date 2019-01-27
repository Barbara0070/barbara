class CashMachine:
    #is_available == False
    def __init__(self):
        self._money = []
    @property
    def is_available(self):
        if self._money == True:
            return True
        return False
    def put_money(self, bills_list):
        self._money.extend(bills_list)
        print(self._money)
    def withdraw_money(self,x):
        money_to_withdraw=[]
        self._money.sort(reverse=True)
        if x==50 or x==100 or x==200:
            for bill in self._money:
                if x==bill:
                    self._money.remove(x)
                    return self._money
        for bill in self._money:
            money_to_withdraw+=bill
            if sum(money_to_withdraw)==x:
                for temp_bill in money_to_withdraw:
                    self._money.remove(temp_bill)




#a.sort(reverse=True)
#sorted(a) zwraca kopie



cash_machine = CashMachine()
print(cash_machine.is_available)
cash_machine.put_money([50,100,50,200])
print(cash_machine.is_available)
cash_machine.withdraw_money(150)
print(cash_machine._money)






#def test_cash_machine_is_not_available():
#    cash_machine = CashMachine()
#    assert not cash_mashine.is_available
#def test_cash_machhine_put_money():
#    cash_machine=CashMachine()
#def test_cash_machine_withdraw_money:
#    cash_machine.put_money([200, 100, 100,50])
#    assert cash_machine_withdraw_money(150)==[100,50]