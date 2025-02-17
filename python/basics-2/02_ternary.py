user_status =False
user_name = "Samray"


name = user_name if user_status else "no name"

print(name)


# short circuting

# logical opertor ecrecise

is_magician = False
is_expert = True

if is_magician and is_expert:
    print("you are a master amgician")
elif is_magician and not is_expert : 
    print("alteast u are getting there")
    
else: 
    print("you nee magic power")
    

