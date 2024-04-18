#!/scr/bin/env python3
import random
import prompt
from brain_games.for_games.even import correct_answer
SCORE = 3


def game_logic():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0

    while index < SCORE:
       question, Correct_answer = correct_answer()
       print(f'Question: {question}')
       user_answer = prompt.string('Answer: ')
       if user_answer == Correct_answer:
           print('Correct!')
           index = index +1
           if index == 3:
               print(f'Congratulations, {name} !')
       else:
           print(f"'{user_answer}' is wrong answer ;(. Correct answer was another answer  '{Correct_answer}'\nLet's try again, {name}! " )
           break


if __name__ == '__main__':
    main()
