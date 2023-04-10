int_var = int(input())
float_var = int(input())
miles_var = int_var + float_var/10
km_var = round((miles_var * 1.61), 1)
print(f'{miles_var} миль = {km_var} км')
#20.5 миль = 33.0 км