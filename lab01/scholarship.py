"""Практический пример из лабораторной: чистый расчёт стипендии."""

from collections.abc import Sequence
from copy import deepcopy
from typing import NotRequired, TypedDict


class Student(TypedDict):
    """Запись студента с необязательным вычисленным размером стипендии."""

    name: str
    grades: list[float]
    scholarship: NotRequired[float]


def average(grades: Sequence[float]) -> float:
    """Вернуть средний балл; для пустого набора оценок выдать ValueError."""
    if not grades:
        raise ValueError("Список оценок пуст")
    return sum(grades) / len(grades)


def scholarship_rate(avg: float) -> float:
    """Определить коэффициент 1.5, 1 или 0 по порогам 90 и 75."""
    return 1.5 if avg >= 90 else 1.0 if avg >= 75 else 0.0


def scholarship(student: Student, base: float) -> float:
    """Рассчитать сумму стипендии по явно переданной базовой сумме."""
    return base * scholarship_rate(average(student["grades"]))


def with_scholarship(student: Student, base: float) -> Student:
    """Создать независимую копию записи и добавить вычисленную стипендию."""
    result = deepcopy(student)
    result["scholarship"] = scholarship(student, base)
    return result


def test_core() -> None:
    """Проверить четыре функции и независимость вложенных данных."""
    student: Student = {"name": "Аружан", "grades": [92, 88, 95]}
    assert average([90, 100]) == 95
    assert average([0, 100]) == 50
    assert scholarship_rate(90) == 1.5
    assert scholarship_rate(75) == 1.0
    assert scholarship_rate(74.99) == 0
    assert scholarship(student, 50_000) == 75_000
    assert scholarship({"name": "X", "grades": [60, 70]}, 50_000) == 0
    result = with_scholarship(student, 50_000)
    assert result["scholarship"] == 75_000
    assert with_scholarship(student, 20_000)["scholarship"] == 30_000
    assert "scholarship" not in student
    result["grades"].append(100)
    assert student["grades"] == [92, 88, 95]


def main() -> None:
    """Продемонстрировать расчёт для двух студентов из условия."""
    test_core()
    students: list[Student] = [
        {"name": "Аружан", "grades": [92, 88, 95]},
        {"name": "Данияр", "grades": [80, 76, 79]},
    ]
    print("ПРИМЕР. Функциональный расчёт стипендии")
    for student in students:
        result = with_scholarship(student, 50_000)
        print(f"{result['name']:<10} {result['scholarship']:>10,.0f} тг")
    print("Исходные записи:", students)
    print("Проверки assert: 11/11 успешно.")


if __name__ == "__main__":
    main()
