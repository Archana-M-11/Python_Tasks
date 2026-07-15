'''
7.Write a function sum_positive(*args) that:
Accepts any number of integers.
Returns the sum of only positive numbers.
Ignore negative numbers and zero.
 
'''
def sumPositive(*args):
    total=0
    for num in args:
        if num>0:
            total+=num
    return total
print(sumPositive(10, -5, 0, 20, 15))