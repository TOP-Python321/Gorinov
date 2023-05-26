def taxi_cost(distance: int, time: int = 0) -> int | None:
    """Возвращает результат вычисления стоимости поездки или None - если вычисление не возможно"""
    # переменные объявлены для возможности изменения тарифов и для понимания работы функции
    price = 80
    bid = 6 / 150
    waiting = 3 * time
    fine = 80
    
    if distance >= 0 and time >= 0:
        if distance == 0:
            return round(price + fine + waiting)
        return round(price + distance * bid + waiting)


# >>> taxi_cost(5415560, 25)
# 216777

# >>> print(taxi_cost(5415560, -1))
# None

