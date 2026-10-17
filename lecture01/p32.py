"""Лекция 1, §3.2. Чистые и нечистые функции."""

from typing import TypeVar

T = TypeVar("T")


def add_vat(price: float, rate: float = 0.12) -> float:
    """Вернуть учебный расчёт цены с явно заданной ставкой."""
    return round(price * (1 + rate), 2)


rate = 0.12


def add_vat_impure(price: float) -> float:
    """Нечистая функция: читает изменяемую глобальную ставку."""
    return round(price * (1 + rate), 2)


def append_item(items: list[T], item: T) -> list[T]:
    """Нечистая функция: изменяет переданный список."""
    items.append(item)
    return items


if __name__ == "__main__":
    print("add_vat(1000) =", add_vat(1000))
    print("global rate=0.12:", add_vat_impure(1000))
    assert add_vat_impure(1000) == 1120.0
    rate = 0.2
    print("global rate=0.20:", add_vat_impure(1000))
    assert add_vat_impure(1000) == 1200.0
    assert add_vat(1000) == 1120.0
    assert add_vat(0) == 0
    items = [1, 2]
    result = append_item(items, 3)
    print("append_item:", items, "; тот же объект:", result is items)
    assert items == [1, 2, 3] and result is items
    print("Проверки: 5 assert, успешно.")
