inp = input('Введите имена файлов: ')

list_inp = sorted(inp.split('; '))
list_out = []

# 1 вариант. Если использовать в нескольких программах - есть вероятность совпадения имен файлов.
dict_count = {}
for file in list_inp:
    dict_count[file] = dict_count.get(file, 0) + 1
    if dict_count[file] == 1:
        list_out.append(file)
    else:
        list_out.append(file[:file.index('.')] + '_' + str(dict_count[file]) + file[file.index('.'):])

print(*list_out, sep='\n')

# 2 вариант. Этот вариант может использоваться несколькими программами для переименования файлов
# (не создадут одинаковые имена файлов (в теории))

# for i in list_inp:
    # if i in list_out:
        # count = 2
        # copy_i = i
        # while i in list_out:
            # i = copy_i[:copy_i.index('.')] + '_' + str(count) + copy_i[copy_i.index('.'):]
            # count += 1
        # list_out.append(i)
    # else:
        # list_out.append(i)

# print(*list_out, sep='\n')


# Введите имена файлов: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz

