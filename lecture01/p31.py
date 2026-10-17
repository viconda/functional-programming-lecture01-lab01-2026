"""Лекция 1, §3.1. Функции как значения первого класса."""

from collections.abc import Callable


def square(x: int) -> int:
    """Вернуть квадрат целого числа."""
    return x * x


def cube(x: int) -> int:
    """Вернуть куб целого числа."""
    return x**3


def apply_twice(func: Callable[[int], int], value: int) -> int:
    """Дважды применить переданную функцию к значению."""
    return func(func(value))


if __name__ == "__main__":
    operations: list[Callable[[int], int]] = [square, cube, abs]
    f = square
    print("f(5) =", f(5))
    print("operations(-3) =", [op(-3) for op in operations])
    print("apply_twice(square, 3) =", apply_twice(square, 3))
    assert f(5) == 25
    assert [op(-3) for op in operations] == [9, -27, 3]
    assert apply_twice(square, 3) == 81
    assert apply_twice(abs, -3) == 3
    print("Проверки: 4 assert, успешно.")
