calc = lambda x : x+10

print(calc(100))
print(calc(200))


my_list =[2,4,6,8]


print(list(map(lambda x: x+ 10 ,my_list)))


print(list(filter(lambda x: x%2 != 0 ,my_list)))


# lambda express to square a list

print(list(map(lambda x : x**2, my_list)))

# list sorting based on 2 nd value
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

