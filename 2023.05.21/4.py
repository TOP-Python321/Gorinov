def repeat(function: 'callable') -> 'callable':
    """Возвращает декорируемую функцию 10 раз"""
    def wrapper (*args, **kwargs) -> 'any':    
        for _ in range(10):
            function(*args, **kwargs)        
    return wrapper
    
# >> def multi(num1, num2):
# ...     return print(num1 * num2)
# ...
# >>> multi = repeat(multi)
# >>> multi(2, 6)
# 12
# 12
# 12
# 12
# 12
# 12
# 12
# 12
# 12
# 12