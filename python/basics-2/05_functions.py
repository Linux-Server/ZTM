
def say_hello(name = "Sachin" , emoji = "👀"):
    print(f"Hello {name} {emoji}")
    
say_hello("sam", '😂')


# default arguments

say_hello()



def sum(n1,n2):
    
    def another(num1, num2):
        return num1 + num2
    
    return another(n1,n2)


print(sum(1,2))


