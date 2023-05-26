# ПЕРЕИМЕНОВАТЬ: arg_1 и arg_2 — не абстрактные аргументы, а вполне конкретные
def central_tendency(arg_1: float, arg_2: float, /, *numbers: float) -> dict[str, float]:
    """Возвращает словарь, в котором: ключами являются меры центральной тенденции, а значения содержат результат вычислений """
    # ИСПОЛЬЗОВАТЬ: все эти действия прекрасно заменяются на одну строчку кода
    # list_numbers = [arg_1, arg_2]
    # list_numbers.extend(list(numbers))
    # list_numbers.sort()
    # ПЕРЕИМЕНОВАТЬ: более того, нет никакой необходимости создавать новую переменную — ведь кортеж numbers в своём исходном виде никак более не используется
    list_numbers = sorted((arg_1, arg_2) + numbers)
    dict_out = {}
    
    if len(list_numbers) % 2:
        dict_out |= dict(median=float(list_numbers[len(list_numbers) // 2]))
        # ИСПОЛЬЗОВАТЬ: есть такая штука, насчёт литералов — их в коде лучше использовать по минимуму (я буду говорить об этом, правда много позже) — но если вы оформляете код как в строчке выше, то этот параметр никак не заменить на перечислитель, или ещё на что-то — поэтому таким способом на самом деле пользуются довольно ограничено, а более полезной практикой является вот такое оформление:
        # dict_out |= {'median': float(list_numbers[i_half])}
    else:
        # ИСПРАВИТЬ: уже второе вычисление длины списка должно было побудить вас сохранить эту длину в отдельную переменную
        # ИСПРАВИТЬ: то же самое касается и индекса середины списка
        dict_out |= dict(median=(list_numbers[len(list_numbers) // 2] + list_numbers[len(list_numbers) // 2 - 1]) / 2)

    dict_out |= dict(arithmetic=sum(list_numbers) / len(list_numbers))
    multi = 1
    for num in list_numbers:      
        multi *= num
    dict_out |= dict(geometric=multi ** (1 / len(list_numbers)))
    dict_out |= dict(harmonic=len(list_numbers) / sum(1 / n for n in list_numbers))
    # СДЕЛАТЬ: подумайте, как ещё можно реализовать вычисление этих трёх мер
    
    return dict_out


# >>> central_tendency(1,3, 4, 2)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>> central_tendency(1,3, 4, 2, 15, 120)
# {'median': 3.5, 'arithmetic': 24.166666666666668, 'geometric': 5.923530438729457, 'harmonic': 2.77992277992278}


# ИТОГ: хорошо, но можно лучше — 4/7
