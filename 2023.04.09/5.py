int_var = int(input())
# КОММЕНТАРИЙ: decimal — десятичный, float — плавающий
float_var = int(input())

miles_var = float(f'{int_var}.{float_var}')
km_var = round(miles_var * 1.61, 1)

print(f'{miles_var} миль = {km_var} км')


# 20.5 миль = 33.0 км


# ИТОГ: отлично — 4/4
