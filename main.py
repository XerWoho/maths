from modes.typing import TypingGame
from modes.choosing import ChoosingGame
from modes.utils.streak_score import streak
from lib.main_menu import chooser_menu
from lib.exiting import exit
from lib.get_user_history import get_user_history

import os
import json
import uuid

class main:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        self.welcomed = False
        self.game_started = False

        self.username = None
        self.unique_id =  uuid.uuid4().hex
        self.longest_streak = 0
        self.history = []

        main.collect_user_info(self)

    def collect_user_info(self):
        self.username = input("Enter in your username:\n")
        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            with open('users.json', 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError as e:
                    data = {}
        except FileNotFoundError:
            data = {}

        new_user = {
            'username': self.username, 
            'uuid': self.unique_id,
            'longest_streak': self.longest_streak,
            'history': [],
        }

        try:
            data["users"].append(new_user)
        except:
            data["users"] = []
            data["users"].append(new_user)

        with open('users.json', 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Alright {self.username}")
        main.start(self)

    def start(self):
        while True:
            mode = chooser_menu(self.welcomed, self.game_started).handle_movement()
            self.welcomed = True
            self.game_started = True

            if mode == "Typing":
                TypingGame(self.unique_id)
                self.game_started = False
            elif mode == "Choosing":
                ChoosingGame(self.unique_id)
                self.game_started = False
            elif mode == "History":
                get_user_history(self.unique_id)
                self.game_started = False
            else:
                print(f'\nLast Streak: ', end="")
                streak.print_streak()

                print('Quiting...')
                exit()

main().__init__()