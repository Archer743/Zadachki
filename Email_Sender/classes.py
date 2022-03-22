from get_data import *
from edit_data import update_data
import datetime


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_registered(self):
        if get_user(self.username):
            return True

        return False

    def save_user(self):
        data = get_data()
        try:
            data[self.username] = {
                "password": self.password,
                "sended_mails": [],
                "received_mails" : []
            }
            update_data(data)
            return True
        except:
            return False

    def receive_mail(self, mail, sender):
        data = get_data()
        data[self.username]["received_mails"].append(mail)
        data[sender.username]["sended_mails"].append(mail)
        update_data(data)


class Mail:
    def __init__(self, sender:User, receiver:User, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.day_assigned = datetime.datetime.now().strftime("%a, %#d %B %Y, %I:%M %p, UTC")

    def send(self, user:User):
        user.receive_mail({"sender" : self.sender, "message" : self.message, "date" : self.day_assigned}, self.sender)
