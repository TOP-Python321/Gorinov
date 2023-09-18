from abc import ABC, abstractmethod
from dataclasses import dataclass
from copy import deepcopy
from typing import Self

import chess


@dataclass
class Turn:
    """
    Представляет класс хранитель.
    """
    piece: chess.Piece
    start_square: chess.Square
    end_square: chess.Square


class Game(list):
    """
    Представляет функции инициатора и опекуна для класса chess.Chessboard.
    """
    def __init__(self):
        super().__init__()
        self.keep = chess.Chessboard()

    def move(self, start_square: str, end_square: str) -> Self:
        """Осуществляет переход фигуры с одного поля на другое."""
        # <<<Доработать исключения>>>
        try:
            if PieceMove.check(self.keep, start_square, end_square):
                self_copy = deepcopy(self.keep)
                try:
                    file = deepcopy(Turn(self.keep[start_square].piece, self.keep[start_square], self.keep[end_square]))
                    self.keep[start_square].piece.move(self.keep[end_square])
                except ValueError:
                    print('Поле занято своей фигурой.')
                else:
                    self.append([file, self_copy])
                # return self
            else:
                print('Недопустимый ход.')
        except AttributeError:
            print('Поле пустое.')



    def ext_history(self) -> None:
        """Выводит в std_out пронумерованные ходы."""
        print('\n'.join(
            f'{i + 1}: '
            f'{elem[0].piece!r}: '
            f'({elem[0].start_square} -> '
            f'{elem[0].end_square})'
            for i, elem in enumerate(self))
        )

    def remove(self, index_store: int):
        """
        Возвращает состояние игрового поля до сделанного хода, который получаем из функции ext_history()        

        :param index_store: номер хода из функции ext_history()
        """
        # не удаляет ход из списка сохранений
        self.keep = self[index_store - 1][1]
        return self


class PieceMove:
    """Представляет класс с методом для автоматического выбора стратегии"""
    @staticmethod
    def check(keep: chess.Chessboard, start: str, end: str) -> bool | None:
        """Выбирает стратегию и возвращает результат выбранной стратегии"""
        if keep[start].piece.kind is chess.PieceKind.ROOK:
            return Rook.check_square(start, end)
        elif keep[start].piece.kind is chess.PieceKind.KING:
            return King.check_square(start, end)
        elif keep[start].piece.kind is chess.PieceKind.QUEEN:
            return Queen.check_square(start, end)
        elif keep[start].piece.kind is chess.PieceKind.BISHOP:
            return Bishop.check_square(start, end)
        elif keep[start].piece.kind is chess.PieceKind.KNIGHT:
            return Knight.check_square(start, end)
        elif keep[start].piece.kind is chess.PieceKind.PAWN:
            return Pawn.check_square(keep, start, end)
        else:
            raise ValueError


class Piece(ABC):
    """Абстрактный класс для стратегий."""
    @staticmethod
    @abstractmethod
    def check_square(start: str, end: str) -> bool:
        """Вычисляет и возвращает результат стратегии."""
        pass


class Rook(Piece):
    """Представляет стратегию хода Ладьи."""
    @staticmethod
    def check_square(start: str, end: str) -> bool | None:
        if start[0] == end[0] or start[1] == end[1]:
            return bool(True)


class King(Piece):
    """Представляет стратегию хода Короля."""
    @staticmethod
    def check_square(start: str, end: str) -> bool| None:
        char_11 = ord(start[0])
        char_12 = int(start[1])
        char_21 = ord(end[0])
        char_22 = int(end[1])
        if char_11 - 1 <= char_21 <= char_11 + 1 and char_12 - 1 <= char_22 <= char_12 + 1:
            return bool(True)

class Bishop(Piece):
    """Представляет стратегию хода Слона."""
    @staticmethod
    def check_square(start: str, end: str) -> bool | None:
        char_11 = ord(start[0])
        char_12 = int(start[1])
        char_21 = ord(end[0])
        char_22 = int(end[1])
        if abs(char_11 - char_21) == abs(char_12 - char_22):
            return bool(True)


class Queen(Piece):
    """Представляет стратегию хода Королевы."""
    @staticmethod
    def check_square(start: str, end: str) -> bool | None:
        if (King.check_square(start, end) or
            Rook.check_square(start, end) or
            Bishop.check_square(start, end)
        ):
            return bool(True)


class Knight(Piece):
    """Представляет стратегию хода Коня."""
    @staticmethod
    def check_square(start: str, end: str) -> bool | None:
        char_11 = ord(start[0])
        char_12 = int(start[1])
        char_21 = ord(end[0])
        char_22 = int(end[1])
        if (abs(char_11 - char_21) == 1 and abs(char_12 - char_22) == 2 or
            abs(char_11 - char_21) == 2 and abs(char_12 - char_22) == 1
        ):
            return bool(True)


class Pawn(Piece):
    """Представляет стратегию хода Пешки."""
    @staticmethod
    def check_square(chess_board: chess.Chessboard, start: str, end: str) -> bool:
        char_11 = ord(start[0])
        char_12 = int(start[1])
        char_21 = ord(end[0])
        char_22 = int(end[1])
        res = False

        if (chess_board[end].piece is None and
            (((char_12 == 2 or char_12 == 7) and
            1 <= abs(char_12 - char_22) <= 2) or
            abs(char_12 - char_22) == 1) and
            char_11 == char_21
        ):
            res = True
        elif (chess_board[end].piece is not None and
              chess_board[end].piece.color != chess_board[start].piece.color and
              abs(char_11 - char_21) == 1 and
              abs(char_12 - char_22) == 1
        ):
            res = True
        return bool(res)
        
        
# >>> test = Game()
# >>> test.move('a7', 'a5')
# >>> test.keep
# {'a': {1: <a1: White Rook>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: Black Pawn>, 6: <a6: None>, 7: <a7: None>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}
# >>> test.move('a1', 'a5')
# >>> test.move('b7', 'b6')
# >>> test.move('b6', 'a5')
# >>> test.move('a5', 'b4')
# Недопустимый ход.
# >>> test.move('b1', 'e4')
# Недопустимый ход.
# >>> test.move('b1', 'c3')
# >>> test.move('c8', 'f5')
# >>> test.move('g4', 'g5')
# Поле пустое.
# >>> test.move('c3', 'b5')
# >>> test.move('d8', 'e5')
# Недопустимый ход.
# >>> test.move('d8', 'g5')

# >>> test.ext_history()
# 1: Black Pawn: (a7 -> a5)
# 2: White Rook: (a1 -> a5)
# 3: Black Pawn: (b7 -> b6)
# 4: Black Pawn: (b6 -> a5)
# 5: White Knight: (b1 -> c3)
# 6: Black Bishop: (c8 -> f5)
# 7: White Knight: (c3 -> b5)
# 8: Black Queen: (d8 -> g5)

# >>> test.keep
# {'a': {1: <a1: None>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: Black Pawn>, 6: <a6: None>, 7: <a7: None>, 8: <a8: Black Rook>}, 'b': {1: <b1: None>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: White Knight>, 6: <b6: None>, 7: <b7: None>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: None>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: None>}, 'e': {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: Black Bishop>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: Black Queen>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}
# >>>
