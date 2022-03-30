from random import randint
from termcolor import colored
from os import system

system("color")


def game(min : int, max : int):
    if min > max:
        temp = max
        max = min
        min = temp
    
    attempts = 1
    rand_num = randint(min, max)
    _input = int(input("{} Guess a number between {} and {}: ".format(colored(text=">", color="red"), min, max)))

    while True:
        if _input < min or _input > max: _input = int(input("{} Out of range! Try again: ".format(colored(text=">", color="red"))))
        elif _input > rand_num: _input = int(input("{} High! Try again: ".format(colored(text=">", color="red"))))
        elif _input < rand_num: _input = int(input("{} Low! Try again: ".format(colored(text=">", color="red"))))
        else: 
            print("{} {} {} {}".format(colored(text=">", color="red"), colored(text="Well, you guessed the number!", color="magenta"), attempts, "attempts" if attempts > 1 else "attempt"))
            break

        attempts += 1


if __name__ == "__main__":
    min = int(input("{} Enter min value: ".format(colored(text=">", color="red"))))
    max = int(input("{} Enter max value: ".format(colored(text=">", color="red"))))
    game(min, max)