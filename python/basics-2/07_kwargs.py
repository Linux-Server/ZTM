# Arguments and Keyword arguments

# *args and **kwargs

def calculate(*num):
    print(*num) 
    print(num) # this will be a tuple
    return sum(num)
    
calculate(1,2,3,4,5)


# print the highest even

def higeest_even(num):
    temp = []
    for i in num:
        if i%2 == 0:
            temp.append(i)
            
    return max(temp)
            
            
            

print(higeest_even([1,2,3,4,5,6,7,8,9, 10]))



