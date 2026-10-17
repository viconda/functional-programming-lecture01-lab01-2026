"""Лекция 1, §4. Генераторное выражение из лекции."""

from statistics import mean

from p4_func import select_functional
from p4_imp import STUDENTS, Student, select_imperative


def select_comprehension(students: list[Student]) -> list[str]:
    """Вернуть фамилии с помощью sorted и генераторного выражения."""
    return sorted(s["name"].upper() for s in students if mean(s["grades"]) >= 75)


if __name__ == "__main__":
    short: list[Student] = [
        {"name": "Иванов", "grades": [80, 75, 90]},
        {"name": "Ли", "grades": [74, 76, 75]},
    ]
    print("Два студента из фрагмента лекции:", select_comprehension(short))
    print("Все четыре студента:", select_comprehension(STUDENTS))
    assert select_comprehension(short) == ["ИВАНОВ", "ЛИ"]
    assert select_comprehension(STUDENTS) == ["ИВАНОВ", "ЛИ", "СЕРИКБАЕВ"]
    assert select_comprehension(STUDENTS) == select_functional(STUDENTS)
    assert select_comprehension(STUDENTS) == select_imperative(STUDENTS)
    assert select_comprehension([]) == []
    print("Проверки: 5 assert, успешно.")
