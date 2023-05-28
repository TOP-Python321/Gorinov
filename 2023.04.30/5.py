scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

text = input('Введите слово: ').upper()

text = text.replace('Ё', 'Е')


print(sum(
    # ИСПРАВИТЬ: в генераторном выражении значение scores на каждой итерации будет равно нулю
    # КОММЕНТАРИЙ: если вы подразумевали, что значение scores будет меняться, то это двойная ошибка:
    #  1) int объекты являются неизменяемыми;
    #  2) если бы были изменяемыми и вы бы как-то прописали это изменение на каждой итерации, то каждое число, возвращаемое генератором во время итерации, содержало бы сумму всех предыдущих очков и очки за очередную букву — а потом все эти числа вы ещё снаружи суммируете функцией sum() — итог вышел бы сильно больше ожидаемого числа
    # первое решение было через цикл и по невнимательности scores + score перенес в генераторное выражение.
    score
    for char in text.upper() for score, letters in scores_letters.items()
    if char in letters
))

# тоже самое через цикл
# for char in text.upper():
    # for score, letters in scores_letters.items():
        # if char in letters:
            # КОММЕНТАРИЙ: не переносите выражения напрямую из явного цикла в генераторное выражение — они могут работать по-разному
            # scores += score


# Введите слово: Питон
# 6


# ИТОГ: хорошо, но требует осмысления — 4/6
