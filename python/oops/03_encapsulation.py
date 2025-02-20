# abstrction = hiding on info

class Person:
    def __init__(self, _name):
        self.name = _name
        
        
    def speak(self):
        return f"User is speaking..."
    
    

person_one = Person("sam")

print(person_one.name)
print(person_one.speak())

person_one.name = "john"
person_one.speak = "Killer clan"

print(person_one.name)
print(person_one.speak)