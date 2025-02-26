def dec_func(func):
    def wrapper(argss):
        print("********")
        func(argss)
        print("********")
    return wrapper

@dec_func
def greet(my_args):
    print("hello Boss", my_args)
    
    
greet("Sachin")
