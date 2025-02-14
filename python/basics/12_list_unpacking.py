# List upacking

my_list = [1,2,3,4]
a,b,c,d = my_list

print(a)

print(my_list)


# upackaing a large list 

my_list = [1,2,3,4,5,6,7,8,9]

a,b, *other  , d= my_list

print(other)
print(d)