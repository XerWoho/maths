from lib.modify_formula import modify_formula
from lib.number_class import number_class
from modes.utils.streak_score import streak
from lib.exiting import exit
from colorama import Fore, Style, init
init()

import time
import os
from lib.update_user_streak import update_user_streak
from lib.update_user_history import update_user_history

class TypingGame:
    def __init__(self, uuid):
        self.uuid = uuid
        os.system('cls' if os.name == 'nt' else 'clear')

        a = number_class(None, True)
        d = number_class(None, True)
        e = number_class(None, True)
        formula = f'{a.number}(x - ({d.number}))^2 {e.get_number_annotation()} {e.return_string_non_negative()}'

        self.start_time = time.time()
        self.formula = formula
        self.right_answer = modify_formula(formula).get_right_answer().replace(" ", "")
        self.right_answer_modified = self.right_answer.replace("-0", "+0")


        print('Whats this vertex form when changed in to the standard form ?')
        print(self.formula, end="\n\n")

        try:
            answer = input("Enter!\n\n").replace(" ", "")
            TypingGame.check_answer(self, answer)
        except:
            print(f'\nLast Streak: ', end="")
            streak.print_streak()

            print('Quiting...')
            exit()

    def check_answer(self, answer):
        end_time = time.time()

        if self.right_answer_modified == answer.replace("-0", "+0"):
            os.system('cls' if os.name == 'nt' else 'clear')

            update_user_history(self.uuid, {
                'game_mode': 'Typing',
                'answer_was': 'right',
                'answer': answer,
                'solution': self.right_answer,
                'TTA': round(end_time - self.start_time, 2)
            })


            streak.inc_point()
            print(Fore.GREEN + 'Youre right!' + Style.RESET_ALL)
            if self.right_answer != answer:
                print(Fore.LIGHTGREEN_EX + "Tho you could've been more accurate.\n" + Style.RESET_ALL)
            
            if end_time - self.start_time > 35:
                print(Fore.LIGHTRED_EX + f'Took you {round(end_time - self.start_time, 2)}s' + Style.RESET_ALL)
            else:
                print(Fore.LIGHTGREEN_EX + f'Took you {round(end_time - self.start_time, 2)}s' + Style.RESET_ALL)

        

            print(f'Formula: {self.formula}')
            print('Steps:')
            steps = modify_formula(self.formula).steps
            for step in steps:
                print(step)

            update_user_streak(self.uuid, streak.streak)
            print(f"\nCurrent streak: ", end="")
            streak.print_streak()
            return True
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')

            update_user_history(self.uuid, {
                'game_mode': 'Typing',
                'answer_was': 'wrong',
                'answer': answer,
                'solution': self.right_answer,
                'TTA': round(end_time - self.start_time, 2)
            })

            print(Fore.RED + f'Wrong! Took you {round(end_time - self.start_time, 2)}s' + Style.RESET_ALL)

            print(f'Formula: {self.formula}')
            print('Steps:')
            steps = modify_formula(self.formula).steps
            for step in steps:
                print(step)

            print(Fore.RED + f'\n(Your answer: {answer})' + Style.RESET_ALL)
            print(f"\nStreak before loss: ", end="")
            streak.print_streak()
            streak.reset_point()
            return False