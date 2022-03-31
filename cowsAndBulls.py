from random import randint
from math import floor
from termcolor import colored
from os import system

system("color")

def numToList(number : int):
    l = []
    while number:
        l.append(number % 10)
        number = floor(number/10)
    l.reverse()
    return l

def game(number : int):
    guesses = 1
    digitList = numToList(number)
    
    while True:
        iNum = int(ans if (ans := input("Enter a number: ")) != "s" else -1)

        if iNum == -1: 
            print(colored(text=f"Answer: {number}", color="green"))
            break
        elif iNum < 1000 or iNum > 9999: break
        
        iNumDigitList = numToList(iNum)
        indexFound = []
        
        cows, bulls = 0, 0
        for index in range(len(iNumDigitList)):
            if iNumDigitList[index] == digitList[index]: 
                cows += 1
                indexFound.append(index)
            else:
                for i in range(index, len(iNumDigitList)):
                    if iNumDigitList[i] == digitList[i] and not (i in indexFound):
                        bulls += 1
                        indexFound.append(index)
                        break
        
        if cows == 4:
            print(colored(text="Correct! You guessed the number!", color="green"))
            print(colored(text=f"Guesses: {guesses}", color="yellow"))
            break
        else:
            print(colored(text=f"Cows: {cows}   Bulls: {bulls}", color="yellow"))
            guesses += 1


if __name__ == "__main__":
    game(randint(1000, 9999))