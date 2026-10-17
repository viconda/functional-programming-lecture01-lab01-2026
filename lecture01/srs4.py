"""СРС 4. Количество слов длиннее пяти символов.
Слово в основном варианте означает фрагмент между пробелами, как split().
Дополнительный вариант выделяет последовательности букв без пунктуации.
"""

import re


def count_imperative(text: str) -> int:
    """Подсчитать длинные фрагменты исходным циклом."""
    count = 0
    for word in text.split():
        if len(word) > 5:
            count += 1
    return count


def count_functional(text: str) -> int:
    """Подсчитать слова через sum и генераторное выражение."""
    return sum(1 for word in text.split() if len(word) > 5)


def count_letters_only(text: str) -> int:
    """Подсчитать буквенные слова, исключив цифры, знаки и underscore."""
    return sum(1 for word in re.findall(r"[^\W\d_]+", text) if len(word) > 5)


if __name__ == "__main__":
    text = "Python помогает писать понятные функции без лишних изменений"
    selected = [word for word in text.split() if len(word) > 5]
    print("Текст:", text)
    print("Слова длиннее 5:", selected)
    print("Цикл:", count_imperative(text), "; функционально:", count_functional(text))
    print(
        "Пунктуация: 'слово!' split =",
        count_functional("слово!"),
        "; только буквы =",
        count_letters_only("слово!"),
    )
    assert count_functional(text) == 7
    assert count_functional("") == 0
    assert count_functional("слово") == 0
    assert count_functional("шестой") == 1
    assert count_functional("  python\tфункция\nкод ") == 2
    assert all(
        count_functional(s) == count_imperative(s)
        for s in (text, "", "слово", "шестой", "слово!")
    )
    assert count_letters_only("слово! функция, Python.") == 2
    print("Проверки: 7 assert, успешно.")
