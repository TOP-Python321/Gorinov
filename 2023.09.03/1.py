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
        self_copy = deepcopy(self.keep)
        try:
            file = deepcopy(Turn(self.keep[start_square].piece, self.keep[start_square], self.keep[end_square]))
            self.keep[start_square].piece.move(self.keep[end_square])
        except AttributeError:
            print('Поле пустое.')
        else:
            # print(f'{self_copy = }')
            self.append([file, self_copy])
        return self

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

# >>> test = Game()
# >>> print(test.keep)
# {'a': {1: <a1: White Rook>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}

# >>> test.move('a1', 'a3')
# >>> print(test.keep)
# {'a': {1: <a1: None>, 2: <a2: White Pawn>, 3: <a3: White Rook>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}

# >>> test.move('b1', 'b3')
# >>> print(test.keep)
# {'a': {1: <a1: None>, 2: <a2: White Pawn>, 3: <a3: White Rook>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: None>, 2: <b2: White Pawn>, 3: <b3: White Knight>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}

# >>> test.ext_history()
# 1: White Rook: (a1 -> a3)
# 2: White Knight: (b1 -> b3)

# >>> test.remove(1)

# >>> print(test.keep)
# {'a': {1: <a1: White Rook>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}

# >>> test.remove(2)

# >>> print(test.keep)
# {'a': {1: <a1: None>, 2: <a2: White Pawn>, 3: <a3: White Rook>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}
# >>>
