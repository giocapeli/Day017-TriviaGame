import requests

class Questions:

    def __init__(self):
        self.token = False
        self.data = False

    def request_questions(self):
        if not self.token:
            self.token = self.request_token() 
        url = f"https://opentdb.com/api.php?amount=10&{self.token if self.token else ''}"
        response = requests.get(url)
        if response.status_code == 200:
            self.data = response.json()["results"]
        else:
            print(f"Request failed with status code: {response.status_code}")
            return False

    def request_token(self):
        url = "https://opentdb.com/api_token.php?command=request"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["token"]
        else:
            print(f"Request failed with status code: {response.status_code}")
        return False
