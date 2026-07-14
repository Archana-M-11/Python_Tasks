'''
3.Create a list of names and insert a new name at a position specified by the user.
'''
arr=['Archana','Anjali','anupama','anusree','anagha']
name=input('enter the name:')
n=int(input('enter the index: '))
arr.insert(n,name)
print(arr)
    