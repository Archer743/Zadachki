from os import system
from time import sleep
from random import randint
from termcolor import colored

system("color")

def draw_progress_bar(progress, total, color="yellow", done="green"):
    if progress != total:
        persent = 100 * (progress / float(total)) 
        bar_in = '|' + '█' * int(persent) # alt + 219(from numpad)
        bar_out = '=' * (100 - int(persent)) + '|'
        print("\r{}{} {}".format(colored(text=bar_in, color=color), colored(text=bar_out, color="red"), colored(text=f'{persent:.2f}%', color=color)), end="\r")
    else: print(colored(text=f"\r|{'█' * 100}| {float(100):.2f}%", color=done))

if __name__ == "__main__":
    max = int(input("Enter a number: "))
    for index in range(0, max): draw_progress_bar(index+1, max) ; sleep(randint(0, 10) / float(100))
    print("Done!")