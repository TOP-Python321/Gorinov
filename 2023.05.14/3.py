def numbers_strip(list_int: list[float], n_num: int = 1, *, copy: bool = False) -> list:

    """Возвращает исходный объект списка с изменениями или измененную копию исходного списка"""
    

    while n_num > 0:
        del list_int[(list_int.index(max(list_int)))], list_int[(list_int.index(min(list_int)))]        
        n_num -= 1
    
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