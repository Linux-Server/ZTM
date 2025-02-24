my_list = [0,1,2,3,4]


# map

def multiply_by_two(item):
    return item * 10

print(multiply_by_two(10))

print(tuple(map(multiply_by_two, [100, 20])))


## filter

def is_even(num):
    return num%2 == 0


print(list(filter(is_even, my_list)))
