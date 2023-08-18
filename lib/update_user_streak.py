import json

def update_user_streak(uuid, streak):
    with open('users.json', 'r') as file:
        existing_data = json.load(file)

    for user in existing_data["users"]:
        if user["uuid"] == uuid:
            if user["longest_streak"] < streak:
                user["longest_streak"] = streak

    with open('users.json', 'w') as file:
        json.dump(existing_data, file, indent=4)