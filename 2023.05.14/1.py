def strong_password(text) -> bool:
    """Возвращает объект bool: True - если пароль соответствует требованиям, False - не соответствует"""
    set_up = {chr(code) for code in range(65, 91)}
    set_low = {chr(code) for code in range(97, 123)}
    set_int = {chr(code) for code in range(48, 58)}
    
    if (
            len(text) >= 8
        and set(text) & set_up
        and set(text) & set_low
        # проверка на наличие любых прочих символов
        and set(text) - (set(text) & (set_up | set_low | set_int))
        and len([char for char in text if char in set_int]) >= 2
    ):
        return True
    return False


# >>> strong_password('Ar3kHl3!')
# True

# >>> strong_password('ar3khl3!')
# False

