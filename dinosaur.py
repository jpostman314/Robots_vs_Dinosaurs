

class Dinosaur:

    def __init__(self, name, health, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = int(health)
    
    def attack_robot(self, robot):
        robot.health = robot.health - self.attack_power
        
        pass