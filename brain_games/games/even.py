import random

overview = ('Answer "yes" if the number is even, otherwise answer "no".')


def correct_answer():
    random_num = get_random_num(1, 100)
    question = random_num
    if random_num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def get_random_num(min_value, max_value):
    return random.randint(min_value, max_value)
