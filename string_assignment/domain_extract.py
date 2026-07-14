'''
6.Write a program to extract domain from email address.
'''
domain=input()
domain=domain.split('@')
print(domain[1])