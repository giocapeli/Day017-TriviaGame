import TriviaModule

questions_list = TriviaModule.TriviaQuestions()
play_again = True

print("Welcome to the Trivia Game!\nThis game uses data from https://opentdb.com/\n")

while play_again:
    for n in range(1, 11):
        questions_list.GetNextQuestion()
        guess = input(f'{questions_list.current_question}\nOptions: {questions_list.current_options}\n')
        questions_list.CheckAnswer(guess)
        print(f'Your score until now: {questions_list.score} of {n}\n')

    print(f'Total score: {questions_list.score}')
    continue_playing = input("Play again? (Y/N): \n").lower()
    if continue_playing == 'n':
        play_again = False

print("Thank you for playing!")