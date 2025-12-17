################## USE GLOBAL VARIABLE ###############################################
# balance = 0

# def main():
#     print("Blalance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Blalance:", balance)

# def deposit(n):
#     global balance
#     balance += n
# def withdraw(n):
#     global balance
#     balance -= n



# if __name__ == "__main__":
#     main()

################################## USE OOP ###############################################
class Account:
    def __init__(self):
        self._balance = 50
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        self._balance = balance
    
    def deposit(self, n):
        self.balance += n
    def withdraw(self, n):
        self.balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.balance = 0
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()