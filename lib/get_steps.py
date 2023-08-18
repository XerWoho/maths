from lib.number_class import get_custom_number_annotation, return_custom_string_non_negative

class get_all_steps:
    def __init__(self, numbers):
        self.numbers = numbers

        self.a = numbers[0]
        self.d = numbers[1]
        self.e = numbers[2]

        self.steps = []

        get_all_steps.get_first_step(self)
    
    def get_first_step(self):
        step = f'{self.a}(x {get_custom_number_annotation(self.d * -1)} {return_custom_string_non_negative(self.d)})^2 {get_custom_number_annotation(self.e)} {return_custom_string_non_negative(self.e)}'

        self.steps.append(step)
        get_all_steps.get_second_step(self)
    

    def get_second_step(self):
        step = f'{self.a}(x^2 {get_custom_number_annotation(2 * self.d * -1)} {return_custom_string_non_negative(2 * self.d)}x + {self.d.__pow__(2)}) {get_custom_number_annotation(self.e)} {return_custom_string_non_negative(self.e)}'

        self.steps.append(step)
        get_all_steps.get_third_step(self)

    

    def get_third_step(self):
        step = f'{self.a}x^2 {get_custom_number_annotation(self.a * 2 * (self.d * -1))} {return_custom_string_non_negative(self.a * 2 * self.d * -1)}x {get_custom_number_annotation(self.a * 2 * self.d.__pow__(2))} {return_custom_string_non_negative(self.a * self.d.__pow__(2))} {get_custom_number_annotation(self.e)} {return_custom_string_non_negative(self.e)}'

        self.steps.append(step)
        get_all_steps.get_final_step(self)

    def get_final_step(self):
        step = f'{self.a}x^2 {get_custom_number_annotation(self.a * 2 * (self.d * -1))} {return_custom_string_non_negative(self.a * 2 * (self.d * -1))}x {get_custom_number_annotation(self.a * self.d.__pow__(2) + self.e)} {return_custom_string_non_negative((self.a * self.d.__pow__(2)) + self.e)}'

        self.steps.append(step)
        return self.steps

    def get_right_answer(self):
        return self.steps[-1]