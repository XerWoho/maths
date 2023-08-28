from lib.modify_formula import modify_formula
from lib.number_class import number_class
from lib.generate_list_answers import generate_list_answers
from modes.utils.streak_score import streak
from lib.chooser_menu import chooser_menu


from colorama import Fore, Style, init
init()

import time
import os
import sys
from lib.update_user_streak import update_user_streak
from lib.update_user_history import update_user_history

class ChoosingGame:
    def __init__(self, uuid):
        self.uuid = uuid
        os.system('cls' if os.name == 'nt' else 'clear')

        a = number_class(None, True)
        d = number_class(None, True)
        e = number_class(None, True)
        formula = f'{a.number}(x - ({d.number}))^2 {e.get_number_annotation()} {e.return_string_non_negative()}'

        self.start_time = time.time()
        self.formula = formula
        self.formula_less_v = modify_formula(self.formula).steps[0]

        self.right_answer = modify_formula(formula).get_right_answer().replace(" ", "")
        self.list = []

        generated = generate_list_answers(formula)
        self.list = generated.list

        self.user_answer = None

        print('Whats this vertex form when changed in to the standard form?')
        print(self.formula_less_v if len(sys.argv) < 2 else self.formula, end="\n\n")

        ChoosingGame.present_possible_answers(self)
    

    def present_possible_answers(self):
        print('Answers:')
        for i, item in enumerate(self.list):
            print(f'{i + 1} {item}')
        print()
        ChoosingGame.get_answer(self)
    

    def get_answer(self):
        answer = chooser_menu(self.list, self.formula).handle_movement()
        self.user_answer = answer

        ChoosingGame.check_answer(self)
    
    def check_answer(self):
        end_time = time.time()
        if self.user_answer.replace(" ", "") == self.right_answer:
            os.system('cls' if os.name == 'nt' else 'clear')

            update_user_history(self.uuid, {
                'game_mode': 'Choosing',
                'answer_was': 'right',
                'answer': self.user_answer,
                'solution': self.right_answer,
                'TTA': round(end_time - self.start_time, 2)
            })

            streak.inc_point()
            print(Fore.GREEN + f'Youre right! Took you {round(end_time - self.start_time, 2)}s' + Style.RESET_ALL)

            print(f'Formula: {self.formula_less_v if len(sys.argv) < 2 else self.formula}')
            print('Steps:')

            steps = modify_formula(self.formula).steps
            if len(sys.argv) < 2:
                steps = steps[1:]

            for step in steps:
                print(step)


            update_user_streak(self.uuid, streak.streak)
            print(f"\nCurrent streak: ", end="")
            streak.print_streak()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

            update_user_history(self.uuid, {
                'game_mode': 'Choosing',
                'answer_was': 'wrong',
                'answer': self.user_answer,
                'solution': self.right_answer,
                'TTA': round(end_time - self.start_time, 2)
            })

            print(Fore.RED + f'Wrong! Took you {round(end_time - self.start_time, 2)}s' + Style.RESET_ALL)

            print(f'Formula: {self.formula_less_v if len(sys.argv) < 2 else self.formula}')
            print('Steps:')

            steps = modify_formula(self.formula).steps
            if len(sys.argv) < 2:
                steps = steps[1:]
            
            for step in steps:
                print(step)
            
            print(Fore.RED + f'\n(Your answer: {self.user_answer})\n' + Style.RESET_ALL)
            print(f"Streak before loss: ", end="")

            streak.print_streak()
            streak.reset_point()
