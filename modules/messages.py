import questions
import random

correct_answer = [
    "You've got it right!",
    "Well Done!",
    "On point!",
    "You're right!",
    "Correct!",
    "On spot!",
    "Simply correct!"
]

incorrect_answer = [
    "Incorrect!",
    "Unfortunally, incorrect!",
    "You're wrong!",
    "Not right!",
    "Sorry, wrong answer!",
    "You missed!"
]

def get_message(question, correct):
    right_answer = f'The right answer is "{question.correct_answer}".'
    if correct:
        response = f'{random.choice(correct_answer)} {right_answer}'
    else:
        response = f'{random.choice(incorrect_answer)} {right_answer}'
    print(response)

    
