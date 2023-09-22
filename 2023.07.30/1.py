from itertools import chain, pairwise
from functools import reduce


class Point:
    """Описывает двухмерную точку."""
    def __init__(self, x: float, y: float):        
        self.__x = x
        self.__y = y
        
    @property
    def x(self) -> float:
        return self.__x
        
    @x.setter
    def x(self, *arg) -> None:
        raise TypeError("'Point' object does not support coordinate assignment")
        
    @property
    def y(self) -> float:
        return self.__y
        
    @y.setter
    def y(self, *arg) -> None:
        raise TypeError("'Point' object does not support coordinate assignment")
        
    def __repr__(self):
        return f'({self.__x},{self.__y})'

    def __str__(self):
        return repr(self)
        
    def __eq__(self, other):
        return (
                self.__x == other.__x
                and self.__y == other.__y)
                
                
class Line:
    """Описывает отрезок."""
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end        
        self.__length = self.__length_calc(self.__start, self.__end)
        
    @property
    def start(self) -> Point:
        return self.__start
        
    @start.setter
    def start(self, start) -> None:
        if isinstance(start, Point):
            self.__start = start
        else:
            raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")
        
    @property
    def end(self) -> Point:
        return self.__end
        
    @end.setter
    def end(self, end) -> None:
        if isinstance(end, Point):
            self.__end = end
        else:
            raise TypeError("'end' attribute of 'Line' object supports only 'Point' object assignment")
        
    @property
    def length(self) -> float:
        return self.__length
        
    @length.setter
    def length(self, *arg) -> None:
        raise TypeError("'Line' object does not support length assignment")
        
    @staticmethod
    def __length_calc(point1: Point, point2: Point) -> float:
        """Вычисляет и возвращает расстояние между двумя точками."""
        return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5
    
    def __str__(self):
        return f'{self.__start}---{self.__end}'
        
    def __repr__(self):
        return str(self)
        
        
class Polygon(list):
    """Описывает многоугольник."""
    
    def __init__(self,
                side1: Line,
                side2: Line,
                side3: Line,
                *sides: Line
    ):
        super().__init__(chain((side1, side2, side3), sides))
        
    def _is_closed(self) -> bool:
        """Проверяет формируют ли отрезки замкнутый многоугольник, возвращает bool объект."""
        if self[0].start != self[-1].end:
            return False
        return all(i[0].end == i[1].start for i in pairwise(self))
        
    @property 
    def perimeter(self) -> float:
        """Вычисляет и возвращает периметр многоугольника."""
        if self._is_closed():
            return reduce(lambda x, y: y+x, [elem.length for elem in self])
        else:
            raise ValueError("line items doesn't form a closed polygon")
  
# >>> p1 = Point(0, 4)
# >>> p2 = Point(4, 5)
# >>> p3 = Point(4, 3)
# >>>
# >>> p1
# (0,4)
# >>>
# >>> repr(p1) == str(p1)
# True
# >>> p1 == Point(0, 4)
# True
# >>>
# >>> p1.x, p1.y
# (0, 4)
# >>>
# >>> p2.y = 5
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
  # File "C:\Users\ПК\Desktop\TOP\Git\repository\самостоятельная работа\i_work\dreft 2023.07.30\1.py", line 25, in y
    # raise TypeError("'Point' object does not support coordinate assignment")
# TypeError: 'Point' object does not support coordinate assignment
# >>>
# >>> l1 = Line(p1, p2)
# >>> l2 = Line(p2, p3)
# >>> l3 = Line(p3, p1)
# >>>
# >>> l1
# (0,4)---(4,5)
# >>>
# >>> repr(l1) == str(l1)
# True
# >>>
# >>> l1.length
# 4.123105625617661
# >>>
# >>> l1.length = 10
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
  # File "C:\Users\ПК\Desktop\TOP\Git\repository\самостоятельная работа\i_work\dreft 2023.07.30\1.py", line 73, in length
    # raise TypeError("'Line' object does not support length assignment")
# TypeError: 'Line' object does not support length assignment
# >>>
# >>> l3.start = 1
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
  # File "C:\Users\ПК\Desktop\TOP\Git\repository\самостоятельная работа\i_work\dreft 2023.07.30\1.py", line 54, in start
    # raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")
# TypeError: 'start' attribute of 'Line' object supports only 'Point' object assignment
# >>>
# >>> pol1 = Polygon(l1, l2, l3)
# >>>
# >>> pol1.perimeter
# 10.246211251235321
# >>>
# >>> pol1.perimeter = 26
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: property 'perimeter' of 'Polygon' object has no setter
# >>>
# >>> l3.end = Point(5, 9)
# >>>
# >>> pol1[-1] = l3
# >>> pol1.perimeter
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
  # File "C:\Users\ПК\Desktop\TOP\Git\repository\самостоятельная работа\i_work\dreft 2023.07.30\1.py", line 107, in perimeter
    # raise ValueError("line items doesn't form a closed polygon")
# ValueError: line items doesn't form a closed polygon
# >>>  