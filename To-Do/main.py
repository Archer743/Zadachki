import json
import datetime
import os
from termcolor import colored


os.system('color')


# Data functions
def get_data():
    with open("data.json", "r") as file:
        return json.load(file)

def update_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def remove_todo(author, name:str):
    try:
        data = get_data()
        del data[author][name]
        data[author]["count"] -= 1
        update_data(data)
        return True
    except:
        return False

def add_user(user:str):
    data = get_data()
    if user not in data.keys():
        data[user] = {}
        data[user]["count"] = 0
        update_data(data)

def help(command="all"):
    output = ""
    command = command.lower()

    if command == "all":
        output += "{}: {}\n".format(colored("at", "green"), colored("Creates and saves one new todo", "red"))
        output += "{}: {}\n".format(colored("rt", "green"), colored("Deletes a todo by it's name", "red"))
        output += "{}: {}\n".format(colored("ra", "green"), colored('Frees your inbox', "red"))
        output += "{}: {}\n".format(colored("v", "green"), colored("Shows a todo", "red"))
        output += "{}: {}\n".format(colored("va", "green"), colored("Shows your todos", "red"))
        output += "{}: {}\n".format(colored("q", "green"), colored('Closes this "app"', "red"))
        output += "{}: {}\n".format(colored("h", "green"), colored('Shows this help message', "red"))

    else:
        if command == "at":
            output = "{}: {}\n".format(colored("at", "green"), colored("Creates and saves one new todo", "red"))
        elif command == "rt":
            output = "{}: {}\n".format(colored("rt", "green"), colored("Deletes a todo by it's name", "red"))
        elif command == "ra":
            output = "{}: {}\n".format(colored("ra", "green"), colored("Frees your inbox!", "red"))
        elif command == "v":
            output = "{}: {}\n".format(colored("v", "green"), colored("Shows a todo", "red"))
        elif command == "va":
            output = "{}: {}\n".format(colored("va", "green"), colored("Shows your todos", "red"))
        elif command == "q":
            output = "{}: {}\n".format(colored("q", "green"), colored('Closes this "app"', "red"))
        elif command == "h":
            output = "{}: {}\n".format(colored("h", "green"), colored('Shows this help message', "red"))

    print(output)


class ToDo:
    def __init__(self, name=None, author=None, day_assigned=None, text=None):
        self.name = name
        self.author = author
        self.day_assigned = day_assigned
        self.text = text

    def push_to_json(self):
        data = get_data()
        if self.name not in data[self.author].keys():
            data[self.author]["count"] += 1
            data[self.author][self.name] = {
                "day_assigned": self.day_assigned,
                "text": self.text
            }
            update_data(data)
            return True
        
        return False
    
    def get_from_json(self, author, name):
        data = get_data()
        try:
            self.author = author
            self.name = name
            self.day_assigned = data[author][name]["day_assigned"]
            self.text = data[author][name]["text"]
            return True
        except:
            print("Todo not found!")
            return False

    def print_todo(self):
        output = f"""
        ________________________{colored("ToDo", "yellow")}_______________________
        |{colored("Author", "green")}: {colored(self.author, "red")}
        |{colored("Name", "green")}: {colored(self.name, "red")}
        |{colored("Day Assigned", "green")}: {colored(self.day_assigned, "red")}
        |{colored("Task", "green")}: {colored(self.text, "red", "on_grey")}
        |__________________________________________________
        """
        print(output)


# Main
exit = False
print(colored("Welcome to ToDo!", "magenta"))
author = input(colored("Please enter your username:\n", "magenta"))
add_user(author)

while not exit:
    option = input(colored("Select option: [at], [rt], [ra], [v], [va], [q], [h]\n", "magenta")).lower()
    
    if option == "h":
        help(command=input(colored('Enter the unknown command (for all commands -> enter "all"):\n', "yellow")))
    
    elif option == "at":
        name = input(colored("Enter todo's name:\n", "yellow")) 
        text = input(colored("Enter the assignment:\n", "yellow"))
        day_assigned = datetime.datetime.now().strftime("%a, %#d %B %Y, %I:%M %p, UTC")

        todo = ToDo(name, author, day_assigned, text)
        saved = todo.push_to_json()
        if saved:
            print(colored("Todo added successfully!", "yellow"))
        else:
            print(colored("Todo was NOT added!", "red"))

    elif option == "rt":
        name = input(colored("Enter todo's name:\n", "yellow"))
        if not remove_todo(author, name):
            while True:
                name = input(colored("Enter a valid name:\n", "red"))
                if remove_todo(author, name):
                    print(colored("Todo was deleted successfully!", "yellow"))
                    break
                elif name == "q":
                    print(colored("Bye, bye!", "magenta"))
                    exit = True
                    break
                elif name == "back":
                    break

            continue

        print(colored("Todo was deleted successfully!", "yellow"))
    
    elif option == "ra":
        data = get_data()
        count = data[author]["count"]
        if count == 0:
            print(colored("You don't have any todos!", "red"))
        else:
            data[author] = {}
            data[author]["count"] = 0
            update_data(data)

            print(colored("Inbox freed!", "yellow"))

    elif option == "v":
        name = input(colored("Enter todo's name:\n", "yellow"))
        data = get_data()
        todo = ToDo()
        found = todo.get_from_json(author, name)
        if found:
            todo.print_todo()
    
    elif option == "va":
        data = get_data()
        count = data[author]["count"]
        print(colored("Todos:", "yellow"), colored("{}".format(count), "red"))
        if count == 0:
            print(colored("You don't have any todos!", "red"))
        else:
            todo = ToDo()
            for todo_name in data[author]:
                if todo_name == "count":
                    continue

                todo.get_from_json(author, todo_name)
                todo.print_todo()

    elif option == "q":
        print(colored("Bye, bye!", "magenta"))
        exit = True