def countable_nouns(num: int, tuple_str: tuple[str, str, str]) -> str:
    """Возвращает строку, которая согласуется с переданным аргументом num"""
    exception = [11, 12, 13, 14]
    # ИСПОЛЬЗОВАТЬ: могут быть использованы несколько раз
    last_digit = num % 10
    last_two_digits = num % 100

    if last_digit == 1 and last_two_digits not in exception:
        return tuple_str[0]
    elif last_digit in [2, 3, 4] and last_two_digits not in exception:
        return tuple_str[1]
    return tuple_str[2]


# >>> countable_nouns(14, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(24, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(451, ("год", "года", "лет"))
# 'год'


# ИТОГ: отлично — 3/3
