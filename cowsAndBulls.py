from random import randint
from termcolor import colored
from os import system

system("color")


def numToList(number : int):
    return [int(element) for element in list(str(number))]

def checkNums(c_num, u_num):  # computer number, user number
    cDigitList = numToList(c_num)
    uDigitList = numToList(u_num)
    cows, bulls = 0, 0

    for index in range(len(uDigitList)):
        if uDigitList[index] == cDigitList[index]: cows += 1
        else: bulls += 1
    
    return [cows, bulls]

def game(c_num : int):
    print(colored(text="Let's play a game of Cowbull!", color="magenta"))
    guesses = 1
    
    while True:
        u_num = int(ans if (ans := input("Enter a number: ")) != "stop" else -1)

        if u_num == -1: 
            print(colored(text=f"Answer: {c_num}", color="green"))
            break
        elif u_num < 1000 or u_num > 9999: break
        
        cows, bulls = checkNums(c_num, u_num)

        if cows == 4:
            print(colored(text=f"Correct! You guessed the number! Number: {c_num}", color="green"))
            print(colored(text=f"Guesses: {guesses}", color="yellow"))
            break
        else:
            print(colored(text=f"Cows: {cows}   Bulls: {bulls}", color="yellow"))
            guesses += 1


if __name__ == "__main__":
    game(randint(1000, 9999))