'''
4.Take a number from the user and remove its first occurrence from the list.
'''
numbers=list(map(int,input('enter the list:').split()))
num=int(input('enter the number to remove:'))
if num in numbers:
    numbers.remove(num)
print(numbers)