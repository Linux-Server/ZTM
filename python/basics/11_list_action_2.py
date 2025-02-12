basket = ["shoes", "laptop", "iphone", "watch"]

print(basket.index("iphone"))

print("watch" in basket)

print("s" in "sachin")

# count the number of items in list

print(basket.count("iphone"))


# Sort ans sorted

new = [1,32,42,4,5]

new.sort() # this will update the list

print(new)

one = [8,2,45,6,1]

two = sorted(one) # create a new list

print(one, two)


# reverse  a list

basket = [9,42,6,1,8]
basket.sort()
basket.reverse()
print(basket)

# reverse and creat e a new list

new_basket = basket[:]
new = new_basket[::-1]
print(new)

# join string

sentanece = "!"

new = sentanece.join(["hello", "my", "dear"])

print(new)

# an easy way of joining string is : 

print("Trump".join(["All", "Hell", "will", "break", "out"]))

print(" ".join(["All", "Hell", "will", "break", "out"]))
