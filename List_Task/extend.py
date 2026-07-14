'''
2.Take two lists from the user and merge them using extend().
'''
arr=list(map(int,input('enter list1:' ).split()))
arr2=list(map(int,input('enter list2:' ).split()))
arr.extend(arr2)
print(arr)