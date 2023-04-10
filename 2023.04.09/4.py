#num_var = int(input('Введите трехзначное число: '))
num_var = int(input())
unit_var = num_var%10
dozen_var = (int(num_var/10))%10
hundred_var = int(num_var/100)
sum_var = hundred_var + dozen_var + unit_var
pro_var = hundred_var * dozen_var * unit_var
print(f'Сумма цифр = {sum_var} \nПроизведение цифр = {pro_var}')
#Сумма цифр = 12
#Произведение цифр = 64