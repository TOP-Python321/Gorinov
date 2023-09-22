"""
Представление MVC приложения.
"""


class CLI:
    """Класс CLI представляет реализацию представления."""
    @staticmethod
    def to_email() -> str:
        """Запрашивает у пользователя адрес электронной почты через stdin и возвращает его."""
        return input('Введите email: > ')

    @staticmethod
    def error_email(email: str) -> None:
        """Выводит в stdout сообщение о некорректном вводе электронной почты."""
        print(f'{email} -> некорректный адрес.')

    @staticmethod
    def save_email(email: str) -> None:
        """Выводит в stdout сообщение об успешном добавлении электронной почты."""
        print(f'{email} -> успешно добавлен.')
