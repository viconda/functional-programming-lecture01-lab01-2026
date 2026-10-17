"""Задание 2. Функциональное ядро расчёта заказа."""

from collections.abc import Sequence

Item = tuple[str, float, int]


def subtotal(cart: Sequence[Item]) -> float:
    """Рассчитать стоимость товаров до скидки и доставки."""
    if any(price < 0 or quantity < 0 for _, price, quantity in cart):
        raise ValueError("Цена и количество не могут быть отрицательными")
    return sum(price * quantity for _, price, quantity in cart)


def discount_amount(total: float, discount_card: bool) -> float:
    """Вернуть скидку 5 процентов при наличии карты."""
    return total * 0.05 if discount_card else 0.0


def discounted_total(total: float, discount_card: bool) -> float:
    """Вернуть сумму после скидки."""
    return total - discount_amount(total, discount_card)


def delivery_cost(total_after_discount: float) -> float:
    """Доставка стоит 1500 тг, если сумма после скидки меньше 30000 тг."""
    return 1500.0 if total_after_discount < 30_000 else 0.0


def order_total(cart: Sequence[Item], discount_card: bool) -> float:
    """Рассчитать итог, сохранив правило доставки из исходного кода."""
    goods = discounted_total(subtotal(cart), discount_card)
    return goods + delivery_cost(goods)


def test_core() -> None:
    """Проверить функции, границу доставки и неизменность корзины."""
    cart = [("Клавиатура", 15_000, 1), ("Мышь", 6000, 2), ("Коврик", 2500, 3)]
    original = cart.copy()
    assert subtotal(cart) == 34_500
    assert subtotal([]) == 0
    assert discount_amount(34_500, True) == 1725
    assert discount_amount(34_500, False) == 0
    assert discounted_total(34_500, True) == 32_775
    assert discounted_total(34_500, False) == 34_500
    assert delivery_cost(29_999) == 1500
    assert delivery_cost(30_000) == 0
    assert order_total(cart, True) == 32_775
    assert order_total([("Товар", 10_000, 1)], False) == 11_500
    assert cart == original
    assert order_total(cart, True) == order_total(cart, True)
    assert order_total([], False) == 1500


def main() -> None:
    """Выполнить тесты и вывести расчёт заказа."""
    test_core()
    cart = [("Клавиатура", 15_000, 1), ("Мышь", 6000, 2), ("Коврик", 2500, 3)]
    original = cart.copy()
    goods = subtotal(cart)
    after_discount = discounted_total(goods, True)
    print("ЗАДАНИЕ 2. Интернет-магазин")
    print("Корзина:", cart)
    print(f"Товары: {goods:.2f} тг")
    print(f"Скидка 5%: {discount_amount(goods, True):.2f} тг")
    print(f"После скидки: {after_discount:.2f} тг")
    print(f"Доставка: {delivery_cost(after_discount):.2f} тг")
    print(f"К оплате: {order_total(cart, True):.2f} тг")
    print("Повторный расчёт:", order_total(cart, True))
    print("Исходная корзина не изменилась:", cart == original)
    print("Граница доставки: 29999 ->", delivery_cost(29_999))
    print("Граница доставки: 30000 ->", delivery_cost(30_000))
    print("Проверки assert: 13/13 успешно.")


if __name__ == "__main__":
    main()
