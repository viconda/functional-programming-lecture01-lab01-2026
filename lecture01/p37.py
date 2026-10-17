"""Лекция 1, §3.7. Рекурсивная сумма."""


def total(numbers: list[int]) -> int:
    """Сложить элементы небольшого списка без изменения аргумента."""
    if not numbers:
        return 0
    return numbers[0] + total(numbers[1:])


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    print("total([1, 2, 3, 4, 5]) =", total(values))
    print("total([]) =", total([]))
    print("total([-5, 2, 3]) =", total([-5, 2, 3]))
    assert total(values) == 15
    assert total([]) == 0
    assert total([-5, 2, 3]) == 0
    assert values == [1, 2, 3, 4, 5]
    print("Проверки: 4 assert, успешно.")
