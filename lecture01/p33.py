"""Лекция 1, §3.3. Изоляция побочных эффектов."""

from contextlib import redirect_stdout
from io import StringIO


def total_price(prices: tuple[float, ...]) -> float:
    """Чистое ядро: вычислить сумму без вывода и изменения данных."""
    return round(sum(prices), 2)


def format_total(total: float) -> str:
    """Чистое ядро: подготовить текст, не печатая его."""
    return f"Итого: {total:.2f}"


def show_total(prices: tuple[float, ...]) -> None:
    """Императивная оболочка: вывести результат вычисления."""
    print(format_total(total_price(prices)))


if __name__ == "__main__":
    prices = (100.0, 250.0, 50.0)
    show_total(prices)
    assert total_price(prices) == 400.0
    assert total_price(()) == 0.0
    assert prices == (100.0, 250.0, 50.0)
    captured = StringIO()
    with redirect_stdout(captured):
        # Для учебной проверки намеренно сохраняем возврат None.
        returned = show_total(prices)  # type: ignore[func-returns-value]
    assert captured.getvalue() == "Итого: 400.00\n"
    assert returned is None
    print("Чистые функции возвращают данные; оболочка выполняет print.")
    print("Проверки: 5 assert, успешно.")
