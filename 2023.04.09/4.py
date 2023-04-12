# num_var = int(input('Введите трехзначное число: '))
num_var = int(input())

# КОММЕНТАРИЙ: единицы (разряд числа) — ones, единица измерения — unit
unit_var = num_var % 10
# КОММЕНТАРИЙ: десятки (разряд числа) — tens, (примерно) десяток, дюжина — dozen
dozen_var = int(num_var / 10) % 10
hundred_var = int(num_var / 100)

sum_var = hundred_var + dozen_var + unit_var
pro_var = hundred_var * dozen_var * unit_var

# ИСПОЛЬЗОВАТЬ: перенос строковых литералов внутри скобок
print(f'Сумма цифр = {sum_var} \n'
      f'Произведение цифр = {pro_var}')


# Сумма цифр = 12
# Произведение цифр = 64


# ИТОГ: отлично — 4/4
