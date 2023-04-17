inp_1 = input('Введите координаты первой клетки: ')
inp_2 = input('Введите координаты второй клетки: ')

if ((len(inp_1) == 2 and len(inp_2) == 2) and 'a'<= inp_1[0] <= 'h' and '1' <= inp_1[1] <= '8' and
    'a' <= inp_2[0] <= 'h' and '1' <= inp_2[1] <= '8'):
    
    char_11 = ord(inp_1[0])
    char_12 = int(inp_1[1])
    char_21 = ord(inp_2[0])
    char_22 = int(inp_2[1])
    
    if char_11 - 1 <= char_21 <= char_11 + 1 and char_12 - 1 <= char_22 <= char_12 + 1:
        print('Да')
        
    else:
        print('Нет')
        
else:
    print('Введите корректно координаты')
    
# Да