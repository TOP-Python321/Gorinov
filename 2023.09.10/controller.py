"""
Контроллер MVC приложения.
"""

import model
import view


class Application:
    """Класс Application представляет реализацию контроллера."""
    @staticmethod
    def save_email(in_emai: str) -> None:
        """
        Проверяет переданный адрес электронной почты в виде строки. При успешной проверке сохраняет данные в файл и
        выводит сообщение об успешном добавлении, иначе выводит сообщение о некорректном адресе электронной почты.
        """
        try:
            email = model.Email(in_emai)
        except ValueError:
            view.CLI.error_email(in_emai)
        else:
            model.FileIO.add_email(email.email)
            view.CLI.save_email(email.email)

    @classmethod
    def accept_email(cls):
        """Запрошивает в цикле через stdin адрес электронной почты. Выход из цикла при введении пустой строки."""
        while True:
            inp = view.CLI.to_email()
            if inp:
                cls.save_email(inp)
            else:
                break
