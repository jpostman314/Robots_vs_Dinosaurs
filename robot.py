from weapon import Weapon

class Robot:

    def __init__(self, name, health, active_weapon):
        self.name = name
        self.active_weapon = active_weapon
        self.health = int(health)
    
    def attack(self, dinosaur):
        self.active_weapon = Weapon("Laser", 10)
        dinosaur.health = dinosaur.health - int(self.active_weapon.attack_power)
        print("")
        print(f"{dinosaur.name}'s remaining health is {dinosaur.health}")
        print("")
        if dinosaur.health <= 0:
            print("")
            print(f"{dinosaur.name} has died!")
            print("")
        