"""Лекция 1, §4. Конвейер filter, map, sorted."""

from copy import deepcopy
from statistics import mean

from p4_imp import STUDENTS, Student, select_imperative


def is_good(student: Student, threshold: float = 75) -> bool:
    """Проверить среднюю оценку; список оценок должен быть непустым."""
    return mean(student["grades"]) >= threshold


def display_name(student: Student) -> str:
    """Вернуть фамилию в верхнем регистре."""
    return student["name"].upper()


def select_functional(students: list[Student]) -> list[str]:
    """Вернуть отсортированные фамилии без изменения исходных данных."""
    return sorted(map(display_name, filter(is_good, students)))


if __name__ == "__main__":
    before = deepcopy(STUDENTS)
    print("filter:", [s["name"] for s in filter(is_good, STUDENTS)])
    print("map + sorted:", select_functional(STUDENTS))
    assert select_functional(STUDENTS) == select_imperative(STUDENTS)
    assert select_functional([]) == []
    assert is_good({"name": "Ли", "grades": [75]})
    assert not is_good({"name": "Тест", "grades": [74]})
    assert STUDENTS == before
    print("Проверки: 5 assert, успешно.")
