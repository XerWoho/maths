import random

from lib.number_class import get_custom_number_annotation, return_custom_string_non_negative
from lib.modify_formula import modify_formula


class generate_list_answers:
    def __init__(self, formula):
        modified = modify_formula(formula)
        numbers = modified.numbers

        self.formula = formula

        self.a = numbers[0]
        self.d = numbers[1]
        self.e = numbers[2]
        
        self.list = []

        self.wrong_answers = []
        for _ in range(0, 3):
            generate_list_answers.generate(self)

        self.right_answers = [modified.get_right_answer()]

        self.list = self.wrong_answers + self.right_answers
        self.list = random.sample(self.list, len(self.list))
    

    def generate(self):
        decider = random.randint(0, 1)
        step = None

        if decider == 0:
            step = f'{self.a}x^2 {get_custom_number_annotation(self.a * 2 * (self.d * -1))} {return_custom_string_non_negative(self.a * 2 * (self.d * -1) - random.randint(-3,3))}x {get_custom_number_annotation(self.a * 2 * self.d.__pow__(2))} {return_custom_string_non_negative((self.a * self.d.__pow__(2)) + self.e - random.randint(-3,3))}'
            
            while step.replace(" ", "") == modify_formula(self.formula).get_right_answer():
                step = f'{self.a}x^2 {get_custom_number_annotation(self.a * 2 * (self.d * -1))} {return_custom_string_non_negative(self.a * 2 * (self.d * -1) - random.randint(-3,3))}x {get_custom_number_annotation(self.a * 2 * self.d.__pow__(2))} {return_custom_string_non_negative((self.a * self.d.__pow__(2)) + self.e - random.randint(-3,3))}'
        else:
            step = f'{self.a}x^2 {generate_list_answers.wrong_annotation(self, self.a * 2 * (self.d * -1))} {return_custom_string_non_negative(self.a * 2 * (self.d * -1) - random.randint(-3,3))}x {generate_list_answers.wrong_annotation(self, self.a * 2 * self.d.__pow__(2))} {return_custom_string_non_negative((self.a * self.d.__pow__(2)) + self.e  - random.randint(-3,3))}'

            while step.replace(" ", "") == modify_formula(self.formula).get_right_answer():
                step = f'{self.a}x^2 {get_custom_number_annotation(self.a * 2 * (self.d * -1))} {return_custom_string_non_negative(self.a * 2 * (self.d * -1) - random.randint(-3,3))}x {get_custom_number_annotation(self.a * 2 * self.d.__pow__(2))} {return_custom_string_non_negative((self.a * self.d.__pow__(2)) + self.e - random.randint(-3,3))}'

        self.wrong_answers.append(step)


    def wrong_annotation(self, number):
        return "+" if number < 0 else "-"
