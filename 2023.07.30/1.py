# аннотации будут доработаны
from itertools import chain, pairwise
from functools import reduce
class Point:
    def __init__(self, x: float, y: float):        
        self.__x = x
        self.__y = y
        
    @property
    def x(self) -> float:
        return self.__x
        
    @x.setter
    def x(*arg):
        raise TypeError("'Point' object does not support coordinate assignment")
        
    @property
    def y(self) -> float:
        return self.__y
        
    @y.setter
    def y(*arg):
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
            length_calc()
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
    def length(self) -> Point:
        return self.__length
        
    @length.setter
    def length(*arg) -> None:
        raise TypeError("'Line' object does not support length assignment")
        
    @staticmethod
    def __length_calc(point1: Point, point2: Point) -> float:
        return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) **0.5
    
    def __str__(self):
        return f'{self.__start}---{self.__end}'
        
    def __repr__(self):
        return str(self)
        
        
class Polygon(list):
    
    def __init__(self,
                side1: Line,
                side2: Line,
                side3: Line,
                *sides: Line
                ):
        super().__init__(chain((side1, side2, side3), sides))
        
    def _is_closed(self) -> bool:
        if self[0].start != self[-1].end:
            return False
        return all(i[0].end== i[1].start for i in pairwise(self))
        
    @property 
    def perimeter(self) -> float:
        if self._is_closed():            
            return sum(elem.length for elem in self)
        else:
            raise ValueError("line items doesn't form a closed polygon")
         