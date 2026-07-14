'''
8.Create a copy of a list and modify the copied list. 
Verify that the original list remains unchanged.
'''
arr=list(map(int,input('enter the list:').split()))
arr2=arr.copy()
n=int(input('enter a element to copied list:'))
arr2.append(n)
print('original:',arr)
print('copied:',arr2)