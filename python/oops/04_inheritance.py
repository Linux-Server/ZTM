# inheritance

class User:   
    def sign_in(self):
        return "User signed iN"
        
        
class Wizrad(User):
    def __init__(self,name):
        self.name= name


class ARhcher:
    pass




wiz = Wizrad("Sam")
print(wiz.sign_in())


print(isinstance(wiz,User))