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
scores = 0

print(sum(
    scores + score
    for char in text.upper() for score, letters in scores_letters.items()
    if char in letters
))

# тоже самое через цикл
# for char in text.upper():
    # for score, letters in scores_letters.items():
        # if char in letters:
            # scores += score


# Введите слово: Питон
# 6

