import request_data
import random
import messages

letter_choices = ["A", "B", "C", "D", "E"]

class TriviaQuestions:

    def __init__(self):
        self.data = False
        self.questions = []
        self.current_question = 0
        self.current_options = 0
        self.correct_answer = 0
        self.score = 0
        self.question_n = 1

    def init_trivia(self):
        self.data = request_data.Questions()
        self.get_questions(self)

    def get_questions(self):
        if not self.data:
            self.init_trivia()
        self.data.request_questions()
        for q in self.data['results']:
            self.questions.append(q)

    def get_next_question(self):
        if len(self.questions) <= 0:
            self.get_questions(self)
        
        self.current_question = self.questions[0]['question']
        self.correct_answer = self.questions[0]['correct_answer']
        self.current_options = self.questions[0]['incorrect_answers']
        self.current_options.append(self.correct_answer)
        random.shuffle(self.current_options)
        self.print_question(self)
        self.question_n += 1

    def print_question(self):
        print(f'Question {self.question_n}: {self.current_question}')
        print(f'Options:')
        for i, o in enumerate(self.current_options):
            print(f'[{letter_choices[i]}] {o}')

    def check_answer(self, guess):
        index = letter_choices.index(guess)
        print(f'You guessed: {guess}, {self.current_options[index]}')
        if self.current_options[index] == self.correct_answer:
            self.score += 1
            messages.get_message(self.questions[0], True)
        else:
            messages.get_message(self.questions[0], False)
        print(f'Your score until now: {questions_list.score} of {n}\n')
        self.questions.pop(0)

