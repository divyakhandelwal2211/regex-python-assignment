# class Bank_Account:

#     def __init__(self, accNo, name, balance):
#         self.accNo = accNo
#         self.name = name
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount < 0:
#             print("invalid amount for deposit")
#         else:
#             self.__balance = self.__balance + amount

#     def withdrawAmount(self, amount):
#         if amount > self.__balance:
#             print("Insufficient amount")
#         else:
#             self.__balance -= amount

#     @property
#     def get_balance(self):
#         return self.__balance

#     @get_balance.setter
#     def get_balance(self, value):
#         self.__balance = value


# class Saving_account(Bank_Account):
#     def __init__(self, accNo, name, balance):
#         self.min_balance = 500
#         if balance > self.min_balance:
#             super().__init__(accNo, name, balance)

#     def withdrawAmount(self, amount):
#         new_balance = self.get_balance
#         if new_balance - amount >= self.min_balance:
#             self.get_balance = new_balance - amount
#             print(f"Saving withdraw {amount} New balance is {new_balance}")
#         else:
#             print(f"Can't withdraw as manage the minimum amount {self.min_balance}")


# class Current_account(Bank_Account):
#     def __init__(self, accNo, name, balance):
#         super().__init__(accNo, name, balance)

#     def withdrawAmount(self, amount):
#         super().withdrawAmount(amount)


# c1 = Saving_account(123, "divya", 1000)
# c1.withdrawAmount(300)
# balance = c1.get_balance
# print(balance)


import mysql.connector


class Bank_Account:
    def __init__(self, accNo, name, balance, account_type="general"):
        self.accNo = accNo
        self.name = name
        self.__balance = balance
        self.account_type = account_type
        self.save_to_db()

    def db_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",  # Use your MySQL username
            password="sql@1234",  # Use your MySQL password
            database="bank_db",
        )

    def save_to_db(self):
        conn = self.db_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO bank_account (accNo, name, balance, account_type)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE name=%s, balance=%s, account_type=%s
        """
        data = (
            self.accNo,
            self.name,
            self.__balance,
            self.account_type,
            self.name,
            self.__balance,
            self.account_type,
        )
        cursor.execute(query, data)
        conn.commit()
        conn.close()

    def deposit(self, amount):
        if amount < 0:
            print("invalid amount for deposit")
        else:
            self.__balance += amount
            self.save_to_db()

    def withdrawAmount(self, amount):
        if amount > self.__balance:
            print("Insufficient amount")
        else:
            self.__balance -= amount
            self.save_to_db()

    @property
    def get_balance(self):
        return self.__balance

    @get_balance.setter
    def get_balance(self, value):
        self.__balance = value
        self.save_to_db()


class Saving_account(Bank_Account):
    def __init__(self, accNo, name, balance):
        self.min_balance = 500
        if balance > self.min_balance:
            super().__init__(accNo, name, balance, account_type="saving")

    def withdrawAmount(self, amount):
        new_balance = self.get_balance
        if new_balance - amount >= self.min_balance:
            self.get_balance = new_balance - amount
            print(f"Saving withdraw {amount}, New balance is {self.get_balance}")
        else:
            print(f"Can't withdraw. Maintain minimum balance: {self.min_balance}")


class Current_account(Bank_Account):
    def __init__(self, accNo, name, balance):
        super().__init__(accNo, name, balance, account_type="current")

    def withdrawAmount(self, amount):
        super().withdrawAmount(amount)


c1 = Saving_account(123, "divya", 1000)
c1.deposit(500)
c1.withdrawAmount(300)

s1 = Saving_account(101, "radha", 2000)
s1.deposit(500)
s1.withdrawAmount(1000)

c1 = Current_account(201, "ram", 3000)
c1.deposit(200)
c1.withdrawAmount(500)
