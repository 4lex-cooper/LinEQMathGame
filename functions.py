import random


def generate_lineq_question():
    """
    Generate a random linear equation maths question.

    Returns:
    Tuple[string, int]: Linear equation maths question, Correct answer (value of y).
    """
    # generate 2 random numbers.
    num_1 = random.randint(1, 10)
    correct_answer = random.randint(1, 10)
    # generate random operator.
    operators_list = ["+", "-", "*"]
    operator = random.choice(operators_list)
    # generate question.
    calc_string = str(num_1) + operator + str(correct_answer)
    question = f"{num_1} {operator} x = {eval(calc_string)}?"
    # return question and answer.
    return question, correct_answer


def is_correct_answer(user_answer, correct_answer):
    """Check if the users answer is the correct answer.

    Args:
        user_answer (int): Answer inputted by the user.
        correct_answer (int): Correct answer to the question.

    Returns:
        bool: True if the user answer is correct, False otherwise.
    """
    return user_answer == correct_answer


def all_questions_answered(questions_answered, total_questions):
    """Check if the user has answered all the questions.

    Args:
        questions_answered (int): Number of questions answered by the user.
        total_questions (int): The total number of questions to be answered.

    Returns:
        bool: True if all questions have been answered, False otherwise.
    """
    return questions_answered == total_questions


def format_instructions_text():
    """Return instructions text string."""

    return """
    
*****************************************************************************
Welcome to the Linear Equation Maths Game! 

Instructions:
For each question you will be shown a linear equation.
You must answer by typing out the value of the variable ‘y’ and clicking submit.
There will be 10 questions in total.

Good luck, have fun!

*****************************************************************************
"""


def format_final_feedback(score, questions_answered):
    """Return completed game final score feedback.

    Args:
        score (int): The number of questions answered correctly.
        questions_answered (int): The total number of questions answered.

    Returns:
        string: The final game feedback text.

    """

    return f"""
    
*****************************************************************************
You have completed the Linear Equation Maths Game!

Your final score is {score} out of {questions_answered}

*****************************************************************************
"""
