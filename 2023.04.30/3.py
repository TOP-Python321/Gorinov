inp_1 = input("Введите числа через пробел: ").split()
inp_2 = input("Введите числа через пробел: ").split()

print_out = 'Нет'
list_int_1, list_int_2 = [int(i) for i in inp_1], [int(i) for i in inp_2]

if not list_int_2:
    print_out = 'Да'
else:
    for i in range(len(list_int_1)):
        for k in list_int_2:
            if list_int_1[i] == k and list_int_2 == list_int_1[i:i + len(list_int_2)]:
                print_out = 'Да'
                break

print(print_out)


# 11 12 45 65 89 562 23658
# 12 45 65 89
# Да


