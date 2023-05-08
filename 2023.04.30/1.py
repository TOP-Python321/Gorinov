mail_inp = input('Введите электронную почту: ')

for i in mail_inp:

    if i == '@' and '.' in mail_inp[mail_inp.index('@'):]:
        print('Да')
        break

else:
    print('Нет')

# vchcvdh@hbv.ru

# Да