from colorama import Fore, Style
import msvcrt
import sys

from lib.exiting import exit
from modes.utils.streak_score import streak


class chooser_menu:
    def __init__(self, weclomed, game_started):
        self.options = ["Typing", "Choosing", "History", "Exit"]
        self.selected = 0
        self.welcomed = weclomed
        self.game_started = game_started

    def display_menu(self):
        if self.welcomed and self.game_started:
            # Clear latest 3 lines from the Terminal
            sys.stdout.write("\033[{}A".format(4))
            sys.stdout.write("\033[J")

        self.welcomed = True
        self.game_started = True

        for i, option in enumerate(self.options):
            if i == self.selected:
                print(Fore.LIGHTCYAN_EX + "> ", option + Style.RESET_ALL)
            else:
                print("  ", option)

    def handle_movement(self):
        if self.welcomed == False:
            print('Choose a game of your liking!')


        while True:
            chooser_menu.display_menu(self)

            key = msvcrt.getch()

            if key == b'\x03':
                print(f'\nLast Streak: ', end="")
                streak.print_streak()

                print('Quiting...')
                exit()
            
            
            if key == b'H' and self.selected > 0:  # Up arrow key
                self.selected -= 1
            elif key == b'P' and self.selected < len(self.options) - 1:  # Down arrow key
                self.selected += 1
            elif key == b'\r':  # Enter key
                break
            else:
                continue
        
        return self.options[self.selected]
