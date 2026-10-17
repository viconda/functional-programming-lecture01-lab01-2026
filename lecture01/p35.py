"""Лекция 1, §3.5. Изменение списка и создание нового кортежа."""

if __name__ == "__main__":
    scores = [70, 85, 90]
    alias = scores
    scores.append(100)
    scores_t: tuple[int, ...] = (70, 85, 90)
    new_scores = scores_t + (100,)
    print("Список:", scores)
    print("Ссылка alias видит изменение:", alias)
    print("Исходный кортеж:", scores_t)
    print("Новый кортеж:", new_scores)
    assert alias is scores and alias == [70, 85, 90, 100]
    assert scores_t == (70, 85, 90)
    assert new_scores == (70, 85, 90, 100)
    assert id(new_scores) != id(scores_t)
    print("Проверки: 4 assert, успешно.")
