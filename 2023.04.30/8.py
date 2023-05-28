inp = input('Введите имена файлов: ')

list_inp = sorted(inp.split('; '))
list_out = []

# 1 вариант. Если использовать в нескольких программах - есть вероятность совпадения имен файлов.
# ОТВЕТИТЬ: что подразумевается под "несколькими программами"?
# Предположил, что несколько программ записывают файлы в одну папку и каждая из них создайт свой словарь (dict_count), но на выходе нет проверки есль ли уже в папке такой файл.

dict_count = {}
for file in list_inp:
    dict_count[file] = dict_count.get(file, 0) + 1
    # КОММЕНТАРИЙ: хорошо, что в один цикл пошли
    if dict_count[file] == 1:
        list_out.append(file)
    else:
        # ИСПРАВИТЬ: метод index() вызывается лишний раз — оптимизируйте
        point_index = file.index('.')
        list_out.append(file[:point_index] + '_' + str(dict_count[file]) + file[point_index:])

print(*list_out, sep='\n')

# 2 вариант. Этот вариант может использоваться несколькими программами для переименования файлов
# (не создадут одинаковые имена файлов (в теории))
# КОММЕНТАРИЙ: если вы подразумеваете различные процессы в ОС, то каждый из них существует в своём пространстве имён — чтобы несколько различных приложений работая параллельно с реальной файловой системой не допускали дублей при переименовывании файлов в одном каталоге, каждое из приложений должно на каждой итерации обновлять текущие имена файлов (list_inp в данном примере)

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


# ИТОГ: очень хорошо — 5/6
