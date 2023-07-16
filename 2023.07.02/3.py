class ChessKing:
    """Описывает шахматную фигуру короля."""
    files: dict[str, int] = dict((chr(ord('a') + val), val + 1) for val in range(8))
    ranks: dict[str, int] = dict((str(num), num) for num in range(1, 9))
    
    def __init__(self, color: str = 'white', square: str = None):
        self.color = color
        if square is None:
            if self.color == 'white':
                square = 'e1'
            else:
                square = 'e8'
        self.square = square        
        
    def __repr__(self):
        return f"'{''.join(k for k, v in globals().items() if v is self).upper()}: {self.square}'"          

    def __str__(self):
        return f"{''.join(k for k, v in globals().items() if v is self).upper()}: {self.square}"    
    
    def is_turn_valid(self, field: str) -> bool:
        """
        Принимает координаты поля в виде строки. И возвращает True, если возможен ход для данного экземпляра класса.
        :param field: координаты поля в виде строки.
        """
        if ( 
                -1 <= self.files[self.square[0]] - self.files[field[0]] <= 1
            and -1 <= self.ranks[self.square[1]] - self.ranks[field[1]] <= 1
            ):
            return True        
        return False        
        
    def turn(self, field: str) ->None:
        """
        Принимает координаты поля в виде строки. Если координыты соответствуют условию, записывает новые
        координаты в атрибут self.square. Иначе выбрасывает ошибку.
        :param field: координаты поля в виде строки.
        """
        if self.is_turn_valid(field):
            self.square = field
        else:
            raise ValueError
      
# >>> ek = ChessKing()
# >>> ek
# 'EK: e1'
# >>> ek.color
# 'white'
# >>> ek.turn('h1')
# ...
# ValueError
# >>> ek.turn('f1')
# >>> ek.square
# 'f1'
# >>> print(ek)
# EK: f1
# >>>
# >>> bbk = ChessKing('black', 'd4')
# >>> bbk.square
# 'd4'
# >>> bbk
# 'BBK: d4'
# >>> bk
# >>> bbk.turn('e5')
# >>> print(bbk)
# BBK: e5
