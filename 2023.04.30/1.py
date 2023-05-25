mail_inp = input('Введите электронную почту: ')

for char in mail_inp:
    if char == '@' and '.' in mail_inp[mail_inp.index('@'):]:
        print('Да')
        break
else:
    print('Нет')


# vchcvdh@hbv.ru
# Да

