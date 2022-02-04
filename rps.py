# rps -> rock paper scissors
import random
import os
from sys import exit
from termcolor import colored

os.system("color")

rock = """
_______________
| | |        (=======)
| | |        (=========)
| | |     (============)
| | |       (==========)
| | |________(====)
"""

paper = """
_____________
| | |        )=========)
| | |        )===========)
| | |        )=============)
| | |        )============)
| | |________)=======)
"""

scissors = """
_____________
| | |        (=======)
| | |        )===========)
| | |        )=============)
| | |        (=======)
| | |________(=======)
"""

vs = """             
    \ \       / / ______
     \ \     / / ||
      \ \   / /  \\\___
       \ \_/ /        \\\
        \___/    _____||  []
"""

options = [rock, paper, scissors]

user = int(input(colored("Choose a rock[1], paper[2] or scissors[3]\n", "magenta"))) - 1
computer = random.randint(0, 2)
print(user, computer)

if user not in [0, 1, 2]:
    print(colored("Invalid number!", "red"))
    exit()

print(vs)