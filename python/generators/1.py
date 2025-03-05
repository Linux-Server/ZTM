# Python generators
def my_func():
    yield 1
    yield 2
    yield 3
    
d = my_func()
print(next(d))
print(next(d))
print(next(d))

s = my_func()
print(next(s))


my_list = [1,2,3,4]

n = iter(my_list)

for i in n:
    print(i)