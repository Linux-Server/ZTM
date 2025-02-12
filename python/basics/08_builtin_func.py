# build in functions
print(len("sachin"))


# string methods
quote = "hello boss!"
print(quote.upper())

print(quote.capitalize())

print(quote.find("bo"))

print(quote.replace("bo", "voo"))


# Erecrcise:

birth_year  = input("what is ur DOB ?")
current_year = 2025


print(f"Your age is {current_year - int(birth_year)}")



# Comments your code

user_name = input("Enter ur username ? ")
password = input("Enter ur password ? ")

password_length = len(password)


print(f"Hola ! {user_name}, you password : {"*" * password_length} seems {password_length} char long..")



