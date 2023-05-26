def numbers_strip(list_int: list[float], n_num: int = 1, *, copy: bool = False) -> list:
    """Возвращает исходный объект списка с изменениями или измененную копию исходного списка"""
    while n_num > 0:
        # КОММЕНТАРИЙ: инструкция del изменяет список, к которому применяется
        del list_int[(list_int.index(max(list_int)))], \
            list_int[(list_int.index(min(list_int)))]
        n_num -= 1
    # ИСПРАВИТЬ: поэтому при постфактум проверке, даже если copy=True, вы уже изменили исходный список (см. пример ниже)
    if not copy:
        return list_int
    return list_int.copy()


# >>> list_int = [i for i in range(10, 150, 8)]
# >>> print(list_int)
# [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98, 106, 114, 122, 130, 138, 146]
# >>> list_int_stripped = numbers_strip(list_int, 5)
# >>> list_int_stripped
# [50, 58, 66, 74, 82, 90, 98, 106]
# >>> list_int is  list_int_stripped
# True

# list_int = [1, 2, 4, 8, 3]
# >>> list_int_stripped = numbers_strip(list_int, copy=True)
# >>> list_int_stripped
# [2, 4, 3]
# >>> list_int is list_int_stripped
# False

# >>> list_int = [1, 2, 3, 4, 5]
# >>> list_int_stripped = numbers_strip(list_int, 2, copy=True)
# >>> list_int_stripped
# [3]
# КОММЕНТАРИЙ: при copy=True этот список должен остаться неизменным
# >>> list_int
# [3]


# ИТОГ: доработать — 2/4
