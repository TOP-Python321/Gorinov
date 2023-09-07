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
    """Представляет методы для выполнения или отмены операции."""
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
    def __init__(self):
        super().__init__()        
        self.undo_operation = []

    def execute(self, *commands):
        for command in commands:
            command.execute()
            self.append(command)
        return self

    def undo(self):        
        self[-1].undo()
        self.undo_operation.append(self.pop())
        
    def re_undo(self) -> None:
        if su_o := self.undo_operation:
            self.execute(su_o[-1])
            su_o.remove(su_o[-1])
        


t1 = TestCase()
t2 = TestCase()
t3 = TestCaseCommand(TestCase(), Operation.PRINT_MSG)
ctcc = CompositeTestCaseCommand().execute(TestCaseCommand(t1, Operation.PRINT_MSG))
ctcc.execute(TestCaseCommand(t2, Operation.PRINT_NUMS), t3)
print(f'{ctcc = }')
print(f'{len(t1.messages) = }')
print(f'{len(t2.messages) = }')
print(f'{len(t3.account.messages) = }')

print(f'\nОтмена последней операции.')
ctcc.undo()
print(f'{ctcc = }')
print(f'{len(t1.messages) = }')
print(f'{len(t2.messages) = }')
print(f'{len(t3.account.messages) = }')
print(f'\nПовторное выполнение последней отмененной операции.')
ctcc.re_undo()
print(f'{ctcc = }')
print(f'{len(t1.messages) = }')
print(f'{len(t2.messages) = }')
print(f'{len(t3.account.messages) = }')

# guj
# 70 80 67 45
# xeumda
# ctcc = [TestCaseCommand(), TestCaseCommand(), TestCaseCommand()]
# len(t1.messages) = 999
# len(t2.messages) = 1000
# len(t3.account.messages) = 999

# Отмена последней операции.
# ctcc = [TestCaseCommand(), TestCaseCommand()]
# len(t1.messages) = 999
# len(t2.messages) = 1000
# len(t3.account.messages) = 1000

# Повторное выполнение последней отмененной операции.
# xeumda
# ctcc = [TestCaseCommand(), TestCaseCommand(), TestCaseCommand()]
# len(t1.messages) = 999
# len(t2.messages) = 1000
# len(t3.account.messages) = 999
# >>>
