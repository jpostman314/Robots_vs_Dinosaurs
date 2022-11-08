from weapon import Weapon

class Robot:

    def __init__(self, name, health, active_weapon):
        self.name = name
        self.active_weapon = active_weapon
        self.health = int(health)
    
    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - int(self.active_weapon.attack_power)
        return dinosaur.health