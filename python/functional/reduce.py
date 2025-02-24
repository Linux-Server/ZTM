from functools import reduce

my_list = [2,4,6,8]

def accumulator(acc, item):
    return acc + item


print(reduce(accumulator,my_list, 0))



#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def capitalizer(item):
    return item.upper()


print(list(map(capitalizer, my_pets)))


print(list(zip(my_strings, reversed(my_numbers))))


def pass_grade(num):
    return num > 50

print(list(filter(pass_grade, scores)))


# reduce
def accumator(acc, item):
    return acc + item

print(reduce(accumator, scores, sum(my_numbers)))
