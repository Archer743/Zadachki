import json
import datetime


def get_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except:
        return None

def update_data(data):
    try:
        with open('data.json', 'w') as file:
            return json.dump(data, file, indent=4)
    except:
        return None

def remove_todo(name:str):
    try:
        data = get_data()
        del data[name]
        update_data(data)
        return True
    except:
        return False


class ToDo:
    def __init__(self, name=None, author=None, day_assigned=None, text=None):
        self.name = name
        self.author = author
        self.day_assigned = day_assigned
        self.text = text

    def push_to_json(self):
        data = get_data()
        data[self.name] = {
            "author": self.author,
            "day_assigned": self.day_assigned,
            "text": self.text
        }
        update_data(data)
    
    def get_from_json(self, name):
        data = get_data()
        try:
            self.author = data[name]["author"]
            self.name = name
            self.day_assigned = data[name]["day_assigned"]
            self.text = data[name]["text"]
        except:
            pass


# Main
exit = False
print("Welcome to To-Do!")
author = input("Please enter your username:\n")

while not exit:
    option = input("Please enter what do you want to do now from these options? [add_todo], [remove_todo], [quit]")

    if option.lower() == "add_todo":
        name = input("Enter name:\n") 
        day_assigned = datetime.datetime.now().strftime("%a, %#d %B %Y, %I:%M %p, UTC")
        text = input("Enter the assignment:\n")

        ToDo(name, author, day_assigned, text)
        ToDo.push_to_json()
        print("Todo added successfully!")

    elif option.lower() == "remove_todo":
        name = input("Enter name:\n")
        if not remove_todo(name):
            while True:
                name = input("Enter a valid name:\n")
                if remove_todo:
                    break
                elif name == "quit":
                    exit = True

    elif option.lower() == "quit":
        print("Bye, bye!")
        exit = True