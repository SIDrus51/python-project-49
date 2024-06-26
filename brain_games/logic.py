#!/scr/bin/env python3
import prompt

SCORE = 3


def game_logic(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.overview)
    index = 0

    while index < SCORE:
        question, answer = game.correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Answer: ')
        if user_answer == answer:
            print('Correct!')
            index = index + 1
            if index == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was another answer '{answer}'.")
            print(f"Let's try again, {name}!")
            break
