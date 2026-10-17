"""Лекция 1, §5. Лямбда-исчисление, каррирование и числа Чёрча."""

from collections.abc import Callable
from typing import Any

Church = Callable[[Callable[[Any], Any]], Callable[[Any], Any]]
inc: Callable[[int], int] = lambda x: x + 1
inc.__doc__ = "Вернуть следующее целое число."
add: Callable[[int], Callable[[int], int]] = lambda x: lambda y: x + y
add.__doc__ = "Вернуть чистую функцию прибавления x."
zero: Church = lambda f: lambda x: x
zero.__doc__ = "Число Чёрча 0: не применять f."
succ: Callable[[Church], Church] = lambda n: lambda f: lambda x: f(n(f)(x))
succ.__doc__ = "Вернуть следующее число Чёрча."
to_int: Callable[[Church], int] = lambda n: n(lambda k: k + 1)(0)
to_int.__doc__ = "Преобразовать число Чёрча в целое число."

if __name__ == "__main__":
    print("Бета-редукция (lambda x: x + 1)(4) =", (lambda x: x + 1)(4))
    add5 = add(5)
    print("add5(10) =", add5(10))
    three = succ(succ(succ(zero)))
    print("to_int(three) =", to_int(three))
    assert inc(4) == 5
    assert add5(10) == 15
    assert to_int(zero) == 0
    assert to_int(three) == 3
    print("Проверки: 4 assert, успешно.")
