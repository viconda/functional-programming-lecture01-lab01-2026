"""Лекция 1, §3.6. Оператор if и условное выражение."""


def parity_statement(n: int) -> str:
    """Определить чётность при помощи оператора if."""
    if n % 2 == 0:
        parity = "чётное"
    else:
        parity = "нечётное"
    return parity


def parity_expression(n: int) -> str:
    """Определить чётность одним условным выражением."""
    return "чётное" if n % 2 == 0 else "нечётное"


if __name__ == "__main__":
    for n in (7, 8, 0, -3):
        print(n, ":", parity_statement(n), "=", parity_expression(n))
    assert parity_expression(7) == "нечётное"
    assert parity_expression(0) == "чётное"
    assert parity_statement(-3) == "нечётное"
    assert all(parity_statement(n) == parity_expression(n) for n in range(-10, 11))
    print("Проверки: 4 assert, включая 21 сравнение, успешно.")
