# time_min = input("Введите время в минутах: ")

# ИСПРАВИТЬ: избыточность строк кода
time_min = input()
time_min = int(time_min)

# ИСПОЛЬЗОВАТЬ: обычно стараются разделять оператор и его операнды пробелами
time_hour = int(time_min / 60)
time_rem_min = time_min % 60

print(f'{time_min} мин - это {time_hour} час {time_rem_min} мин')


# 150 мин - это 2 час 30 мин


# ИТОГ: отлично — 3/3
