from modes.typing import TypingGame
from modes.choosing import ChoosingGame
from modes.utils.streak_score import streak
from lib.main_menu import chooser_menu
from lib.exiting import exit
from lib.get_user_history import get_user_history
from lib.login_register import login_register

import os
import json
import sys

class main:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        self.welcomed = False
        self.game_started = False

        self.unique_id = None
        self.longest_streak = 0
        self.history = []

        main.collect_user_info(self)
        return

    def collect_user_info(self):
        while self.unique_id is None:
            user = login_register()

            if user.uuid != None:
                self.unique_id = user.uuid  
            else:
                user = login_register()


        os.system('cls' if os.name == 'nt' else 'clear')
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