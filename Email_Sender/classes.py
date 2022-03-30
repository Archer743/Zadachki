from get_data import *
from edit_data import update_data
import datetime


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.s_id = None
        self.r_id = None

    def is_registered(self):
        if get_user(self.username):
            return True

        return False
    
    def login(self):
        if self.is_registered():
            user_saved = get_user(self.username)
            if user_saved["password"] == self.password:
                self.s_id = get_last_id(self.username, True)
                self.r_id = get_last_id(self.username, False)
                return True
            return False
        else: 
            self.save_user()
            self.s_id = get_last_id(self.username, True)
            self.r_id = get_last_id(self.username, False)
            return True


    def save_user(self):
        data = get_data()
        try:
            data[self.username] = {
                "password": self.password,
                "s_id" : 0,
                "r_id" : 0,
                "sent_mails": [],
                "received_mails" : []
            }
            update_data(data)
            return True
        except:
            return False
    
    def delete_user(self):
        data = get_data()
        if self.login():
            try:
                del data[self.username]
                update_data(data)
                return True
            except:
                return False
        
        return False


class Mail:
    def __init__(self, sender:User, receiver:str, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.day_assigned = datetime.datetime.now().strftime("%a, %#d %B %Y, %I:%M %p, UTC")

    def send(self):
        data = get_data()
        try:
            self.sender.s_id += 1
            data[self.sender.username]["s_id"] = self.sender.s_id

            data[self.receiver]["r_id"] += 1
            
            data[self.receiver]["received_mails"].append({"id" : data[self.receiver]["r_id"], "sender" : self.sender.username, "message" : self.message, "date" : self.day_assigned})
            data[self.sender.username]["sent_mails"].append({"id" : self.sender.s_id, "receiver" : self.receiver, "message" : self.message, "date" : self.day_assigned})
            
            update_data(data)
            return True
        except:
            return False