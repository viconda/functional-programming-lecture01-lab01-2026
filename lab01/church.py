"""Дополнительное задание. Все семь вычислительных определений используют lambda.

Число Чёрча n применяет переданную функцию к начальному значению n раз.
Область from_int: целые неотрицательные числа. Для 0**0 принято значение 1.
Императивные проверки и печать вынесены в отдельные служебные функции.
"""

# Присваивание lambda требуется условием дополнительного задания.

from collections.abc import Callable
from typing import Any

Church = Callable[[Callable[[Any], Any]], Callable[[Any], Any]]

zero: Church = lambda f: lambda x: x
succ: Callable[[Church], Church] = lambda n: lambda f: lambda x: f(n(f)(x))
plus: Callable[[Church], Callable[[Church], Church]] = lambda m: (
    lambda n: lambda f: lambda x: m(f)(n(f)(x))
)
mult: Callable[[Church], Callable[[Church], Church]] = lambda m: (
    lambda n: lambda f: m(n(f))
)
power: Callable[[Church], Callable[[Church], Church]] = lambda base: (
    lambda exponent: exponent(base)
)
to_int: Callable[[Church], int] = lambda n: n(lambda value: value + 1)(0)
from_int: Callable[[int], Church] = lambda n: zero if n == 0 else succ(from_int(n - 1))

zero.__doc__ = "Применить функцию ноль раз."
succ.__doc__ = "Создать следующее число Чёрча."
plus.__doc__ = "Создать сумму двух чисел Чёрча."
mult.__doc__ = "Создать произведение двух чисел Чёрча."
power.__doc__ = "Возвести первое число Чёрча в степень второго."
to_int.__doc__ = "Преобразовать число Чёрча в int применением +1 к нулю."
from_int.__doc__ = "Преобразовать целое неотрицательное n в число Чёрча."


def test_core() -> None:
    """Проверить все семь определений минимум двумя утверждениями."""
    assert zero(lambda value: value + 1)(10) == 10
    assert zero(str.upper)("text") == "text"
    assert to_int(succ(zero)) == 1
    assert to_int(succ(from_int(4))) == 5
    assert to_int(plus(from_int(2))(from_int(3))) == 5
    assert to_int(plus(zero)(from_int(3))) == 3
    assert to_int(mult(from_int(3))(from_int(4))) == 12
    assert to_int(mult(zero)(from_int(4))) == 0
    assert to_int(power(from_int(2))(from_int(3))) == 8
    assert to_int(power(from_int(3))(zero)) == 1
    assert to_int(zero) == 0
    assert to_int(succ(succ(zero))) == 2
    assert from_int(3)(str.upper)("text") == "TEXT"
    assert from_int(0)(lambda value: value + 1)(5) == 5
    assert to_int(power(zero)(zero)) == 1


def main() -> None:
    """Запустить проверки и напечатать результаты арифметики Чёрча."""
    test_core()
    print("ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ. Числа Чёрча")
    print("zero =", to_int(zero))
    print("succ(4) =", to_int(succ(from_int(4))))
    print("plus(2)(3) =", to_int(plus(from_int(2))(from_int(3))))
    print("mult(3)(4) =", to_int(mult(from_int(3))(from_int(4))))
    print("power(2)(3) =", to_int(power(from_int(2))(from_int(3))))
    print("power(3)(0) =", to_int(power(from_int(3))(zero)))
    print("Преобразование from_int(5), затем to_int:", to_int(from_int(5)))
    print("Проверки assert: 15/15 успешно.")


if __name__ == "__main__":
    main()
