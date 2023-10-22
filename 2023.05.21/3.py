def math_function_resolver(
        function: 'callable',
        /,
        # ИСПРАВИТЬ: для произвольного кортежа аргументов всегда аннотируется сразу тип элементов
        *numbers: tuple[int | float],
        strings: bool = False
) -> list[str | float]:
    """Вычисляет округленные значения математических функций и возвращает список с вычисленными значениями.

    :param function: вызываемая функция, имеет строго позиционный аргумент. Принимает один позиционно - ключевой аргумент и вычисляет значение математической функции.
    :param numbers: позиционный аргумент. Передается кортеж из int или float объектов.
    :param strings: ключевой аргумент, передается в виде объекта bool. Значение по умолчанию False - возвращает значения float, True - возвращает значение str.
    :return: возвращает список с вычисленными значениями математической функции.
    """
    list_result = []
    for item in numbers:
        result = round(function(item), 2)
        list_result += [float(result)] if not strings else [str(result)]
    return list_result


# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), strings=True)
# ['2.72', '7.4', '20.12', '54.74', '148.88', '404.96', '1101.49', '2996.07', '8149.3']

# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]

# >>> math_function_resolver(lambda x: 5*x / 5, *range(1, 10))
# [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

# >>> math_function_resolver(lambda x: 5*x / 5, *range(1, 10), strings = True)
# ['1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0']


# ИТОГ: хорошо — 4/5
