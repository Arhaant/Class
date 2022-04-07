class ATM:
    def __init__(self,CardNo,PinNo):
        self.CardNo = CardNo
        self.PinNo = PinNo
    def balance(self):
        print('Your balance is 10000')
    def withdraw(self,amount):
        newBalance = 10000-amount
        print('Your new balance is ', newBalance)


a1 = ATM(1234,900990)
print(a1.CardNo)
a1.balance()
a1.withdraw(5000)
        