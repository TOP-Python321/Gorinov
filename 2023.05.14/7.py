def to_ten(num: str, int_1: int) -> int:
    """Возвращает переданную строку в десятеричной системе исчисления"""
    dict_num = dict(zip(
        [str(n) for n in range(0, 10)] + [str(chr(c)) for c in range(97, 123)],
        [i for i in range(0, 36)]
    ))
    num_10 = 0
    n = len(num) - 1  
    
    for i in num:        
        num_10 += (dict_num[i]) * (int_1**n)
        n -= 1

    return num_10
    
    
def to_base(num: int, int_1: int) -> str:
    """Возвращает переданное число из десятеричной системы исчисления в любую другую систему исчисления."""
    dict_num = dict(zip(
        [str(n) for n in range(0, 10)] + [str(chr(c)) for c in range(97, 123)],
        [i for i in range(0, 36)]
    ))
    num_out = []
    
    while True:
        reminder = int(num) % int_1
        num = int(num) // int_1       
        num_out.append(reminder)
        if num < int_1:
            num_out.append(num)
            break
    num_out.reverse()
    
    str_out = []
    for rem in num_out:
        for k, v in dict_num.items():
            if rem == v:
                str_out.append(k)
                break
    return ''.join(str_out)     
    
    
def int_base(num: str, arg1: int, arg2: int) -> str | None:
    """Возвращает переданный параметр (num) из системы исчисления указанной параметром (arg1) 
       в систему исчисления указанной в параметре (arg2). Функция работает с системами исчисления от 2 до 36."""
    list_num = [str(n) for n in range(0, 10)] + [str(chr(c)) for c in range(97, 123)]
    if 2 <= arg1 <= 36 and 2 <= arg2 <= 36 and not ''.join(c for c in num.lower() if c in list_num[arg1:]):
        return to_base((to_ten(num.lower(), arg1)), arg2)


# >>> print(int_base('0100129', 9, 36))
# None
# >>> print(int_base('0100128', 7, 36))
# None
# >>> print(int_base('0100128', 9, 36))
# 19n8
# >>> int_base('0100128', 9, 36)
# '19n8'
# >>> int_base('01001j3028', 30, 5)
# '41222233240133233'
