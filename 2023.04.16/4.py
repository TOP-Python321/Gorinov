inp_1 = input('Введите координаты первой клетки: ')
inp_2 = input('Введите координаты второй клетки: ')

# ИСПОЛЬЗОВАТЬ: сложносоставные выражения лучше записывать на нескольких строчках — так лучше читается
if ((len(inp_1) == 2 and len(inp_2) == 2)
        and 'a' <= inp_1[0] <= 'h'
        and '1' <= inp_1[1] <= '8'
        and 'a' <= inp_2[0] <= 'h'
        and '1' <= inp_2[1] <= '8'):

    # КОММЕНТАРИЙ: вам очень повезло, что код символа 'a' является нечётным числом =)
    # здесь не понял ошибки. если код символа 'a' будет четным, то далее кода символов идут с шагом +1 и остаток от деления у клеток одного цвета будет одинаковым.
    if (ord(inp_1[0]) + int(inp_1[1])) % 2 == (ord(inp_2[0]) + int(inp_2[1])) % 2:
        print('Да')
    else:
        print('Нет')

else:
    print('Введите корректно координаты')

# КОММЕНТАРИЙ: вот случай, где копирование только вывода без ввода вообще не имеет смысла
# Да


# ИТОГ: отлично — 5/5
