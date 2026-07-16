'''
Write a Python decorator named timer that measures and displays the execution time of any function it decorates.
'''
import time
def timer(func):
    def wrapper():
        start = time.time()         
        func() 
        end = time.time()            
        print(f'Execution Time: {end - start:.6f} seconds')
        return
    return wrapper
@timer
def display():
    for i in range(5):
        print(i)
        time.sleep(1)   
display()