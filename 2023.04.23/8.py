num_n = int(input('Введите натуральное число: '))

num = 0
case = [1, 1]

if num_n == 1:
        print(case[1])
        
elif num_n == 2:
        print(*case)
        
else:
    for i in range(2, num_n):
        
        case += [case[-1] + case[-2]]
        
    print(*case)
    
# Введите натуральное число: 18

# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584