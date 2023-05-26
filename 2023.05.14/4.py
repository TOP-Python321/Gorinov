def countable_nouns(num: int, tuple_str: tuple[str, str, str]) -> str:
    """Возвращает строку, которая согласуется с переданным аргументом num"""
    exception = [11, 12, 13, 14]
    if num % 10 == 1 and num % 100 not in exception:
        return tuple_str[0]
    elif num % 10 in [2, 3, 4] and num % 100 not in exception:
        return tuple_str[1]
    return tuple_str[2]


# >>> countable_nouns(14, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(24, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(451, ("год", "года", "лет"))
# 'год'

