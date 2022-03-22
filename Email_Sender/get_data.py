import json

def get_data():
    with open("data.json", "r") as file:
        return json.load(file)

def get_user(username:str):
    if (data := get_data()):
        try:
            return data[username]
        except:
            return None
    
    return None