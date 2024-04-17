import random

def correct_answer():
    random_num = random.randint(1, 100)

    if random_num % 2 ==0:
        Correct_answer = 'yes'
    else:
        Correct_answer = 'no'
    question = random_num
    return question, Correct_answer
