num = int(input('Введите натуральное число: '))
sum_num_i = 0

for num_i in range(1, num + 1):

    if num_i * num_i == num:
        sum_num_i += num_i
        break
        
    elif not num % num_i:
        sum_num_i += num_i + num // num_i
        
    elif num_i * num_i > num:
        break
        
print(sum_num_i)

# Введите натуральное число: 49

# 57