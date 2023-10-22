def logger(function: 'callable') -> 'callable':
    """Выводит в стандартный поток журнал вызовов декорируемой функции"""
    def wrapper(*args, **kwargs) -> 'any':
        # кортеж позиционных аргументов по умолчанию
        def_poz_arg = function.__defaults__
        def_key_arg = function.__kwdefaults__
        # получение позиционных параметров
        poz_arg = [str(arg) for arg in args]
        # получение ключевых параметров
        key_arg = {k:v for k, v in kwargs.items()}

        # ИСПРАВИТЬ: проверку на None проводим с помощью операторов is и is not
        if def_key_arg != None and not [key for key in def_key_arg.keys() if key in key_arg]:
            key_arg |= def_key_arg
        if def_poz_arg != None:
            poz_arg += [str(i) for i in def_poz_arg]            
                
        print_log = f"{function.__name__}({', '.join(poz_arg + [f'{k}={v}' for k, v in key_arg.items()])}) -> "
        
        try:
            result = function(*args, **kwargs)
        except Exception as inst:
            print(print_log + f'\n\t{type(inst).__name__}: {str(inst)}')
        else:
            print(print_log + f'{result}')
            return result
            
    return wrapper


# >>> def calculation(num1, num2, digits = 2):
# ...     return num1 * num2 / digits
# ...
# >>> calculation = logger(calculation)
# >>> calculation(2,2)
# calculation(2, 2, 2) -> 2.0
# 2.0

# >>> def calculation(num1, num2, *, digits = 2):
# ...     return num1 * num2 / digits
# ...
# >>> calculation = logger(calculation)
# >>> calculation(2,2)
# calculation(2, 2, digits=2) -> 2.0
# 2.0
# >>>
# >>> calculation(2,2, digits = 0)
# calculation(2, 2, digits=0) ->
        # ZeroDivisionError: division by zero
# >>>
# >>> calculation(2,2, digits = '1')
# calculation(2, 2, digits=1) ->
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
# >>>
# >>> calculation(num1 = 2, num2 = 4, digits = 2)
# calculation(num1=2, num2=4, digits=2) -> 4.0
# 4.0

# КОММЕНТАРИЙ: мало сценариев объявления и вызова декорируемой функции рассмотрено

# СДЕЛАТЬ: изучите пример, запустите тестовые функции со своей реализацией декоратора, найдите ошибки


# ИТОГ: хорошо, но можно лучше — 4/7
