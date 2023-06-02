# ДОБАВИТЬ: аннотацию параметра
def strong_password(text: str) -> bool:
    """Возвращает объект True - если пароль соответствует требованиям, False - если не соответствует"""
    set_up = {chr(code) for code in range(65, 91)}
    set_low = {chr(code) for code in range(97, 123)}
    # ИСПОЛЬЗОВАТЬ: не то чтобы я был против генераторных выражений, но есть и более очевидное решение =)
    # set_int = {chr(code) for code in range(48, 58)}
    set_int = set('0123456789')
    set_text = set(text)

    # ИСПРАВИТЬ: вот это длинное выражение в круглых скобках — оно при вычислении какие объекты возвращает?
    if (
            len(text) >= 8
        and set_text & set_up
        # ИСПРАВИТЬ: многократное вычисление множества символов пароля — неоптимально
        and set_text & set_low
        # проверка на наличие любых прочих символов
        # ИСПРАВИТЬ: пересечение лишнее — достаточно из множества символов пароля вычесть все множества категорий
        and set_text - set_up - set_low - set_int
        and len([char for char in text if char in set_int]) >= 2
    ):
        return bool(True)
    return bool(False)


# >>> strong_password('Ar3kHl3!')
# True

# >>> strong_password('ar3khl3!')
# False


# ИТОГ: хорошо, немного доработать — 2/4
