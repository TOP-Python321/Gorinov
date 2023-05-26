# КОММЕНТАРИЙ: вообще, впечатление, что эту задачу писали под утро после бессонной ночи )) если так случается, то вы на свежую голову пересматривайте код — уверен, что половину сами бы увидели

def to_ten(num: str, int_1: int) -> int:
    """Возвращает переданную строку в десятичной системе счисления."""
    dict_num = dict(zip(
        # ИСПРАВИТЬ здесь и далее: range(0, 10) == range(10)
        # ИСПРАВИТЬ здесь и далее: chr() возвращает объект str — преобразование избыточно
        [str(n) for n in range(0, 10)] + [str(chr(c)) for c in range(97, 123)],
        # ИСПРАВИТЬ здесь и далее: функция zip() принимает любые итерируемые объекты, поэтому достаточно range(36)
        [i for i in range(0, 36)]
    ))
    num_10 = 0
    n = len(num) - 1
    for i in num:
        # ИСПОЛЬЗОВАТЬ везде: круглые скобки вокруг выражений нужны либо для многострочной записи, либо для изменения приоритетов операторов — в остальных случаях не нужны
        num_10 += (dict_num[i]) * (int_1**n)
        n -= 1
    return num_10


def to_base(num: int, int_1: int) -> str:
    """Возвращает переданное число из десятичной системы счисления в любую другую систему счисления."""
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
    # ИСПРАВИТЬ: вместо этих лишних циклов словарь выше стоило создать наоборот (впрочем, на самом деле хватило бы и списка)
    for rem in num_out:
        for k, v in dict_num.items():
            if rem == v:
                str_out.append(k)
                break
    return ''.join(str_out)


def int_base(num: str, arg1: int, arg2: int) -> str | None:
    """Возвращает переданный параметр (num) из системы счисления указанной параметром (arg1)
       в систему счисления указанной в параметре (arg2). Функция работает с системами счисления от 2 до 36."""
    list_num = [str(n) for n in range(0, 10)] + [str(chr(c)) for c in range(97, 123)]
    if (
            2 <= arg1 <= 36
        and 2 <= arg2 <= 36
        # КОММЕНТАРИЙ: хороший способ, хотя хватило бы и представления списка — метод join() всё ж чутка помедленнее
        and not ''.join(c for c in num.lower() if c in list_num[arg1:])
    ):
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


# ИТОГ: неплохо, доработать — 4/8
