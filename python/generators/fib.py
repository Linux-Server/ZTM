def calc(num):
    try: 
        l = list(range(20))
        fib = 0
        for i in l:
            fib += l[i] + l[i+1]
            
        return fib
    except IndexError:
        return fib
        
print(calc(20))


# 0,1,1,2,3,5,8,13
# 0,1,2,3,4,5,6,7