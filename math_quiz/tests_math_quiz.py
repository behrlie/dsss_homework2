import unittest
from math_quiz import get_random_integer, get_random_operator, build_expression


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Test if random operator generated is one of the specified operators
        for _ in range(50):
            operator = get_random_operator()
            self.assertTrue(operator in ['+', '-', '*'])


    def test_build_expression(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 2, '-', '3 - 2', 1),
                (7, 3, '*', '7 * 3', 21),
                (3, -2, '-', '3 - -2', 5),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = build_expression(num1, num2, operator)
                self.assertTrue(problem == expected_problem and answer == expected_answer)

if __name__ == "__main__":
    unittest.main()
