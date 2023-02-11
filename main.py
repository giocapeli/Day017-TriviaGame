from modules import questions

questions_list = questions.TriviaQuestions()
play_again = True

print("Welcome to the Trivia Game!\nThis game uses data from https://opentdb.com/\n")

questions_list.init_trivia()

while play_again:
    for n in range(1, 11):
        questions_list.get_next_question()
        guess = input(f'Your answer: ').upper().split()[0]
        questions_list.check_answer(guess)

    print(f'Total score: {questions_list.score}')
    continue_playing = input("Play again? (Y/N): \n").lower()
    if continue_playing == 'n':
        play_again = False

print("Thank you for playing!")