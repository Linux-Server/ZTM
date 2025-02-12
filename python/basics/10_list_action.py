# list actions

basket = [1,2,3,4,5,6]
new_basket = basket

basket.append(100)


print(basket, new_basket)

basket.insert(0, 10)

print(new_basket)

# adding another list to  list

new_basket.extend(["shoes", "laptop"])

print(basket)

# Removing

basket.pop()

print(basket)

basket.pop(0)

print(basket)

basket.remove(100)

print(basket)