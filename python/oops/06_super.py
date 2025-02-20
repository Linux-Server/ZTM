
class User:
    def __init__(self, email):
        self.email = email
        
    def sign_in(self):
        print("Logged In")
        


class Wizard(User):
    def __init__(self, name, power,email):
        super().__init__(email)
        self.name = name
        self.power = power
        
    def attack(self):
        return f"attacking with power of {self.power}"
    
    
wiz_one = Wizard("sam", 101, "sam@gmail.com")
print(wiz_one.email)