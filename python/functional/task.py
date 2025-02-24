# comphrehension task


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

print(some_list)

# find duplicates

print(set([char for char in some_list if some_list.count(char) > 1]))