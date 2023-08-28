import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.generate_list_answers import generate_list_answers

formula = "2(x - (2))^2+5"
generated = generate_list_answers(formula)

def test_generation_function():
    assert generated.right_answers[0] not in generated.wrong_answers