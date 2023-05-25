fruit_list = []
while True:
    inp = input("Введите название фрукта( введите пустую строку для прекращения ввода): ")
    if not inp:
        break
    else:
        fruit_list.append(inp)

if len(fruit_list) >= 2:
    fruit_list = fruit_list[:-2] + [' и '.join(fruit_list[-2:])]

print(' , '.join(fruit_list))


# яблоко
# груша
# апельсин
# лимон
# яблоко , груша , апельсин и лимон

