class BankAccount:
    def __init__(self,balance,name):
        self.name=name
        self.__balance=balance
    def get__balance(self):
        return self.__balance
    #Scatters
    def set_balance(self,amount):
        if amount>0 :
            self.__balance+=amount
        else:
            print("INVAILD BALANCE AMOUNT")

#Main
account=BankAccount(500,"Andrews")
print(account.get__balance())
account.set_balance(500)
print("Total after adding",account.get__balance())        
        