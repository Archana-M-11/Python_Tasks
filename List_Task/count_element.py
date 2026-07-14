'''
7.Count how many times a number appears in a list.
'''
numbers=list(map(int,input('enter the list:').split()))
num=int(input('enter the number : '))
count=numbers.count(num)
print(count)
