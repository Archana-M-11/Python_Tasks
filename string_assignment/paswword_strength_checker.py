'''
7.Create a Password Strength Checker
 
Conditions:
 
At least 8 characters
Contains uppercase
Contains lowercase
Contains digit
Contains special character
'''

pas=input()
upper = False
lower = False
digit = False
special = False
for ch in pas:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True
if len(pas)>=8 and upper and lower and digit and special:
    print('strong password')
else:
    print('weak password')