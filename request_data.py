import requests

open_trivia_URL = "https://opentdb.com/api.php"
head_start = {
    "amount": 10,
    "type": "boolean",
    "difficulty":"easy",
    "token":''
}

class Questions:

    def __init__(self):
        self.token = False
        self.data = False
        self.head = head_start

    def request_questions(self):
        if not self.head["token"]:
            self.head["token"] = self.request_token() 
        response = requests.get(open_trivia_URL, self.head)
        if response.status_code == 200:
            self.data = response.json()["results"]
        else:
            print(f"Request failed with status code: {response.status_code}")
            return False

    def request_token(self):
        token_url = "https://opentdb.com/api_token.php?command=request"
        response = requests.get(token_url)
        if response.status_code == 200:
            data = response.json()
            return data["token"]
        else:
            print(f"Request failed with status code: {response.status_code}")
        return False
