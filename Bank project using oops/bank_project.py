class Bank_Account:

    def __init__(self, accNo, name, balance):
        self.accNo = accNo
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("invalid amount for deposit")
        else:
            self.balance = self.balance + amount

    def withdrawAmount(self, amount):
        if amount > self.balance:
            print("Insufficient amount")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.__balance


class Saving_account(Bank_Account):
    def __init__(self, accNo, name, balance):
        self.min_balance = 500
        if balance > self.min_balance:
            super().__init__(accNo, name, balance)

    def withdrawAmount(self, amount):
        new_balance = self.get_balance()
        if new_balance - amount >= self.min_balance:
            new_balance -= amount
            print(f"Saving withdraw {amount} New balance is {new_balance}")
        else:
            print(f"Can't withdraw as manage the minimum amount {self.min_balance}")


class Current_account(Bank_Account):
    def __init__(self, accNo, name, balance):
        super().__init__(accNo, name, balance)

    def withdrawAmount(self, amount):
        super().withdrawAmount(amount)


c1 = Current_account(123, "divya", 1000)
c1.get_balance()
c1.withdrawAmount(300)
print(c1.balance)
