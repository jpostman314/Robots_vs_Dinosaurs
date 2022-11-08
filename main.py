from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon



bite = Weapon("Bite", 12)
laser = Weapon("Laser", 10)
murphy = Robot("Murphy", 100, laser)
linda = Dinosaur("Linda", 100, bite)

print(murphy.attack(linda))


