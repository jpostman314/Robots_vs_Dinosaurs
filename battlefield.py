from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon




class Battlefield:

    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
        pass

    
    def display_welcome(self):
        print("Welcome to a battle like you've never seen berfore. Robot vs. Dinosuar!!!!")
        pass
    
    def battle_phase(self):
        pass

    def display_winner(self):
        pass
