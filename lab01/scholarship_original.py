"""Буквальный нечистый пример стипендии из лабораторного материала.

Globals, изменение словаря и печать оставлены для воспроизведения примера.
После исходных операций main дополнительно показывает содержимое журнала.
"""

BASE = 50_000
log = []


def calc_scholarship(student):
    global BASE
    avg = sum(student["grades"]) / len(student["grades"])
    if avg >= 90:
        amount = BASE * 1.5
    elif avg >= 75:
        amount = BASE
    else:
        amount = 0
    student["scholarship"] = amount          # изменение аргумента
    log.append(student["name"])              # изменение глобального списка
    print(student["name"], amount)           # вывод
    return amount


def main() -> None:
    """Выполнить исходный пример и показать наблюдаемые изменения."""
    print("ПРИМЕР. Исходный нечистый расчёт стипендии")
    s = {"name": "Аружан", "grades": [92, 88, 95]}
    calc_scholarship(s)
    print(s)
    print("Глобальный журнал log:", log)


if __name__ == "__main__":
    main()
