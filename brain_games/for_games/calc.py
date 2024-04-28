from random import randint
from random import choice
overview = ('What is the result of the expression?')


def correct_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    operation = choice(['+', '-', '*'])
    question = (f'{num_1} {operation} {num_2}')
    cor_answer = str(calculate(num_1, operation, num_2))
    return question, cor_answer


def calculate(num_1, operation, num_2):
    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    elif operation == '*':
        result = num_1 * num_2
    return result
