class Person:
    """The person class is blueprint to create instance of this class"""
    # class atrribute
    is_born = True
    
    # constructor
    def __init__(self, _name):
        # instance attribute
        self.name = _name
        
    def run(self):
        return "person is running"
    
    @classmethod
    def is_alive(cls):
        return "Person is  alive and kicking"
    
    @staticmethod
    def adding(num1,num2):
        return num1 + num1
        
        


person_one = Person("Samray")

print(person_one.name)

print(person_one.run())

print(person_one.is_born)

print(person_one.is_alive())

print(person_one.adding(10,20))