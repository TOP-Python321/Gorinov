mail_inp = input('Введите электронную почту: ')

for i in mail_inp:

    if i == '@' and '.' in mail_inp[mail_inp.index('@'):]:
        print('yes')
        break

else:
    print('No')

# acssdcdsc@mail.ru

# yes