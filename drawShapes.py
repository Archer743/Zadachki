from termcolor import colored
from os import system
from math import ceil, floor

system("color")


def drawRectangle(height : int, width : int, color : str = None, material : str = "*"):
    for y in range(height):
        side = ""
        for x in range(width):
            side += material
        print(colored(text=side, color=color))

# not exactly a circle
def drawCircle(radius : int, color : str = None, material : str = "*"):
    for y in range(0, floor(radius / 2)):
        line = ""
        for x in range(0, radius + 1):
            if x >= floor(radius / 2) - (y+1) and x <= ceil(radius / 2) + (y+1): line += material
            else: line += " "
        print(colored(text=line, color=color))

    line = ""
    for i in range(radius+1): line += material
    print(colored(text=line, color=color))

    rev = reversed(range(0, ceil(radius / 2)))

    for z in rev:
        line = ""
        for x in range(radius + 1):
            if x >= floor(radius / 2) - (z+1) and x <= ceil(radius / 2) + (z+1): line += material
            else: line += " "
        print(colored(text=line, color=color))


if __name__ == "__main__":
    shape = input("Choose shape: S, C\n")

    if shape.lower() == "s":
        height = int(input("Enter height: "))
        width = int(input("Enter width: "))
        color = input("Enter color: ")
        material = input("Enter material: ")
        drawRectangle(height, width, color, material)
        
    elif shape.lower() == "c":
        radius = int(input("Enter radius: "))
        color = input("Enter color: ")
        material = input("Enter material: ")
        drawCircle(radius, color, material)