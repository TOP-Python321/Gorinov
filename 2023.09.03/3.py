from enum import Enum
from typing import Self
from random import choice


class Handler:
    """
    Базовый класс цепочки обработчиков.
    """
    code: int

    def __init__(self):
        self.next_modifier: Handler | None = None

    def add_modifier(self, modifier: Self):
        """Формирует звено цепочки."""
        if self.next_modifier is None:
            self.next_modifier = modifier
        else:
            self.next_modifier.add_modifier(modifier)

    def handle(self, request: int):
        if self.next_modifier:
            self.next_modifier.handle(request)

    def info(self, msg: str):
        print(f'{self.__class__.__name__}: {msg}')


class Code404(Handler):
    code = 404

    def handle(self, request: int):
        if request != self.code:
            return super().handle(request)
        self.info('Not Found client error response')


class Code500(Handler):
    code = 500

    def handle(self, request: int):
        if request != self.code:
            return super().handle(request)
        self.info('Internal Server Error server error response')


class Response(Enum):
    # это пример ручного добавления обработчиков в перечислитель, а можно сделать и автоматически для всех производных классов Handler
    # OK =
    # FORBIDDEN =
    # MOVED_PERMANENTLY =
    NOT_FOUND = Code404
    INTERNAL_SERVER_ERROR = Code500

    @classmethod
    def random(cls) -> Self:
        return choice(tuple(cls))


class MockWebServer:
    """
    Имитация работы веб-сервера, который получает запрос и генерирует ответ.
    """
    def __init__(self):
        self.chain_root = Handler()
        for handler in tuple(Response):
            self.chain_root.add_modifier(handler.value())

    def get_request(self):
        """Имитация получения запроса."""
        input('request > ')
        self.handle_request()

    def handle_request(self):
        """Имитация обработки запроса."""
        # генерация случайного ответа
        response = Response.random().value.code
        # обработка ответа
        return self.chain_root.handle(response)


test = MockWebServer()
test.get_request()

