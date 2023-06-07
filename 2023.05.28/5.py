from pathlib import Path
from sys import path
from datetime import datetime as dt

def logger(function: 'callable') -> 'callable':
    """Выводит в стандартный поток журнал вызовов декорируемой функции. Записывает строки журнала вызовов в файл"""    
     
    file_path= Path(path[0]) / 'data/function_calls.log'
    
    def wrapper(*args, **kwargs) -> 'any':
        
        now = dt.now()
        now.strftime('%Y.%m.%d %H:%M:%S')
        # кортеж позиционных аргументов по умолчанию
        def_poz_arg = function.__defaults__
        def_key_arg = function.__kwdefaults__
        # получение позиционных параметров
        poz_arg = [str(arg) for arg in args]
        # получение ключевых параметров
        key_arg = {k:v for k, v in kwargs.items()}
        
        if def_key_arg != None and not [key for key in def_key_arg.keys() if key in key_arg]:
            key_arg |= def_key_arg
        if def_poz_arg != None:
            poz_arg += [str(i) for i in def_poz_arg]            
                
        print_log = (now.strftime('%Y.%m.%d %H:%M:%S') + ' - ' + 
                    f"{function.__name__}({', '.join(poz_arg + [f'{k}={v}' for k, v in key_arg.items()])}) -> "
                    )
                    
        
        try:
            result = function(*args, **kwargs)
        except Exception as inst:
            log_file = open(file_path, 'a', encoding='utf-8')
            log_file.write(print_log + f'{type(inst).__name__}: {str(inst)}\n')
            log_file.close()
            print(print_log + f'\n\t{type(inst).__name__}: {str(inst)}')
        else:
            log_file = open(file_path, 'a', encoding='utf-8')
            log_file.write(print_log + f'{result}\n')
            log_file.close()
            print(print_log + f'{result}')
            return result
            
    return wrapper
    
# C:\Users\ПК\Desktop\TOP\Git\repository\python\дз\Gorinov\2023.05.28
 # 22:18:26 > py -i 5.py
# >>> def calculation(num1, num2, *, digits = 2):
# ...     return num1 * num2 / digits
# ...
# >>> calculation = logger(calculation)
# >>> calculation(2,2)
# 2023.06.07 22:19:37 - calculation(2, 2, digits=2) -> 2.0
# 2.0
# >>> calculation(2,2, digits = 0)
# 2023.06.07 22:19:48 - calculation(2, 2, digits=0) ->
        # ZeroDivisionError: division by zero
# >>> ^Z

# C:\Users\ПК\Desktop\TOP\Git\repository\python\дз\Gorinov\2023.05.28
 # 22:19:52 > type data\function_calls.log
# 2023.06.07 22:19:37 - calculation(2, 2, digits=2) -> 2.0
# 2023.06.07 22:19:48 - calculation(2, 2, digits=0) -> ZeroDivisionError: division by zero