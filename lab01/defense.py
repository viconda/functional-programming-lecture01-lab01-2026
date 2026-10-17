"""Проверка небольшого изменения критерия для подготовки к защите."""

from task4 import Student, average_grade, select_students


def main() -> None:
    """Сравнить пороги 90 и 95, не меняя алгоритм отбора."""
    students: list[Student] = [
        ("Аружан", (92, 88, 95)),
        ("Данияр", (80, 76, 79)),
        ("Виктория", (96, 98, 94)),
        ("Алия", (65, 70, 75)),
    ]
    before = students.copy()
    print("ПОДГОТОВКА К ЗАЩИТЕ. Изменение условия отбора")
    for threshold in (90, 95):
        selected = select_students(
            students, lambda student: average_grade(student[1]) >= threshold
        )
        names = [student[0] for student in selected]
        expected = ["Аружан", "Виктория"] if threshold == 90 else ["Виктория"]
        assert names == expected
        print(f"Порог {threshold}: {names}")
    assert students == before
    print("Исходные записи не изменились:", students == before)
    print("Формула для Виктории: (96 + 98 + 94) / 3 =", average_grade((96, 98, 94)))
    print("Проверка обоих условий и неизменности данных прошла.")


if __name__ == "__main__":
    main()
