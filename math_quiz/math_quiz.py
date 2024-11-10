import random

def get_random_integer(min, max):
    """
    Returns a random integer in between bounds.

    Args:
        min (int): The minimum value of the random integer.
        max (int): The maximum value of the random integer.
    
    Returns:
        int: A random integer between the bounds.
    """
    return random.randint(min, max)


def get_random_operator():
    """
    Returns a random operator from the list ['+', '-', '*'].

    Returns:
        str: A string that reflects a operator from the list ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])


def build_expression(number1, number2, operator):
    """
    Builds a math expression from two numbers and an operator. Calculates the result of the expression.

    Args:
        number1 (int): The first number of the expression.
        number2 (int): The second number of the expression.
        operator (str): The operator of the expression.

    Returns:
        tuple: A tuple containing the expression as a string and the result of the expression as an integer.
    """
    # print the expression
    expression = f"{number1} {operator} {number2}"
    # calculate the result based on the operator
    if operator == '+': 
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else: 
        result = number1 * number2
    return expression, result

def math_quiz():
    """
    Runs a math quiz game. The player is presented with 3 math problems and needs to provide the correct answers.
    """
    score = 0
    number_of_rounds = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # play 3 rounds
    for _ in range(number_of_rounds):
        # generate random numbers and operator
        number1 = get_random_integer(1, 10) 
        number2 = get_random_integer(1, 6)
        operator = get_random_operator()

        # build the expression and get the result
        current_problem, current_answer = build_expression(number1, number2, operator)
        print(f"\nQuestion: {current_problem}")

        # query the user for an answer
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except:
            # if the user input is not a number, stop the game
            print("Invalid input. Please enter a number.")
            break

        if useranswer == current_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {current_answer}.")

    print(f"\nGame over! Your score is: {score}/{number_of_rounds}")

if __name__ == "__main__":
    math_quiz()
