
my_list = [1,2,3,4,5,6,7,8,9]

new_list = [num**2 for num in my_list if num < 5]

print(new_list)


# dict comprehension

my_dict = {"name" : 44,
           "age":  22}

print({key:value+10 for key,value in my_dict.items()})

print({num:num + 2 for num in [1,2,3]})

