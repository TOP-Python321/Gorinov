digit = int(input('Введите разряд числа: '))

range_1 = int('1' + '0' * (int(digit) - 1))
count = 0

# долго вычисляет при разряде больше 4
for num_1 in range(range_1, int('9' * digit) + 1):

    step = 0
    
    for num_2 in range(2, num_1):
    
        if num_1 % num_2 == 0:
             step += 1
             
    if step == 0:
        count += 1
        
print(count)

# Введите разряд числа: 4

# 1061