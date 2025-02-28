# Build a performance decorator
from time import time
def performance_decorator(func):
    def wrapper(num):
        start = time()
        func(num)
        end = time()
        print(f"The total time taken is {end-start} s")
    return wrapper
   






@performance_decorator
def calc_func(num):
    for i in range(num):
        i*5
        

calc_func(10000000)