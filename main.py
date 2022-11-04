class BankAccount(object):
    defaultAccNumber = 1

    def __init__(self, name, balance = 0) -> None:
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber + 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough balance!")
        else:
            self.balance -= amount

    def getBalance(self):
        return self.balance


if __name__ == '__main__':
    myobj = BankAccount('Saurav', 100000)
    myobj.deposit(2000)
    print(myobj.getBalance())
    myobj.withdraw(1500)
    print(myobj.getBalance())

