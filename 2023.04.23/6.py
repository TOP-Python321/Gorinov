num = input('Введите шестизначное число: ')

sum_num_1 = sum(int(num[i]) for i in range(3))
sum_num_2 = sum(int(num[i]) for i in range(3,6))

if sum_num_1 == sum_num_2:
    print('Да')
else:
    print('Нет')

# решение через цикл    
# sum_num_1, sum_num_2 = 0, 0
# for i in range(3):
    # sum_num_1 += int(num[i])
# for i in range(3, 6):
    # sum_num_2 += int(num[i])
# if sum_num_1 == sum_num_2:
    # print('Да')
# else:
    # print('Нет')


# Введите шестизначное число: 123321
# Да


# ИТОГ: отлично — 3/3
