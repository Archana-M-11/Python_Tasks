'''
Write a Python decorator named timer that measures and displays the execution time of any function it decorates.
'''
def validate_numbers(func):
    def wrapper(*args):
        for i in args:
            if not isinstance(i, int):
                print('All positional arguments must be integers')
                return
        return func(*args)
    return wrapper
@validate_numbers
def add(a, b):
    print('Sum:', a + b)
add(10, 20)      
add(10, "20")    