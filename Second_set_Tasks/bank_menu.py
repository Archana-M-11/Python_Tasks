'''
5.Using match..case do the following task in the menuaccoring to user's choice
1. Banking Menu
1 Deposit
 
2 Withdraw
 
3 Balance
 
4 Mini Statement
 
5 Exit
 
Use match-case.
'''
balance=10000
print('1.Deposit')
print('2.Withdraw')
print('3.Balance')
print('Mini Statement')
print('Exit')
choice=int(input())
match choice:
    case 1:
        amount=int(input('enter the deposit amount: '))
        balance+=amount
        print('Balance Amount:',balance)
    case 2:
        withdraw=int(input('enter the amount to withdraw:'))
        if withdraw<=balance:
            balance-=withdraw
            print('Balance Amount:',balance)
        else:
            print('no sufficient balance!')
    case 3:
        print('Balance:',balance)
    case 4:
        print('Balance:',balance)
    case 5:
        print('Thank you')
    case _:
        print('invalid input')

