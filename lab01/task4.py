"""Задание 4. Вариант 3, успеваемость студентов.

Шкала передаётся аргументом. Демонстрационные пороги взяты из опубликованной
общей шкалы Satbayev University. Это перевод среднего балла в букву,
а не полный алгоритм официальной итоговой оценки с экзаменом и допуском.
Силлабус конкретной дисциплины CSE6742 не приложен.
"""

from collections.abc import Callable, Sequence

Student = tuple[str, tuple[float, ...]]
Scale = tuple[tuple[float, str], ...]


def average_grade(grades: Sequence[float]) -> float:
    """Найти средний балл непустой последовательности оценок 0..100."""
    if not grades or any(not 0 <= grade <= 100 for grade in grades):
        raise ValueError("Нужна непустая последовательность оценок от 0 до 100")
    return sum(grades) / len(grades)


def letter_grade(score: float, scale: Scale) -> str:
    """Определить букву по убывающим нижним порогам заданной шкалы."""
    if not 0 <= score <= 100:
        raise ValueError("Балл должен лежать в диапазоне 0..100")
    if (
        not scale
        or scale[-1][0] != 0
        or any(not 0 <= threshold <= 100 for threshold, _ in scale)
        or any(scale[i][0] <= scale[i + 1][0] for i in range(len(scale) - 1))
    ):
        raise ValueError("Пороги шкалы должны строго убывать и завершаться нулём")
    return next(letter for threshold, letter in scale if score >= threshold)


def group_ranking(students: Sequence[Student]) -> list[Student]:
    """Вернуть рейтинг по убыванию среднего, при равенстве по имени."""
    return sorted(
        students, key=lambda student: (-average_grade(student[1]), student[0])
    )


def select_students(
    students: Sequence[Student],
    predicate: Callable[[Student], bool],
) -> list[Student]:
    """Отобрать студентов по переданному чистому условию."""
    return [student for student in students if predicate(student)]


def group_average(students: Sequence[Student]) -> float:
    """Найти среднее средних баллов студентов с одинаковым весом каждого."""
    return average_grade([average_grade(student[1]) for student in students])


def test_core() -> None:
    """Проверить каждую функцию, границы шкалы и сохранность данных."""
    scale: Scale = (
        (95, "A"),
        (90, "A-"),
        (85, "B+"),
        (80, "B"),
        (75, "B-"),
        (70, "C+"),
        (65, "C"),
        (60, "C-"),
        (55, "D+"),
        (50, "D"),
        (25, "FX"),
        (0, "F"),
    )
    students: list[Student] = [("Алия", (90, 95)), ("Данияр", (70, 80))]
    original = students.copy()
    assert average_grade((90, 95)) == 92.5
    assert average_grade((0, 100)) == 50
    assert letter_grade(95, scale) == "A"
    assert letter_grade(94.99, scale) == "A-"
    assert letter_grade(50, scale) == "D"
    assert letter_grade(49.99, scale) == "FX"
    assert letter_grade(25, scale) == "FX"
    assert letter_grade(24.99, scale) == "F"
    assert letter_grade(0, scale) == "F"
    assert letter_grade(100, scale) == "A"
    assert group_ranking(students)[0][0] == "Алия"
    assert group_ranking([]) == []
    assert select_students(
        students, lambda student: average_grade(student[1]) >= 90
    ) == [students[0]]
    assert select_students(students, lambda student: False) == []
    assert group_average(students) == 83.75
    assert group_average([("X", (0,)), ("Y", (100, 100, 100))]) == 50
    assert students == original
    assert group_ranking([("Б", (80,)), ("А", (80,))])[0][0] == "А"
    try:
        average_grade(())
    except ValueError as error:
        assert "непустая" in str(error)
    else:
        raise AssertionError("Пустой набор оценок должен вызвать ValueError")


def main() -> None:
    """Выполнить проверки и показать индивидуальное задание."""
    test_core()
    scale: Scale = (
        (95, "A"),
        (90, "A-"),
        (85, "B+"),
        (80, "B"),
        (75, "B-"),
        (70, "C+"),
        (65, "C"),
        (60, "C-"),
        (55, "D+"),
        (50, "D"),
        (25, "FX"),
        (0, "F"),
    )
    students: list[Student] = [
        ("Аружан", (92, 88, 95)),
        ("Данияр", (80, 76, 79)),
        ("Виктория", (96, 98, 94)),
        ("Алия", (65, 70, 75)),
    ]
    original = students.copy()
    print("ЗАДАНИЕ 4. Вариант 3. Успеваемость студентов")
    print("Буквенное отображение среднего по опубликованной общей шкале SU.")
    for place, (name, grades) in enumerate(group_ranking(students), start=1):
        score = average_grade(grades)
        print(
            f"{place}. {name:<10} средний {score:6.2f}; оценка {letter_grade(score, scale)}"
        )
    best = select_students(students, lambda student: average_grade(student[1]) >= 90)
    print("Средний балл не ниже 90:", [student[0] for student in best])
    print(f"Среднее средних баллов группы: {group_average(students):.2f}")
    print("Исходные данные не изменились:", students == original)
    print("Проверки assert: 19/19 успешно.")


if __name__ == "__main__":
    main()
