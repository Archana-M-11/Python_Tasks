'''
1.Create a Bank_account class.
Methods:
deposit()
withdraw()
check_balance()
Rules:
Balance cannot become negative.
Display appropriate messages.
'''
class Bank_account():
    def __init__(self,amount):
        self.amount=amount
    def deposit(self,amount):
        self.amount+=amount
        print(f'Balance:{self.amount}')
    def withdraw(self,amount):
        if self.amount>=amount:
            print(f'{self.amount}-{amount}')
            self.amount-=amount            
            print(f'Balance:{self.amount}')
        else:
            print(f'insufficient amount')
    def check_balance(self):
        print(f'Balance:{self.amount}')
account=Bank_account(1000)
account.deposit(5000)
account.withdraw(300)
account.check_balance()
