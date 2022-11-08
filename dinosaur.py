

class Dinosaur:

    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = int(attack_power)
        self.health = int(health)
    
    def attack_robot(self, robot):
        robot.health = robot.health - self.attack_power
        print(f"{robot.name}'s remaining health is {robot.health}")
        if robot.health <= 0:
            print(f"{robot.name} has died!")
        pass