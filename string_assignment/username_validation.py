'''
3.Check whether a username starts with "xm_"
contains only alphanumeric characters and underscore
length should be greater than 8
'''

username=input()
if username.startswith('xm_'):
    print('Starts with xm_')
else:
    print('doent not starts withxm_')

if  len(username)>8:
    print('lenth is greater than 8')
else:
    print('length should be greater than 8')
valid=True
for ch in username:
    if not (ch.isalnum() or ch=='_'):
        valid=False
        break
if valid and username.startswith("xm_") and len(username) > 8:
    print("Valid username")
else:
    print("Invalid username")