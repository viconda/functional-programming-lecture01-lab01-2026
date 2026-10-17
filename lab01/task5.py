"""Задание 5. Эвристика обнаружения некоторых признаков нечистоты."""

import io
import random
from collections.abc import Callable
from contextlib import redirect_stdout
from copy import deepcopy
from typing import Any

import impure_examples as original


def check_purity(
    func: Callable[..., Any],
    *args: Any,
    runs: int = 3,
) -> dict[str, bool]:
    """Сравнить результаты повторов и исходные аргументы; это не доказательство.

    Проверяемая функция получает исходные объекты, а не их копии.
    После каждого вызова результат сразу копируется, иначе повторная мутация
    одного возвращаемого объекта могла бы скрыть различие результатов.
    Исключения func не подавляются. Сравнение требует корректного ==.
    """
    if not isinstance(runs, int) or isinstance(runs, bool) or runs < 2:
        raise ValueError("runs должно быть целым числом не меньше 2")
    before = deepcopy(args)
    results = []
    unchanged = True
    for _ in range(runs):
        results.append(deepcopy(func(*args)))
        unchanged = unchanged and args == before
    return {
        "deterministic": all(result == results[0] for result in results[1:]),
        "args_unchanged": unchanged,
    }


def test_core() -> None:
    """Проверить чистый вызов, изменения аргумента, алиас результата и stdout."""
    assert check_purity(lambda value: value * value, 3) == {
        "deterministic": True,
        "args_unchanged": True,
    }
    assert check_purity(original.f3, [3, 1, 2]) == {
        "deterministic": True,
        "args_unchanged": False,
    }
    shared: list[int] = []

    def reused_result(value: int) -> list[int]:
        """Нечистый тестовый пример: возвращает и меняет один общий список."""
        shared.append(value)
        return shared

    assert check_purity(reused_result, 5) == {
        "deterministic": False,
        "args_unchanged": True,
    }
    assert shared == [5, 5, 5]
    output = io.StringIO()
    with redirect_stdout(output):
        result = check_purity(original.f7, "Алия")
    assert result == {"deterministic": True, "args_unchanged": True}
    assert output.getvalue().splitlines() == ["Привет, Алия"] * 3
    try:
        check_purity(lambda value: value, 1, runs=1)
    except ValueError as error:
        assert "не меньше 2" in str(error)
    else:
        raise AssertionError("Один запуск не позволяет сравнивать повторы")


def main() -> None:
    """Применить эвристику ко всем восьми исходным функциям."""
    test_core()
    original.counter = 0
    random.seed(2026)  # Для воспроизводимости опыта, не для чистоты f6.
    cases = (
        (original.f1, (2, 3)),
        (original.f2, (5,)),
        (original.f3, ([3, 1, 2],)),
        (original.f4, (100,)),
        (original.f5, ("  Привет МИР  ",)),
        (original.f6, (8,)),
        (original.f7, ("Алия",)),
        (original.f8, (2007,)),
    )
    print("ЗАДАНИЕ 5. Эвристическая проверка исходных f1–f8")
    print("Функция   deterministic   args_unchanged")
    for func, args in cases:
        output = io.StringIO()
        with redirect_stdout(output):
            result = check_purity(func, *args)
        print(
            f"{func.__name__:<9} {result['deterministic']!s:<15} "
            f"{result['args_unchanged']}"
        )
        if output.getvalue():
            print("  Отдельно замечен stdout:", repr(output.getvalue()))
    print("f4, f7, f8 прошли эвристику, но ручной анализ выявляет нечистоту.")
    print("Проверка алиаса результата выявила изменение: False/True.")
    print("Проверки assert: 7/7 успешно.")


if __name__ == "__main__":
    main()
