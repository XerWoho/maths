import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.generate_list_answers import generate_list_answers

def modify_result(res):
    return res.replace(" ", "").replace("+0", "-0")


formula_1 = "2(x - (3))^2 + 5"
result_1 = "2x^2 - 12x + 23"
generated_1 = generate_list_answers(formula_1)
def test_run_conversion_1():
    assert modify_result(result_1) == modify_result(generated_1.right_answers[0])


formula_2 = "-1(x - (1))^2 - 9"
result_2 = "-1x^2 + 2x - 10"
generated_2 = generate_list_answers(formula_2)
def test_run_conversion_2():
    assert modify_result(result_2) == modify_result(generated_2.right_answers[0])


formula_3 = "7(x - (3))^2 - 3"
result_3 = "7x^2 - 42x + 60"
generated_3 = generate_list_answers(formula_3)
def test_run_conversion_3():
    assert modify_result(result_3) == modify_result(generated_3.right_answers[0])


formula_4 = "-4(x - (-3))^2 + 36"
result_4 = "-4x^2 - 24x - 0"
generated_4 = generate_list_answers(formula_4)
def test_run_conversion_4():
    assert modify_result(result_4) == modify_result(generated_4.right_answers[0])