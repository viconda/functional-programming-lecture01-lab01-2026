"""Задание 3. Передача, хранение и возврат функций."""

import math
import operator
from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")


def apply_n(f: Callable[[T], T], n: int, x: T) -> T:
    """Применить чистую f ровно n раз; n должно быть целым и неотрицательным."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n должно быть целым неотрицательным числом")
    result = x
    for _ in range(n):
        result = f(result)
    return result


def apply_all(funcs: Sequence[Callable[[T], R]], x: T) -> list[R]:
    """Применить каждую переданную функцию к одному аргументу."""
    return [func(x) for func in funcs]


def calculate(expression: str) -> float | None:
    """Вычислить 'число оператор число'; при некорректном вводе вернуть None."""
    operations: dict[str, Callable[[float, float], float]] = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow,
        "%": operator.mod,
    }
    parts = expression.split()
    if len(parts) != 3 or parts[1] not in operations:
        return None
    try:
        left, right = float(parts[0]), float(parts[2])
        if not math.isfinite(left) or not math.isfinite(right):
            return None
        value = operations[parts[1]](left, right)
        if isinstance(value, complex) or not math.isfinite(value):
            return None
        return float(value)
    except (ValueError, ZeroDivisionError, OverflowError):
        return None


def make_counter_of(
    predicate: Callable[[T], bool],
) -> Callable[[Sequence[T]], int]:
    """Вернуть счётчик элементов, удовлетворяющих чистому предикату."""

    def count_matching(items: Sequence[T]) -> int:
        """Сосчитать подходящие элементы, не изменяя последовательность."""
        return sum(1 for item in items if predicate(item))

    return count_matching


def test_core() -> None:
    """Проверить функции высшего порядка и все операции калькулятора."""
    assert apply_n(lambda value: value * 2, 3, 1) == 8
    assert apply_n(lambda value: value + 10, 0, 7) == 7
    assert apply_all([lambda value: value + 1, lambda value: value * 2], 3) == [4, 6]
    assert apply_all([], 3) == []
    assert calculate("12 + 4") == 16.0
    assert calculate("12 - 4") == 8.0
    assert calculate("12 * 4") == 48.0
    assert calculate("12 / 4") == 3.0
    assert calculate("2 ** 3") == 8.0
    assert calculate("13 % 4") == 1.0
    assert calculate("12 / 0") is None
    assert calculate("12 % 0") is None
    assert calculate("wrong") is None
    assert calculate("12 ? 4") is None
    assert calculate("nan + 2") is None
    assert calculate("-1 ** 0.5") is None
    assert calculate("one + 2") is None
    even: Callable[[Sequence[int]], int] = make_counter_of(lambda value: value % 2 == 0)
    positive: Callable[[Sequence[int]], int] = make_counter_of(lambda value: value > 0)
    assert even([1, 2, 3, 4]) == 2
    assert even([]) == 0
    assert positive([-2, 0, 3, 4]) == 2
    assert positive([-2, 0]) == 0
    try:
        apply_n(lambda value: value, -1, 0)
    except ValueError as error:
        assert "неотрицательным" in str(error)
    else:
        raise AssertionError("Отрицательное n должно вызвать ValueError")


def main() -> None:
    """Выполнить тесты, примеры и исследование атрибутов функций."""
    test_core()
    print("ЗАДАНИЕ 3. Функции как объекты первого класса")
    print("apply_n(удвоение, 3, 1) =", apply_n(lambda value: value * 2, 3, 1))
    funcs = [lambda value: value + 1, lambda value: value * 2]
    print("apply_all([+1, *2], 3) =", apply_all(funcs, 3))
    for expression in (
        "12 + 4",
        "12 - 4",
        "12 * 4",
        "12 / 4",
        "2 ** 3",
        "13 % 4",
        "12 / 0",
        "12 % 0",
        "wrong",
    ):
        print(expression, "=", calculate(expression))
    even: Callable[[Sequence[int]], int] = make_counter_of(lambda value: value % 2 == 0)
    print("Количество чётных в [1, 2, 3, 4]:", even([1, 2, 3, 4]))
    for func in (apply_n, calculate, make_counter_of):
        print(f"__name__={func.__name__}; __defaults__={func.__defaults__}")
        print("__doc__:", func.__doc__)
    print("Проверки assert: 22/22 успешно.")


if __name__ == "__main__":
    main()
