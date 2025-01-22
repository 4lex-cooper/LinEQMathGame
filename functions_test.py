from functions import generate_lineq_question, is_correct_answer, all_questions_answered


def test_generate_lineq_question():
    """Test that test_generate_lineq_question returns valid results."""
    question, correct_answer = generate_lineq_question()
    # Ensure the answer is between 1 and 10 inclusive
    assert 1 <= correct_answer <= 10
    # Ensure the answer is an integer value
    assert type(correct_answer) == "int"
    # Ensure the question length is between 10 and 14 characters inclusive
    assert 10 <= len(question) <= 14


def test_is_correct_answer():
    """Test that is_correct_answer correctly marks the user answer."""
    assert is_correct_answer(12, 12)  # Correct answer
    assert is_correct_answer(2, 8)  # Incorrect answer


def all_questions_answered():
    """Test that all_questions_answered correctly identifies completion."""
    assert all_questions_answered(10, 10)  # All questions answered
    assert all_questions_answered(5, 10)  # Not all questions answered
