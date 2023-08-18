from colorama import Fore, Style
import msvcrt
import os

from lib.exiting import exit
from modes.utils.streak_score import streak

class chooser_menu:
    def __init__(self, options, formula):
        self.options = options
        self.formula = formula
        self.selected = 0

    def display_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print('What is the standard form from this vertex form?')
        print(f'{self.formula}\n')
        for i, option in enumerate(self.options):
            if i == self.selected:
                print(Fore.LIGHTCYAN_EX + "> ", option + Style.RESET_ALL)
            else:
                print("  ", option)

    def handle_movement(self):
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