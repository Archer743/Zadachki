import json
from classes import *

def update_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# def send_mail(sender:User, receiver:User, mail:Mail):
#     pass