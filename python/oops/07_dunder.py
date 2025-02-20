class Toy:
    def __init__(self, color, age):
        self.name = color
        self.age = age
        
    def __str__(self):
        return f"its a toy broo"
    
    def __len__(self):
        return 100
    
    def __call__(self):
        print("Im called")
        


toy = Toy("red", 12)

print(toy.__str__())

print(str(toy))

print(len(toy))

toy()

