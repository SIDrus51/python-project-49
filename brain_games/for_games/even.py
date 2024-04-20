import random

overview = ('Answer "yes" if the number is even, otherwise answer "no".')


def correct_answer():
    random_num = get_random_num(1,100)
    question = random_num
    if random_num % 2 ==0:
        Correct_answer = 'yes'
    else:
        Correct_answer = 'no'
    return question, Correct_answer

def get_random_num(min_value, max_value):
    return random.randint(min_value, max_value)
