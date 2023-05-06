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

print(sum(scores + k for i in text.upper() for k, v in scores_letters.items() if i in v))

# тоже самое через цикл
# for i in text.upper():
  
    # for k, v in scores_letters.items():
        # if i in v:
            # scores += k
            
# Введите слово: Питон

# 6