import json

def update_user_history(uuid, data):
    with open('users.json', 'r') as file:
        existing_data = json.load(file)

    for user in existing_data["users"]:
        if user["uuid"] == uuid:
            user["history"].append(data)

    with open('users.json', 'w') as file:
        json.dump(existing_data, file, indent=4)