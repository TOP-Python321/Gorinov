inp = input('Введите год: ')

if inp.isdecimal():
    inp = int(inp)

    if (not inp % 4 and inp % 100) or not inp % 400:
        print('Да')
        
    else:
        print('Нет')

else:
    print('Не верный формат ввода')
    
# Да