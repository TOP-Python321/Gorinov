int_var = int(input())
# КОММЕНТАРИЙ: decimal — десятичный, float — плавающий
float_var = int(input())

# ИСПРАВИТЬ: ваш способ не сработает если пользователю понадобится ввести дробную часть для числа 12.34
miles_var = float(f'{int_var}.{float_var}')
# ИСПРАВИТЬ: скобки вокруг выражения miles_var * 1.61 не нужны
km_var = round(miles_var * 1.61, 1)

print(f'{miles_var} миль = {km_var} км')


# 20.5 миль = 33.0 км


# ИТОГ: доработать — 2/4
