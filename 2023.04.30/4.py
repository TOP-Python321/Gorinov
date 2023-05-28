case = {}
while True:
    inp = input('Введите число и через пробел значение\n(для выхода - введите пустую строку): ')
    if not inp:
        break
    # ИСПОЛЬЗОВАТЬ: если мы уверены в том, что split() вернёт список из ровно двух объектов (а в учебной задаче мы уверены), то можно сходу распаковать:
    # key, value = inp.split()
   
    key, value = inp.split()
    case[key] =  value

inp_value = input('Введите значение: ')
for k, v in case.items():
    if v == inp_value:
        print(k)
        break
else:
    print('! value error !')   
    


# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB
# 1007 ER_DB_CREATE_EXISTS
# 1008 ER_DB_DROP_EXISTS
# 1010 ER_DB_DROP_RMDIR
# 1016 ER_CANT_OPEN_FILE
# 1022 ER_DUP_KEY
# ER_DB_DROP_RMDIR
# 1010


# ИТОГ: отлично — 3/3
