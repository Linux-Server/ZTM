# Higher Order Funtion - a function which can accept another function a parameter or return a function

def greet(func):
    func()
    
    
def greet2():
    def wohoo():
        print("Wohooo")
    
    return wohoo
    

def hello():
    print("hello")

def hi():
    print("hi")
    
    
greet2()