import random

class number_class:
    def __init__(self, number, random_number = False):
        if random_number:
            self.number = random.randint(-3, 3)
            while self.number == 0:
                self.number = random.randint(-3, 3)
        else:
            self.number = number
        
        self.is_negative = None

        number_class.check_negative(self)
    
    def check_negative(self):
        self.is_negative = self.number < 0
        return self.is_negative
    

    def multiply_negative(self):
        return self.number * (-1)
    
    
    def get_number_annotation(self):
        return "-" if self.is_negative else "+"
    
    def return_string(self):
        return self.number.__str__()


    def return_string_non_negative(self):
        return self.number.__str__().replace("-", "")
    


def get_custom_number_annotation(number):
    return "-" if number < 0 else "+"

def return_custom_string_non_negative(number):
    return number.__str__().replace("-", "")