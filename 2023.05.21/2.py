def deck() -> 'generator':
    """Возвращает объект генератор, который формирует упорядоченную колоду карт"""
    for suit in ["черви", "бубны", "пики", "трефы"]:
        for val in range(2, 15):             
             yield (val, suit)

# >>> list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
# >>> list(deck())[::-13]
# [(14, 'трефы'), (14, 'пики'), (14, 'бубны'), (14, 'черви')]
# >>> list(deck())[:6]
# [(2, 'черви'), (3, 'черви'), (4, 'черви'), (5, 'черви'), (6, 'черви'), (7, 'черви')]