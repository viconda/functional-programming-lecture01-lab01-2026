"""СРС 1. Анализ пяти функций существующего проекта lab1_Швачкина.
Четыре вычисления сохранены по смыслу, добавлены типы и docstrings.
Исходный run_file из run_all.py сохранён без изменения тела.
Для нечистой функции отделено построение плана от исполнения файла.
"""

import runpy
from collections.abc import Sequence
from contextlib import redirect_stdout
from io import StringIO
from math import isclose, pi
from pathlib import Path, PurePath


def circle_area(r: float) -> float:
    """task_01.py: вернуть площадь круга при r >= 0."""
    return pi * r**2


def rect_perimeter(a: float, b: float) -> float:
    """task_01.py: вернуть периметр прямоугольника при a,b >= 0."""
    return 2 * (a + b)


def celsius_to_fahrenheit(temps: Sequence[float]) -> list[float]:
    """task_02.py: вернуть новый список температур Фаренгейта."""
    return list(map(lambda c: c * 9 / 5 + 32, temps))


def long_words_comp(words: Sequence[str]) -> list[str]:
    """task_04.py: вернуть слова длиннее пяти символов."""
    return [w for w in words if len(w) > 5]


def run_file(name: str) -> None:
    """run_all.py: напечатать заголовок и выполнить внешний файл."""
    print(f"\n--- {name} ---")
    runpy.run_path(str(Path(__file__).with_name(name)), run_name="__main__")


def build_run_plan(script_path: str, name: str) -> tuple[str, str]:
    """Чистая часть run_file: подготовить заголовок и путь без I/O."""
    return f"\n--- {name} ---", str(PurePath(script_path).with_name(name))


if __name__ == "__main__":
    temps = [0, 20, 100]
    words = ["python", "код", "функция"]
    print("1. circle_area(5):", round(circle_area(5), 2), "; чистая")
    print("2. rect_perimeter(4, 6):", rect_perimeter(4, 6), "; чистая")
    print("3. celsius_to_fahrenheit:", celsius_to_fahrenheit(temps), "; чистая")
    print("4. long_words_comp:", long_words_comp(words), "; чистая")
    captured = StringIO()
    with redirect_stdout(captured):
        # Для учебной проверки намеренно сохраняем возврат None.
        returned = run_file("p31.py")  # type: ignore[func-returns-value]
    print("5. run_file: нечистая, выполнен p31.py и перехвачен stdout.")
    print("Подтверждение вывода:", captured.getvalue().strip().splitlines()[1])
    plan = build_run_plan("lecture01/srs1.py", "p31.py")
    print("Чистый вариант, план:", plan)
    assert isclose(circle_area(5), 78.53981633974483)
    assert circle_area(0) == 0
    assert rect_perimeter(4, 6) == 20
    assert rect_perimeter(0, 0) == 0
    assert celsius_to_fahrenheit(temps) == [32, 68, 212]
    assert temps == [0, 20, 100]
    assert long_words_comp(words) == ["python", "функция"]
    assert words == ["python", "код", "функция"]
    assert returned is None and "f(5) = 25" in captured.getvalue()
    assert plan == ("\n--- p31.py ---", str(PurePath("lecture01/p31.py")))
    assert plan == build_run_plan("lecture01/srs1.py", "p31.py")
    print("Проверки: 11 assert и реальные вызовы всех 5 функций, успешно.")
