inp_1 = input("Введите числа через пробел: ").split()
inp_2 = input("Введите числа через пробел: ").split()
list_int_1, list_int_2 = [int(i) for i in inp_1], [int(i) for i in inp_2]

# ИСПОЛЬЗОВАТЬ: альтернативный способ написания того же самого (чуть более щадящий для памяти):
# prompt = "Введите числа через пробел: "
# list_int_1 = [int(n) for n in input(prompt).split()]
# list_int_2 = [int(n) for n in input(prompt).split()]

print_out = 'Нет'
if not list_int_2:
    print_out = 'Да'
else:
    len_list_int_2 = len(list_int_2)
    for i in range(len(list_int_1)):
        # УДАЛИТЬ: никак не могу понять, зачем здесь вложенный цикл — сравнить срез первого списка со вторым списком можно прекрасно и без него
        # for num in list_int_2:
            # ИСПРАВИТЬ: неоптимально на каждой итерации заново вычислять длину списка, про который точно известно, что его длина не изменится в ходе работы этого цикла
            # УДАЛИТЬ: первая часть условия избыточна, поскольку она проверяется во второй части условия
        if list_int_2 == list_int_1[i:i + len_list_int_2]:
            print_out = 'Да'
            break
print(print_out)

# ОТВЕТИТЬ: а какие ещё возможны способы решения этой задачи?

# # Через преобразование в строку
# if not list_int_2 or str(list_int_2)[1:-1] in str(list_int_1)[1:-1]:
    # print_out = 'Да'
# print(print_out)
    
# # Срез без использования цикла. Так как писал в качестве примера, не стал объявлять переменную для list_int_1.index(list_int_2[0])   
# if (not list_int_2 or list_int_2 
   # and list_int_1[list_int_1.index(list_int_2[0]):list_int_1.index(list_int_2[0]) + len(list_int_2)] == list_int_2
   # ):
    # print_out = 'Да' 
# print(print_out)


# 11 12 45 65 89 562 23658
# 12 45 65 89
# Да


# ИТОГ: нужно лучше — 1/3
