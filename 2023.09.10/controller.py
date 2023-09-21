import model
import view


class Application:
    @staticmethod
    def save_email(in_emai: str):
        try:
            email = model.Email(in_emai)
        except ValueError:
            view.CLI.error_email(in_emai)
        else:
            model.FileIO.add_email(email.email)
            view.CLI.save_email(email.email)

    @classmethod
    def accept_email(cls):
        while True:
            inp = view.CLI.to_email()
            if inp:
                cls.save_email(inp)
            else:
                break
