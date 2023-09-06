from random import randrange as rr, sample
from string import ascii_lowercase as letters
from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass


class Operation(Enum):
    PRINT_MSG = 'print_msg'
    PRINT_NUMS = 'print_nums'


class TestCase:
    """
    Адресат.
    """
    def __init__(self):
        self.messages = [
            ''.join(sample(letters, k=rr(3, 7)))
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4, 6))) 
            for _ in range(1000)
        ]
    
    def print_msg(self):
        msg = self.messages.pop()
        print(msg)
    
    def print_nums(self):
        nums = self.numbers.pop()
        print(*nums)
    

class Command(ABC):
    """Базовый класс команд для различных действий."""
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

@dataclass
class TestCaseCommand(Command):
    """Одна команда."""
    def __init__(self, account: TestCase, action: Operation):
        self.account = account
        self.action = action
        self.success: bool = False

    def execute(self):
        if self.action is Operation.PRINT_MSG:
            self.values = self.account.messages[-1]
            self.account.print_msg()
            self.success = True
        elif self.action is Operation.PRINT_NUMS:
            self.values = self.account.numbers[-1]
            self.account.print_nums()
            self.success = True

    def undo(self):
        if self.success:
            if self.action is Operation.PRINT_MSG:
                self.account.messages.append(self.values)
            elif self.action is Operation.PRINT_NUMS:
                self.account.numbers.append(self.values)
            self.success = False
        else:
            pass


class CompositeTestCaseCommand(Command, list):
    """Список команд."""
    def __init__(self, *commands: Command):
        super().__init__()
        self.append(*commands)

    def execute(self):
        for command in self:
            command.execute()

    def undo(self):
        for command in self:
            command.undo()


t1 = TestCase()
print(t1.messages)
ctcc = CompositeTestCaseCommand(TestCaseCommand(t1, Operation.PRINT_MSG))
ctcc.execute()
print(t1.messages)
ctcc.undo()
print(t1.messages)
