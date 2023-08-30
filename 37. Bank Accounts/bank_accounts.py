# Write code below 💖

class BankAccount:

    balance: object

    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.first_name = first_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance


    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance


    def display_balance(self):
        print(f"The balance is {self.balance}")


Santander = BankAccount('Sonic', ' the Hedgehog', 1234, 'Credit', 1234, 150.50)

Santander.deposit(50.50)

Santander.display_balance()

Santander.withdraw(20)

Santander.display_balance()