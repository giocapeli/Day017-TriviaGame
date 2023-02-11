import requests
import random

class TriviaQuestions:

    def __init__(self):
        self.session_token = 0
        self.questions = []
        self.current_question = 0
        self.current_options = 0
        self.correct_answer = 0
        self.score = 0

    def GetQuestions(self):
        self.GetSessionToken()
        url = f"https://opentdb.com/api.php?amount=10&{self.session_token}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.questions = data['results']
        else:
            print(f"Request failed with status code: {response.status_code}")

    def GetSessionToken(self):
        url = "https://opentdb.com/api_token.php?command=request"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.session_token = data["token"]
        else:
            print(f"Request failed with status code: {response.status_code}")

    def GetNextQuestion(self):
        if len(self.questions) <= 0:
            self.GetQuestions()
        
        self.current_question = self.questions[0]['question']
        self.correct_answer = self.questions[0]['correct_answer']
        self.current_options = self.questions[0]['incorrect_answers']
        self.current_options.append(self.correct_answer)
        random.shuffle(self.current_options)

        self.questions.pop(0)


    def CheckAnswer(self, guess):
        print(f'You guessed: {guess}')
        if guess == self.correct_answer:
            self.score += 1
            print("Right answer!")
            return True
        else:
            print(f"Wrong answer! The right one is '{self.correct_answer}'")
            return False

