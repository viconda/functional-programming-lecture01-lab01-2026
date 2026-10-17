"""Задание 1. Чистые варианты восьми функций из условия."""

from collections.abc import Sequence


def f1(a: float, b: float) -> float:
    """Вычислить a * b + 1. Исходная функция уже была чистой."""
    return a * b + 1


def f2(x: float, counter: int) -> tuple[float, int]:
    """Вернуть результат и новое состояние счётчика без изменения globals."""
    new_counter = counter + 1
    return x * new_counter, new_counter


def f3(items: Sequence[float]) -> float:
    """Вернуть минимум непустой последовательности, не сортируя её на месте."""
    if not items:
        raise ValueError("Нельзя найти минимум пустой последовательности")
    return min(items)


def f4(price: float, tax: float) -> float:
    """Рассчитать цену с явно переданной ставкой налога."""
    return price * (1 + tax)


def f5(text: str) -> list[str]:
    """Убрать внешние пробелы и получить слова в нижнем регистре."""
    return text.strip().lower().split()


def f6(n: int, draws: Sequence[int]) -> list[int]:
    """Взять n заранее полученных бросков; случайность остаётся в оболочке."""
    if n < 0 or n > len(draws):
        raise ValueError("Нужно передать не менее n бросков, n >= 0")
    if any(value < 1 or value > 6 for value in draws):
        raise ValueError("Бросок кубика должен лежать в диапазоне 1..6")
    return list(draws[:n])


def f7(name: str) -> tuple[str, int]:
    """Подготовить приветствие и длину имени без печати."""
    return f"Привет, {name}", len(name)


def f8(birth_year: int, current_year: int) -> int:
    """Вычислить разность лет по явным аргументам, как в условии."""
    return current_year - birth_year


def test_core() -> None:
    """Проверить каждую функцию дважды, а также неизменность списка."""
    assert f1(2, 3) == 7
    assert f1(0, -7) == 1
    assert f2(5, 0) == (5, 1)
    assert f2(5, 3) == (20, 4)
    items = [3, 1, 2]
    assert f3(items) == 1
    assert f3((-2, 5)) == -2
    assert items == [3, 1, 2]
    assert abs(f4(100, 0.12) - 112) < 1e-9
    assert f4(100, 0) == 100
    assert f5("  Привет МИР  ") == ["привет", "мир"]
    assert f5(" \t ") == []
    assert f6(3, (2, 6, 1, 4)) == [2, 6, 1]
    assert f6(0, ()) == []
    assert f7("Алия") == ("Привет, Алия", 4)
    assert f7("") == ("Привет, ", 0)
    assert f8(2007, 2026) == 19
    assert f8(2026, 2026) == 0


def main() -> None:
    """Запустить проверки и показать чистые вычисления."""
    test_core()
    print("ЗАДАНИЕ 1. Чистые варианты функций")
    print("f1(2, 3) =", f1(2, 3))
    print("f2(5, counter=3) =", f2(5, 3))
    items = [3, 1, 2]
    print("f3([3, 1, 2]) =", f3(items), "; исходный список:", items)
    print("f4(100, tax=0.12) =", round(f4(100, 0.12), 2))
    print("f5('  Привет МИР  ') =", f5("  Привет МИР  "))
    print("f6(3, draws=(2, 6, 1, 4)) =", f6(3, (2, 6, 1, 4)))
    print("f7('Алия') =", f7("Алия"))
    print("f8(2007, current_year=2026) =", f8(2007, 2026))
    print("Проверки assert: 17/17 успешно.")


if __name__ == "__main__":
    main()
