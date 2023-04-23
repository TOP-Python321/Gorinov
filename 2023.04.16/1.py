inp_1 = float(input('Введите первое число: '))
inp_2 = float(input('Введите второе число: ')) 
inp_3 = float(input('Введите третье число: '))

sum_inp = 0

if inp_1 > 0:
    sum_inp += inp_1 

if inp_2 > 0:
    sum_inp += inp_2

if inp_3 > 0:
    sum_inp += inp_3

if sum_inp - int(sum_inp) > 0:
    print(round(sum_inp, 2))
else:
    print(round(sum_inp))
    
# 5.5
