class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.interest_rate = 0.01

    def deposit(self, amnt):
        self.balance += amnt
        
    def withdraw(self,amnt):
        self.balance -= amnt
        
    def get_balance(self):
        return self.balance

    def set_interest_rate(self, intr):
        self.interest_rate = intr

    def apply_interest(self):
        self.balance = self.balance * (1 + self.interest_rate)
        
