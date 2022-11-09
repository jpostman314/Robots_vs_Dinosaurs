from weapon import Weapon
from dinosaur import Dinosaur


class Robot:

    def __init__(self, name, health, active_weapon):
        self.name = name
        self.active_weapon = active_weapon
        self.health = int(health)
        self.weapons_list = [Weapon("Toxic Gas", 10), Weapon("Flame Thrower", 20), Weapon("Laser", 25)]



    def attack(self, dinosaur):
        
        user_selection = input("Which weapon would you like the robot to attack with? [type 1 for Toxic Gas, type 2 for Flame Thrower, or type 3 for Laser] ")
        self.active_weapon = self.weapons_list[int(user_selection)-1]
        dinosaur.health = dinosaur.health - int(self.active_weapon.attack_power)
        print("")
        print(f"{dinosaur.name}'s remaining health is {dinosaur.health}")
        print("")
        if dinosaur.health <= 0:
            print("")
            print(f"{dinosaur.name} has died!")
            print("")
    

