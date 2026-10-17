"""Лекция 1, §4. Императивный отбор студентов."""

from copy import deepcopy
from typing import TypedDict


class Student(TypedDict):
    """Запись студента с фамилией и непустым списком оценок."""

    name: str
    grades: list[int]


STUDENTS: list[Student] = [
    {"name": "Иванов", "grades": [80, 75, 90]},
    {"name": "Ахметова", "grades": [60, 70, 65]},
    {"name": "Серикбаев", "grades": [95, 88, 92]},
    {"name": "Ли", "grades": [74, 76, 75]},
]


def select_imperative(students: list[Student]) -> list[str]:
    """Отобрать фамилии при среднем балле >=75; оценки непустые."""
    result = []
    for s in students:
        total = 0
        for g in s["grades"]:
            total += g
        avg = total / len(s["grades"])
        if avg >= 75:
            result.append(s["name"].upper())
    result.sort()
    return result


if __name__ == "__main__":
    before = deepcopy(STUDENTS)
    print(
        "Средние баллы:",
        [round(sum(s["grades"]) / len(s["grades"]), 2) for s in STUDENTS],
    )
    print("Императивно:", select_imperative(STUDENTS))
    assert select_imperative(STUDENTS) == ["ИВАНОВ", "ЛИ", "СЕРИКБАЕВ"]
    assert select_imperative([]) == []
    assert select_imperative([{"name": "Ли", "grades": [75]}]) == ["ЛИ"]
    assert STUDENTS == before
    print("Проверки: 4 assert, успешно.")
