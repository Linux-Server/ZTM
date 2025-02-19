class PlayerCharcter:
    membership = "Granted"
    # dunder or magic method
    def __init__(self, name):
        self.name = name
        
    def run(self):
        print("run")
        
    
    
# class is a blueprint of objects
# object is an instance of class

player_one = PlayerCharcter("samray")
print(player_one.run())
print(player_one.name)



player_one.attack = "Activated"

print(player_one.attack)

print(player_one.membership)