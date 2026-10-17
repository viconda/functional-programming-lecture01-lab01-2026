"""Сборка проверок лабораторной обычной командой pytest lab01."""

import church
import scholarship
import task1
import task2
import task3
import task4
import task5


def test_task1() -> None:
    """Проверить исправленные чистые функции задания 1."""
    task1.test_core()


def test_task2() -> None:
    """Проверить функциональное ядро интернет-магазина."""
    task2.test_core()


def test_task3() -> None:
    """Проверить функции высшего порядка и калькулятор."""
    task3.test_core()


def test_task4() -> None:
    """Проверить индивидуальный вариант успеваемости."""
    task4.test_core()


def test_task5() -> None:
    """Проверить эвристику и мутацию возвращаемого объекта."""
    task5.test_core()


def test_scholarship() -> None:
    """Проверить практический пример расчёта стипендии."""
    scholarship.test_core()


def test_church() -> None:
    """Проверить семь lambda-определений чисел Чёрча."""
    church.test_core()
