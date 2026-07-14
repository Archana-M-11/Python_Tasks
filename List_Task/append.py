'''
1.Create an empty list and ask the user to enter 5 numbers. 
Store them using append() and display the list.
'''
arr=[]
for i in range (5):
    num=int(input('enter the number:'))
    arr.append(num)
print('List: ',arr)
