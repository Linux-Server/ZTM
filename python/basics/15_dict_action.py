my_dict = {
    "name" : "Sachin",
    "age": 30
}


print(my_dict)

# to check some thing exist in a dict

print("name" in my_dict)

# to check keys

print("name" in my_dict.keys())

# to check value exist

print(30 in my_dict.values())

# items

print(my_dict.items())

# remove 

my_dict.pop("name")

print(my_dict)

# pop the last itrm

print(my_dict.popitem())

print(my_dict)

my_dict.update({"name": "Sam"})
print(my_dict)

