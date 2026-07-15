'''
8.Write a function find_max(*args) that:
Accepts any number of integers.
Returns the largest number.
If no arguments are passed, return "No numbers provided".
'''
def find_max(*args):
    if len(args) == 0:
        return 'No numbers provided'
    maximum = float('-inf')
    for num in args:
        if num > maximum:
            maximum = num
    return maximum
print(find_max(10, 25, 7, 50, 18))  
print(find_max(-5, -2, -10))         
print(find_max())                    