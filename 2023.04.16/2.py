inp_1 = input("Введите целое число: ")
inp_2 = input("Введите целое число: ")

if inp_1.isdecimal() and inp_2.isdecimal():    
    inp_1, inp_2 = int(inp_1), int(inp_2)
    
    if inp_1 % inp_2 == 0:
        print(f'{inp_1} делится на {inp_2} нацело\n'
              f'частное: {inp_1 / inp_2:.0f}')

    else:
        print(f'{inp_1}  не делится на {inp_2} нацело\n'
              f'неполное частное: {inp_1 / inp_2:.0f}\n'
              f'остаток: {inp_1 % inp_2:.0f}')
              
else:
    print("Введите целое число")
    
# 11  не делится на 5 нацело
# неполное частное: 2
# остаток: 1