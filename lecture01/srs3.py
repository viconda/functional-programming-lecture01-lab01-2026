"""СРС 3. Сложение чисел Чёрча без преобразования в int внутри plus."""

from collections.abc import Callable

from p5 import Church, succ, to_int, zero

plus: Callable[[Church], Callable[[Church], Church]] = lambda m: (
    lambda n: lambda f: lambda x: m(f)(n(f)(x))
)
plus.__doc__ = "Вернуть число Чёрча m+n: сначала n, затем m применений f."

if __name__ == "__main__":
    one = succ(zero)
    two = succ(one)
    three = succ(two)
    print("to_int(plus(two)(three)) =", to_int(plus(two)(three)))
    print("to_int(plus(zero)(three)) =", to_int(plus(zero)(three)))
    print("to_int(plus(three)(zero)) =", to_int(plus(three)(zero)))
    print("to_int(plus(zero)(zero)) =", to_int(plus(zero)(zero)))
    assert to_int(plus(two)(three)) == 5
    assert to_int(plus(zero)(three)) == 3
    assert to_int(plus(three)(zero)) == 3
    assert to_int(plus(zero)(zero)) == 0
    assert to_int(plus(three)(two)) == 5
    assert plus(two)(three)(lambda s: s + "*")("") == "*****"
    print("Проверки: 6 assert, включая нечисловое применение f, успешно.")
