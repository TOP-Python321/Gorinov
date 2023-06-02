# ПЕРЕИМЕНОВАТЬ: arg_1 и arg_2 — не абстрактные аргументы, а вполне конкретные
def central_tendency(num_1: float, num_2: float, /, *numbers: float) -> dict[str, float]:
    """Возвращает словарь, в котором: ключами являются меры центральной тенденции, а значения содержат результат вычислений """
    # ИСПОЛЬЗОВАТЬ: все эти действия прекрасно заменяются на одну строчку кода
    # numbers = [num_1, num_2]
    # numbers.extend(list(numbers))
    # numbers.sort()
    # ПЕРЕИМЕНОВАТЬ: более того, нет никакой необходимости создавать новую переменную — ведь кортеж numbers в своём исходном виде никак более не используется
    
    
    numbers = sorted((num_1, num_2) + numbers)
    
    dict_out = {}
    len_numbers = len(numbers)
    center_len_numbers = len_numbers // 2
    
    if len_numbers % 2:
        dict_out |= {'median':float(numbers[center_len_numbers])}
        # ИСПОЛЬЗОВАТЬ: есть такая штука, насчёт литералов — их в коде лучше использовать по минимуму (я буду говорить об этом, правда много позже) — но если вы оформляете код как в строчке выше, то этот параметр никак не заменить на перечислитель, или ещё на что-то — поэтому таким способом на самом деле пользуются довольно ограничено, а более полезной практикой является вот такое оформление:
        # dict_out |= {''median'': float(numbers[i_half])}
    else:
        # ИСПРАВИТЬ: уже второе вычисление длины списка должно было побудить вас сохранить эту длину в отдельную переменную
        # ИСПРАВИТЬ: то же самое касается и индекса середины списка
        dict_out |= {'median':(numbers[center_len_numbers] + numbers[center_len_numbers - 1]) / 2}

    # dict_out |= {'arithmetic':sum(numbers) / len_numbers}
    # multi = 1
    # for num in numbers:      
        # multi *= num
    # dict_out |= {'geometric':multi ** (1 / len_numbers)}
    # dict_out |= {'harmonic':len_numbers / sum(1 / n for n in numbers)}
    # СДЕЛАТЬ: подумайте, как ещё можно реализовать вычисление этих трёх мер
    sum_num = 0
    count = 0
    multi = 1
    sum_divisor = 0
    for i in numbers:
        sum_num += i        
        count += 1        
        multi *= i        
        sum_divisor += 1 / i
        
    dict_out |= {'arithmetic':sum_num / count}
    dict_out |= {'geometric':multi ** (1 / count)}
    dict_out |= {'harmonic':count / sum_divisor}
    
    return dict_out


# >>> central_tendency(1,3, 4, 2)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>> central_tendency(1,3, 4, 2, 15, 120)
# {'median': 3.5, 'arithmetic': 24.166666666666668, 'geometric': 5.923530438729457, 'harmonic': 2.77992277992278}


# ИТОГ: хорошо, но можно лучше — 4/7
