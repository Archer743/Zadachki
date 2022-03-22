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
       \ \_/ /        \\
        \___/    _____||  []
"""

options = [rock, paper, scissors]
names = ["ROCK", "PAPER", "SCISSORS"]

user = int(input(colored("Choose a rock[1], paper[2] or scissors[3]\n", "magenta"))) - 1
bot = random.randint(0, 2)
status = ""

if user not in [0, 1, 2]:
    print(colored("Invalid number!", "red"))
    exit()
elif (user == 0 and bot == 1) or (user < bot):
    status = colored("You loose!", "red")
elif (user == 1 and bot == 0) or (user > bot):
    status = colored("You win!", "blue")
elif user == bot:
    status = colored("Tied!", "yellow")

output = f"""
    ====================================================
    {colored("You: {}".format(names[user]), "blue")}
    {colored(options[user], "blue")}

    {colored(vs, "yellow")}

    {colored("Bot: {}".format(names[bot]), "red")}
    {colored(options[bot], "red")}

    {colored("STATUS: ", "yellow")} {status}
    ====================================================
"""
print(output)