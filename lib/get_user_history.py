from colorama import Fore, Style
import json
import os

def get_user_history(uuid):
    with open('users.json', 'r') as file:
        existing_data = json.load(file)

    os.system('cls' if os.name == 'nt' else 'clear')

    for user in existing_data["users"]:
        if user["uuid"] == uuid:
            if len(user["history"]) == 0:
                print("Nothing here yet.")

            for history in user["history"]:
                print(f'''
                {Fore.RED +'INCORRECT' + Style.RESET_ALL if history["answer_was"] == "wrong" else Fore.GREEN +  "CORRECT" + Style.RESET_ALL}
                Gamemode: {history["game_mode"]},
                Answer: {history["answer"]},
                Solution: {history["solution"]}
                TimeToAnswer: {history["TTA"]}s
                ''')
    