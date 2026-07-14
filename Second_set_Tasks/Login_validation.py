'''
4.Login Validation
 
Check
 
Username exists
Password correct
Account locked
Password expired
'''
username = input("Enter username: ")
password = input("Enter password: ")
correct_username = "admin"
correct_password = "1234"
account_locked = False
password_expired = False
if username != correct_username:
    print("Username does not exist")
elif account_locked:
    print("Account is locked")
elif password_expired:
    print("Password has expired")
elif password != correct_password:
    print("Incorrect password")
else:
    print("Login Successful")