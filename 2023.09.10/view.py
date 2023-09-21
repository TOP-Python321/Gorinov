class CLI:
    @staticmethod
    def to_email() -> str:
        return input('Введите email: > ')

    @staticmethod
    def error_email(email: str) -> None:
        print(f'{email} -> некорректный адрес.')

    @staticmethod
    def save_email(email: str) -> None:
        print(f'{email} -> успешно добавлен.')
