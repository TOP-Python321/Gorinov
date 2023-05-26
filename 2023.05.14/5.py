def central_tendency(arg_1: float, arg_2: float, /, *numbers: float) -> dict[str, float]:
    """Возвращает словарь, в котором: ключами являются меры центральной тенденции, а значения содержат результат вычислений """

    list_numbers = [arg_1, arg_2]
    list_numbers.extend(list(numbers))
    list_numbers.sort()    
    dict_out = {}
    
    if len(list_numbers) % 2:
        dict_out |= dict(median=float(list_numbers[len(list_numbers) // 2]))
    else:
        dict_out |= dict(median=(list_numbers[len(list_numbers) // 2] + list_numbers[len(list_numbers) // 2 - 1]) / 2)

    dict_out |= dict(arithmetic=sum(list_numbers) / len(list_numbers))

    multi = 1
    for num in list_numbers:      
        multi *= num

    dict_out |= dict(geometric=multi ** (1 / len(list_numbers)))
    dict_out |= dict(harmonic=len(list_numbers) / sum(1 / n for n in list_numbers))
    
    return dict_out


# >>> central_tendency(1,3, 4, 2)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>> central_tendency(1,3, 4, 2, 15, 120)
# {'median': 3.5, 'arithmetic': 24.166666666666668, 'geometric': 5.923530438729457, 'harmonic': 2.77992277992278}

