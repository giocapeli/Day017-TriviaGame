import request_data
import random
import messages
class TriviaQuestions:

    def __init__(self):
        self.data = False
        self.questions = []
        self.current_question = 0
        self.current_options = 0
        self.correct_answer = 0
        self.score = 0

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

    def check_answer(self, guess):
        print(f'You guessed: {guess}')
        if guess == self.correct_answer:
            self.score += 1
            messages.get_message(self.questions[0], True)
        else:
            messages.get_message(self.questions[0], False)
        self.questions.pop(0)

