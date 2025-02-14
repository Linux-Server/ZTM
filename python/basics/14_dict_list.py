# list - its is orderd collection ,  can access with index
# dict - unorderd collection , can not access with index

my_dict = {True: "sachin", 100: 200, "name": "ray"}

print(my_dict[True])  


# to check a doict have a key

user = {
    "basket" : "Iphone",
    "name": "sam"
}

#print(user["ki"]) # this will throw error, bcoz key not exist

print(user.get("basket"))

# add default value if key not exist

print(user.get("sam", "billa"))

# creat an empty dict

my_dict = dict(name ="John")

print(my_dict)