import tkinter as tk
from tkinter import ttk
from functions import (
    generate_lineq_question,
    is_correct_answer,
    all_questions_answered,
    format_instructions_text,
    format_final_feedback,
)


class AppWindow(tk.Tk):
    def __init__(self):
        """Initialize the main application window."""
        # Setup window.
        super().__init__()
        self.title("Linear Equation Maths Game")
        self.geometry("500x300")

        # Show instructions and start game button.
        self.InstructionsFrame = InstructionsFrame(self)
        self.start_game_button = ttk.Button(
            self, text="Start Game", command=self.start_game_click
        )
        self.start_game_button.pack()

    def start_game_click(self):
        """Move to questions frame."""
        self.InstructionsFrame.pack_forget()
        self.start_game_button.pack_forget()
        self.QuestionFrame = QuestionsFrame(self)


class InstructionsFrame(ttk.Frame):
    def __init__(self, parent):
        """Initialize the instructions frame."""
        # Setup and place frame.
        super().__init__(parent)
        self.pack()

        # Create and place instructions in frame.
        instructions = format_instructions_text()
        self.instructions_label = ttk.Label(self, text=instructions)
        self.instructions_label.pack()


class QuestionsFrame(ttk.Frame):
    def __init__(self, parent):
        """Initialize the questions frame."""
        # Initialize variables.
        self.question = None
        self.user_answer_text = None
        self.user_answer = None
        self.correct_answer = None
        self.score = 0
        self.questions_answered = 0
        self.total_questions = 10

        # Setup and place frame.
        super().__init__(parent)
        self.pack()

        # Create widgets.
        self.answer_feedback_label = ttk.Label(self, text=None)
        self.question_label = ttk.Label(self, text=self.question)
        self.score_label = ttk.Label(self, text="Score: 0 / 0")
        self.game_completed_label = ttk.Label(self, text=None)
        self.quit_game_button = ttk.Button(self, text="Quit", command=self.close_click)
        self.close_button = ttk.Button(self, text="Close", command=self.close_click)
        self.submit_answer_button = ttk.Button(
            self, text="Submit", command=self.submit_answer_click
        )
        self.user_answer_entry = ttk.Entry(self)

        # Place widgets.
        self.answer_feedback_label.pack(padx=5, pady=5)
        self.score_label.pack(padx=5, pady=5)
        self.question_label.pack(padx=5, pady=5)
        self.user_answer_entry.pack(padx=5, pady=5)
        self.submit_answer_button.pack(padx=5, pady=5, side=tk.RIGHT)
        self.quit_game_button.pack(padx=5, pady=5, side=tk.RIGHT)

        # Generate first question.
        self.show_next_question()

    def show_next_question(self):
        """Generate new question and update widget text."""
        self.question, self.correct_answer = generate_lineq_question()
        self.question_label.configure(text=self.question)

    def submit_answer_click(self):
        """Check answer, track score and progress then move to next question"""
        # Handle non-integer and blank input errors.
        self.user_answer_text = self.user_answer_entry.get()
        try:
            type(int(self.user_answer_text))
        except ValueError:
            self.answer_feedback_label.configure(
                text="Psst! Enter an whole number with the number keys."
            )

        # Save and clear answer.
        self.user_answer = int(self.user_answer_entry.get())
        self.user_answer_entry.delete(0, tk.END)

        # Check answer and update score.
        if is_correct_answer(self.user_answer, self.correct_answer):
            self.score += 1
            self.answer_feedback_label.configure(text="That is correct, well done!")
        else:
            self.answer_feedback_label.configure(
                text=(
                    "That is incorrect."
                    f"The correct answer was {self.correct_answer}."
                )
            )

        # Track completion progress.
        self.questions_answered += 1
        if all_questions_answered(self.questions_answered, self.total_questions):
            self.game_completed()

        # Show score.
        self.score_label.config(text=f"Score: {self.score} / {self.questions_answered}")

        # Move to next question.
        self.show_next_question()

    def game_completed(self):
        """Summarize game results to user."""
        # Remove all active widgets.
        self.answer_feedback_label.pack_forget()
        self.score_label.pack_forget()
        self.question_label.pack_forget()
        self.user_answer_entry.pack_forget()
        self.submit_answer_button.pack_forget()
        self.quit_game_button.pack_forget()

        # Show final summary feedback.
        game_completed_text = format_final_feedback(self.score, self.questions_answered)
        self.game_completed_label.config(text=game_completed_text)
        self.game_completed_label.pack()

        # Show close game button.
        self.close_button.pack()

    def close_click(self):
        """Quit and exit the game application."""
        quit()


def main():
    """Run the application."""
    app = AppWindow()
    app.mainloop()


# Ensure game is only run if this is the file that is originally executed.
if __name__ == "__main__":
    main()
