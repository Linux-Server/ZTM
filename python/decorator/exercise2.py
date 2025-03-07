# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args):
        print(args)
        
        if args[0]["valid"]:
             fn(args)
        else:
            print("No a valid user")
    return wrapper
            
       

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)