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

# if id == True: returns s_id else r_id
def get_last_id(username:str, id:bool):
    if (data := get_data()):
        try:
            return data[username]["{}".format("s_id" if id else "r_id")]
        except:
            return None
    
    return None