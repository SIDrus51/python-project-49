from random import randint

overview = ('What number is missing in the progression?')


def correct_answer():
    num_1 = randint(1, 20)  # число
    num_2 = randint(1, 10)  # шаг
    n = randint(5, 10)  # длина
    progression = [num_1 + num_2 * i for i in range(n)]
    index = randint(0, len(progression) - 1)  # случайный индекс
    answer = str(progression[index])  # сохраняем правильный ответ
    progression[index] = ".."
    question = ' '.join(map(str, progression))
    return question, answer
