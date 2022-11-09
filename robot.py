from weapon import Weapon

class Robot:

    def __init__(self, name, health, active_weapon):
        self.name = name
        self.active_weapon = active_weapon
        self.health = int(health)
       



    def attack(self, dinosaur):
        
        laser = Weapon("Laser", 25)
        flame_thrower = Weapon("Flame Thrower", 20)
        toxic_gas = Weapon("Toxic Gas", 10)
        active_weapon = input("Which weapon would you like the robot to attack with? [Toxic Gas, Flame Thrower, or Laser] ")
        self.active_weapon = active_weapon
        dinosaur.health = dinosaur.health - int(self.active_weapon.attack_power)
        print("")
        print(f"{dinosaur.name}'s remaining health is {dinosaur.health}")
        print("")
        if dinosaur.health <= 0:
            print("")
            print(f"{dinosaur.name} has died!")
            print("")
    

