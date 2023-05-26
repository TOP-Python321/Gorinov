def orth_triangle(*,
                  cathetus1: float = 0,
                  cathetus2: float = 0,
                  hypotenuse: float = 0) -> float | None:
    """Возвращает результат вычисления третьей стороны прямоугольного треугольника. Если вычисление не возможно, возвращает None"""

    if not cathetus1 and cathetus2 and cathetus2 < hypotenuse:
        # ИСПРАВИТЬ здесь и далее: преобразование во float избыточно, потому что 1/2 возвращает объект float, а если хотя бы один из операндов математических операторов (включая **) является объектом float, то и результат будет объектом float
        return float((hypotenuse**2 - cathetus2**2) ** (1/2))

    elif not cathetus2 and cathetus1 and cathetus1 < hypotenuse:
        return float((hypotenuse**2 - cathetus1**2) ** (1/2))

    elif not hypotenuse and cathetus1 and cathetus2:
        return float((cathetus1**2 + cathetus2**2) ** (1/2))


# >>> orth_triangle(cathetus1=6, cathetus2=8)
# 10.0
# >>> orth_triangle(cathetus1=6, hypotenuse=10)
# 8.0
# >>> print(orth_triangle(cathetus2=8,cathetus1=4, hypotenuse=10))
# None


# ИТОГ: очень хорошо — 3/4
