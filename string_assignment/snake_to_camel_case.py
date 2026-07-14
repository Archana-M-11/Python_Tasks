'''
10.snake_to_camel_case.py
'''
s=input('enter the snale case: ').split('_')
camel=s[0]
for ch in s[1:]:
    camel+=ch.title()
print('In cammelCase:',camel)    
