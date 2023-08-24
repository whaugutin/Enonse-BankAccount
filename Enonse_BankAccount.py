class BankAccount():

    def __init__(self, account_number, account_holder, initial_balance):
        if initial_balance < 500.0:
            print("Ou sipoze ouvri kont lan 500.0 HTG pou pi piti")
        else:
            self.account_number = account_number
            self.account_holder = account_holder
            self.initial_balance = initial_balance

    def deposit(self, amount):
        self.amount = amount
        self.initial_balance += amount
    
    def withdraw(self, amount):
        if amount > self.initial_balance:
            print("Ou pa gen tout kòb sa sou kont ou")
        else:
            self.amount = amount
            self.initial_balance -= amount
    
    def get_balance(self):
        print(f"Balans ou se {self.initial_balance}")
    
    def __str__(self):
       return f"\nAccount Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalnce: {self.initial_balance} HTG"

# Create an account
account_1 = BankAccount("10319173", "Whitchy", 10_000.00)

# Deposit
try:
    account_1.deposit(1_000_000.00)
except:
    pass
else:
    # Withdrawal
    account_1.withdraw(500_000.00)

    # Check the balance of the account 
    balance = account_1.get_balance()

    # Display account info
    print(account_1)

