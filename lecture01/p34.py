"""Лекция 1, §3.4. Ссылочная прозрачность и случайность."""

import random

from p31 import square


def roll() -> int:
    """Нечистый бросок: читает и изменяет состояние генератора."""
    return random.randint(1, 6)


if __name__ == "__main__":
    print("square(4) + square(4) =", square(4) + square(4))
    print("16 + 16 =", 16 + 16)
    assert square(4) + square(4) == 16 + 16
    random.seed(42)  # Фиксируем реальный генератор для воспроизводимости.
    first, second = roll(), roll()
    random.seed(42)
    single = roll()
    print("Два броска:", first, second, "; сумма:", first + second)
    print("Один бросок:", single, "; удвоение:", 2 * single)
    assert first == single
    assert all(1 <= x <= 6 for x in (first, second, single))
    possible_sum = {a + b for a in range(1, 7) for b in range(1, 7)}
    possible_double = {2 * a for a in range(1, 7)}
    print("Все суммы:", sorted(possible_sum))
    print("Все удвоения:", sorted(possible_double))
    assert possible_sum == set(range(2, 13))
    assert possible_double == {2, 4, 6, 8, 10, 12}
    assert possible_sum != possible_double
    print("Проверки: 6 assert, успешно.")
