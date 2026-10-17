"""Буквальная копия f1–f8 из условия для анализа нечистого кода.

Изменяемые globals и отсутствие аннотаций оставлены намеренно:
это исходный материал преподавателя, а не рекомендуемая реализация.
"""

import random, datetime

counter = 0
CONFIG = {"tax": 0.12}


def f1(a, b):
    return a * b + 1


def f2(x):
    global counter
    counter += 1
    return x * counter


def f3(items):
    items.sort()
    return items[0]


def f4(price):
    return price * (1 + CONFIG["tax"])


def f5(text):
    return text.strip().lower().split()


def f6(n):
    return [random.randint(1, 6) for _ in range(n)]


def f7(name):
    print("Привет,", name)
    return len(name)


def f8(birth_year):
    return datetime.date.today().year - birth_year
