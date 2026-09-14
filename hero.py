import random
class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self,name):
        self.name = name
        self.health = 127
        self.attack_power = 23
    def attack(self):
        return random.randint(1,self.attack_power)
    def Damage_cry(self):
            print("Ahhhhhhhhh!!!!!!")
    def take_damage(self, damage):
        self.health = max(0,self.health - damage)
        print (f"{self.name} takes {damage} damage. Health: {self.health}")
        self.Damage_cry()
    def is_alive(self):
        return self.health > 0
