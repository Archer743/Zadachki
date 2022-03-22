import os
from termcolor import colored

from classes import *


os.system("color")

sender = input(colored("Enter your username:\n", "magenta"))
password = input(colored("Enter your password:\n", "magenta"))

user = User(sender, password)
if not user.is_registered():
    user.save_user()

# mail = Mail(user, )
