class Tetrahedron:
    """Класс Rectangle описывает правильный тетраэдр."""
    def __init__(self, edge: float):
        """
        Инициализирует объект класса Rectangle.
        :param edge: длина ребра
        """
        self.edge = float(edge)
        
    def surface(self) -> float:
        """Возвращает площадь поверхности экземпляра класса."""
        return self.edge ** 2 * 3 ** 0.5
        
    def volume(self) -> float:
        """Возвращает объём экземпляра класса."""
        return self.edge ** 3 / 12 * 2 ** 0.5  
        

# >>> t1 = Tetrahedron(5)
# >>> t1.edge
# 5.0
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.73139127471974
# >>> t1.edge = 6
# >>> t1.surface()
# 62.35382907247958

# >>> t2 =  Tetrahedron(7)
# >>> t2.edge
# 7.0
# >>> t2.volume()
# 40.42293765783097
# >>> t2.surface()
# 84.87048957087498
# >>> t2 =  Tetrahedron(5)
# >>> t2.volume()
# 14.73139127471974