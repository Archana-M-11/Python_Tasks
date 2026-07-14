'''
5.Remove the last element and display both the removed element and updated list.
'''
numbers=list(map(int,input('enter the list:').split()))
res=numbers.pop()
print('last element:',res)
print('balnce list:',numbers)