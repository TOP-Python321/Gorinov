from controller import Application as Ap


def main():
    Ap.accept_email()


if __name__ == '__main__':
    main()

# Введите email: > asd@mail.ru
# asd@mail.ru -> успешно добавлен.
# Введите email: > jhvj@gmail.c
# jhvj@gmail.c -> некорректный адрес.
# Введите email: > try@gmail.com
# try@gmail.com -> успешно добавлен.
# Введите email: >