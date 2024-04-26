from random import randint
import math
overview = ('Find the greatest common divisor of given numbers.')

def correct_answer():
    num_1 = randint(1,100)
    num_2 = randint(1,100)
    question = f'{num_1} {num_2}'
    cor_answer = str(calculate(num_1, num_2))
    return question, cor_answer


def calculate(num_1, num_2):
    math_answer = math.gcd(num_1, num_2)
    return math_answer
