import random
from collections import deque
from request_data import Questions
from messages import get_message
import html

letter_choices = ["A", "B", "C", "D", "E"]

class TriviaQuestions:

    def __init__(self):
        self.data = False
        self.questions = deque()
        self.current_question = 0
        self.current_options = 0
        self.correct_answer = 0
        self.score = 0

    def init_trivia(self):
        self.data = Questions()
        self.data.request_questions()
        for q in self.data.data:
            self.questions.append(q)

    def get_next_question(self):
        if len(self.questions) <= 0:
            self.init_trivia()
        
        self.current_question = self.questions[0]['question']
        self.correct_answer = self.questions[0]['correct_answer']
        self.current_options = {letter_choices[i]: o for i, o in enumerate(self.questions[0]['incorrect_answers'] + [self.correct_answer])}
        random.shuffle(list(self.current_options.values()))
        self.print_question()

    def print_question(self):
        unescape_question = html.unescape(self.current_question)
        print(f'Question {len(self.questions)}: {unescape_question}')
        print(f'Options:')
        for i, opt in self.current_options.items():
            unescape_option = html.unescape(opt)
            print(f'[{i}] {unescape_option}')

    def check_answer(self, guess):
        print(f'You guessed: {guess}, {self.current_options[guess]}')
        if self.current_options[guess] == self.correct_answer:
            self.score += 1
            get_message(self.questions[0], True)
        else:
            get_message(self.questions[0], False)
        print(f'Your score until now: {self.score}\n')
        self.questions.popleft()
