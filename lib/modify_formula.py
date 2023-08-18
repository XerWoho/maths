from lib.get_steps import get_all_steps

import re
formula_pattern = r'[-+]?\b\d+\b'

class modify_formula:
    def __init__(self, quadratic_formula):
        self.formula = quadratic_formula
        self.numbers = []
        self.steps = []

        modify_formula.get_numbers(self)
        self.steps = get_all_steps(self.numbers).steps


    def get_numbers(self):
        modify_formula.rework_quadratic_formula(self)
        self.numbers = [int(x) for x in re.findall(r'[-+]?\b\d+\b', self.formula)]

    
    def rework_quadratic_formula(self):
        self.formula = self.formula.replace(" ", "").replace("x", " ").replace("^", "x")

        
    def get_right_answer(self):
        return get_all_steps(self.numbers).get_right_answer()
