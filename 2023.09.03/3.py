from dataclasses import dataclass
from typing import Self
from random import choice


@dataclass()
class Request:
    def generate(self):
        elem = choice(['404', '500', None])
        return elem


class RequestModifier:
    def __init__(self):
        self.next_modifier: Optional[CreatureModifier] = None

    def add_modifier(self, modifier: Self):
        """Формирует звено цепочки."""
        if self.next_modifier is None:
            self.next_modifier = modifier
        else:
            self.next_modifier.add_modifier(modifier)
        return self

    def handle(self, request):
        if self.next_modifier:
            self.next_modifier.handle(request)

    def undo(self):
        self.next_modifier = None


class Code404(RequestModifier):
    def handle(self, request):
        if request == '404':
            self.undo()
            return print(f'{self.__class__.__name__}')
        return super().handle(request)


class Code500(RequestModifier):
    def handle(self, request):
        if request == '500':
            self.undo()
            return print(f'{self.__class__.__name__}')
        return super().handle(request)


t1 = Request().generate()

test = RequestModifier().add_modifier(Code404()).add_modifier(Code500())
test.handle(t1)
