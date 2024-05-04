from random import randint

overview = ('Answer "yes" if given number is prime. Otherwise answer "no".')


def correct_answer():
    question = (f'{randint(1, 100)}')
    answer = is_prime(question)
    return question, answer


def is_prime(question):
    a = int(question)
    for i in range(2, (a // 2) + 1):
        if a % i == 0:
            return 'no'
    return 'yes'
