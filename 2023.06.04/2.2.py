from functools import wraps
from time import sleep
from typing import Any

def exception_delay_repeat(function) -> Any|None:
    """
    Повторяет через полсекунды вызов декорируемой функции в случае возникновения исключения.
    В случае повторного исключения выводит в stdout имя класса исключения и текст исключения.
    Иначе возвращает значение декорируемой функции.
    """
    retry: int = 2
    @wraps(function)
    def wrapper(*args, **kwargs):
        nonlocal retry  
        while retry:      
            try:
                return function(*args, **kwargs)
            except Exception as e:                
                    sleep(0.5)
                    retry -=1
                    if not retry:                    
                        print(f'{type(e).__name__}: {str(e)}')
                        # если необходим повторный вызов после ошибки
                        # retry = 2
                        # return None                        
    return wrapper
    
# >>> from random import randrange
# >>> def test_func():
# ...     if randrange(2):
# ...             raise ConnectionError('failure')
# ...     else:
# ...             return 'success'
# >>>
# >>> test_func
# <function test_func at 0x0000027C44A15DA0>
# >>> test_func = exception_delay_repeat(test_func)
# >>> test_func
# <function test_func at 0x0000027C44A8DC60>
# >>> test_func()
# 'success'
# >>> test_func()
# 'success'
# >>> test_func()
# 'success'
# >>> test_func()
# 'success'
# >>> test_func()
# 'success'
# >>> test_func()
# ConnectionError: failure
# >>> test_func()