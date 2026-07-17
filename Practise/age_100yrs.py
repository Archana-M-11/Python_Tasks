'''
1.Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
'''
name=input('enter the name : ')
age=int(input('enter the age: '))
cur_year=2026
res=cur_year+(100-age)
print(name,'You will be 100 in the year :',res)