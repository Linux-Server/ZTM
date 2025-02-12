# list  - ordered sequence of object, any datatype

amazon_cart  = ["notebooks", "watch", "laptop"]

print(amazon_cart[0])

amazon_cart[0] = "snickers"

print(amazon_cart)

# create a new list rather than updation

# here we are creating a copy of the list
new_cart = amazon_cart[0:2]
print(new_cart)
print(amazon_cart)

# here we are pointing to same memory

test_cart = amazon_cart
test_cart[0] = "phone"

print(amazon_cart)


# lesson
# if u want to copy a list u do
cart_one = amazon_cart[:]
cart_one[0] = "iphone"
print(f"cart_one : {cart_one}  and amazon cart : {amazon_cart}")

 
