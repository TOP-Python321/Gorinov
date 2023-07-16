import datetime
from decimal import Decimal
import numbers

class PowerMeter:
    """Описывает двухтарифный счетчик потребленной электрической мощности."""
    def __init__(
            self,
            tariff1: numbers.Number = 6.62,
            tariff2: numbers.Number = 3.45,
            tariff2_starts: datetime.time = datetime.time(23, 0),
            tariff2_ends: datetime.time = datetime.time(7, 0)
        ):
        self.tariff1: decimal.Decimal = Decimal(tariff1)
        self.tariff2: decimal.Decimal = Decimal(tariff2)
        self.tariff2_starts: datetime.time = tariff2_starts
        self.tariff2_ends: datetime.time = tariff2_ends
        self.power: decimal.Decimal = 0
        self.charges: dict[datetime.date, decimal.Decimal] = {}
        self.month: str = datetime.datetime.now().strftime("%b")
        
    def __str__(self):
        return f"({self.month}) {self.charges.get(self.month, 0)}"
        
    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.power:.2f} кВт/ч>"
        
    def meter(self, power: numbers.Number) -> Decimal :
        """
        Вычисляет и возвращает стоимость потребленной электрической мощности.
        :param power: потребленная электрическая мощность.
        """
        self.power += Decimal(power)
        tmp_hour: datetime.time = datetime.time(datetime.datetime.now().hour)
      
        if self.tariff2_ends < tmp_hour < self.tariff2_starts:
            cost = round(Decimal(power) * self.tariff1, 2)            
        else:
            cost = round(Decimal(power) * self.tariff2, 2)            
        
        self.charges[self.month] = self.charges.get(self.month, 0) + cost
        return cost
        
# >>> pm =  PowerMeter()
# >>> pm
# <PowerMeter: 0.00 кВт/ч>
# >>> print(pm)
# (Jul) 0
# >>> pm.meter(3)
# Decimal('19.86')
# >>> pm.meter(1.5)
# Decimal('9.93')
# >>> pm
# <PowerMeter: 4.50 кВт/ч>
# >>> print(pm)
# (Jul) 29.79