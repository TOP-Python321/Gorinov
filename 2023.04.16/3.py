inp = input('Введите год: ')

if inp.isdecimal():
    inp = int(inp)

    # КОММЕНТАРИЙ: отлично
    if (not inp % 4 and inp % 100) or not inp % 400:
        print('Да')
    else:
        print('Нет')

else:
    print('Неверный формат ввода')

# Да


# ИТОГ: отлично — 3/3
