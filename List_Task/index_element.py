'''
6.Find the index of a given element.
'''
numbers = list(map(int,input('enter the list').split()))
num = int(input("enter element: "))
if num in numbers:
    print("index:", numbers.index(num))
else:
    print("Element not found")