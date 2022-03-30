from os import system
from termcolor import colored

from classes import *

system("color")


if __name__ == "__main__":
    sender = input(colored("Enter your username:\n", "magenta"))
    password = input(colored("Enter your password:\n", "magenta"))

    user = User(sender, password)
    
    if not user.login():
        print(colored(text="Error! Check your username or password!", color="red"))
    else:
        print(colored(text="Your login is successful!", color="green"))
        
        while True:
            mode = input("Enter mode: S/B (Send/Bye): ")
            
            if mode.lower() == "s":
                receiver = input(colored(text="Receiver: ", color="red"))
                message = input(colored(text="Mail:\n", color="red"))
                mail = Mail(user, receiver, message)
                
                if mail.send():
                    print(colored(text="Mail sent successfully!", color="green"))
                else: print(colored(text="Error! Mail was not sent!", color="red"))
            
            elif mode.lower() == "b":
                print(colored(text="Bye, bye!", color="blue"))
                break