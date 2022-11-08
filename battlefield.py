from robot import Robot
from dinosaur import Dinosaur





class Battlefield:

    def __init__(self):
        self.robot = Robot("Murphy", 100, "Laser")
        self.dinosaur = Dinosaur("Linda", 25, 100)
        


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
        pass

    
    def display_welcome(self):
        print("Welcome to a battle like you've never seen berfore. Robot vs. Dinosuar!!!!")
        
    
    def battle_phase(self):
        turn_counter = 0
        
        while self.robot.health >0 and self.dinosaur.health >0:
            if (turn_counter % 2) == 0:
                print("")
                print(f"{self.robot.name} attacked {self.dinosaur.name}!")
                print("")
                self.robot.attack(self.dinosaur)
                turn_counter += 1
            else:
                print("")
                print(f"{self.dinosaur.name} attacked {self.robot.name}!")
                print("")
                self.dinosaur.attack_robot(self.robot)
                turn_counter += 1
                

    def display_winner(self):
        if self.robot.health > 0:
            print("")
            print(f"{self.robot.name} is the winner!")
            print("")
        elif self.dinosaur.health > 0:
            print("")
            print(f"{self.dinosaur.name} is the winner!")
            print("")


