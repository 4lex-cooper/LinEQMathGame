# Linear Equation Maths Game Documentation

## Introduction

The Linear Equation Maths Game is a mock exam style interactive game where users can practice linear algebra by solving simple randomly generated linear equestions. Players must answer a total of 10 questions by working out the value of the 'Y' variable and submitting their answers using the games graphical user interface.


## User Guide

Are you looking to improve your basic linear alebra maths skills? Well this game is right for you! Test your skill level by attempting to solve 10 randomly generated linear equations and you aren't happy with your score, then start a new game and try again!


### Features
- **Avoid memorisation with randomly generated linear equations**: Equations consist of two whole numbers, each from the value of 1 to 10, summed, subracted or multiplied together with an answer after an equals sign. One number is hidden under the variable 'Y'. This is the value that you must work out.
- **Learn and improve as you play with instant feedback on your answers**: Receive your mark after you answer each question. If your answer was incorrect, the game will tell you what the correct answer was. 
- **Sudden emergency? Easy to quit whenever you want**: Just press the 'Quit' button to end the game at any time.
- **Not so good with numbers? Keeps track of your score and your progress**: Your score and the amount of questions answered will be displayed throughout.  
- **Scared of the terminal? Play using the games simple user interface**: Do you miss Windows XP? Enjoy the games simple but effective user interface design. Who needs flashy colours and animations, right?
- **Cat like's walking on your keyboard? Invalid answers will not be accepted**: If you accidentally submit a blank value or a word instead of anumber, your answer will not be accepted and you will quietly be prompted for a valid answer. No one will ever know.


### What you'll need

- Required: Python (version 3.9 or later) installed on your computer.
- Optional: A Python interpreter or IDE such as PyCharm or Visual Studio Code with Python extension installed.

### How to Launch
- Simply run the game in your terminal or open the 'main.py' file with Python.

### How to Play
1. Read the instructions and click 'Start Game'.
2. Solve the equation.
3. Input your answer with your keyboard.
4. Click submit.
5. Answer 10 questions to complete the game.

### Example Gameplay


## Technical Documentation

### To clone the repository:

```bash
git clone https://github.com/4lex-cooper/LinEQMathGame.git
```

### Python Modules Used

- random:
- tkinter:
- tkk:


### Code Summary


### Variables

| Variable Name     | Data Type | Description                                              |
| ----------------- | --------- | -------------------------------------------------------- |
| instructions      | string    | Text that describes how to play the game for the user |
| question          | string    | Current linear equation maths question |
| user_answer_text  | string    | Latest answer submitted by the user |
| user_answer       | integer   | Latest answer submitted by the user converted to the int data type |
| correct_answer    | integer   | Correct answer to the current question |
| score             | integer   | Number of correct answers the user has submitted in the current game |
| questions_answered | integer  | Number of questions the user has answered in the current game |
| total_questions   | integer   | Total number of questions to be answered to complete the game |



### Modification Considerations





