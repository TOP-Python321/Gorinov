inp_1 = input('Введите координаты первой клетки: ')
inp_2 = input('Введите координаты второй клетки: ')

if ((len(inp_1) == 2 and len(inp_2) == 2) and 'a'<= inp_1[0] <= 'h' and '1' <= inp_1[1] <= '8' and
    'a' <= inp_2[0] <= 'h' and '1' <= inp_2[1] <= '8'):
    
    if (ord(inp_1[0]) + int(inp_1[1])) %2 == (ord(inp_2[0]) + int(inp_2[1])) %2:
        print('Да')
        
    else:
        print('Нет')
        
else:
    print('Введите корректно координаты')
    
# Да