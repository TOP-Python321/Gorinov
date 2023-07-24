from datetime import date
import datetime

vacations: list[tuple[datetime.date, datetime.timedelta]]
# vacations = [(date(2023, 7, 17), datetime.timedelta(weeks=1)),(date(2023, 5, 1), datetime.timedelta(weeks=1))]

def schedule(
        start_date: datetime.date, 
        first_les :int, 
        *next_les: tuple[int, ...],        
        total_days: int, 
        format_str: str = '%d/%m/%Y') -> list[str, ...]:
    """
     Генерирует и возвращает график проведения мероприятий.
     :param start_date: начальная дата для графика
     :param first_les: номер недели, который входит в график
     :param next_les: номера недель, которые входят в график
     :param total_days: количество дней занятий в графике 
     """
    step: int = 0
    list_lessons: list = []
    while total_days > len(list_lessons):
        lessons = [(start_date + datetime.timedelta(weeks = step)) + datetime.timedelta(days) for days in range(7)]        
        lessons = list(dates for dates in lessons if dates.isocalendar()[2] in [first_les,*next_les])        
        list_lessons += list(filter(in_vacations, lessons)) if 'vacations' in globals() else lessons
        step +=1
        
    return list(map(lambda x: x.strftime(format_str), list_lessons[: total_days]))
    
    # незавершенный вариант, без итерации по каждому дню
    # new_start_date = start_date - datetime.timedelta(start_date.weekday())
    # first_week = list(filter(lambda x: x.isocalendar()[2] in [first_les,*next_les], (new_start_date + datetime.timedelta(days) for days in range(7))))
    # print(first_week)
    # step = 0
    # list_lessons = []
    # while total_days > len(list_lessons):
        # lessons = map(lambda x: x + datetime.timedelta(weeks=step), first_week)
        # list_lessons += list(filter(in_vacations, lessons))
        # step += 1
    # print(list_lessons)
    # return list_lessons    
    
def  in_vacations(x: datetime.date) -> bool:
    """Проверяет входит ли переданный аргумент в диапазон дат списка vacations."""
    for elem in vacations:        
        if elem[0] < x < elem[0] + elem[1]:
            return False
    return True
    
# >>> py321 = schedule(date(2023, 4, 1), 6, 7, total_days=50)
# >>> len(py321)
# 50
# >>> py321[28:32]
# ['08/07/2023', '09/07/2023', '15/07/2023', '16/07/2023']
# >>> vacations = [(date(2023, 7, 17), datetime.timedelta(weeks=1)),(date(2023, 5, 1), datetime.timedelta(weeks=1))]
# >>> py321 = schedule(date(2023, 4, 1), 6, 7, total_days=50)
# >>> len(py321)
# 50
# >>> py321[28:32]
# ['15/07/2023', '16/07/2023', '29/07/2023', '30/07/2023']
# >>> py321 = schedule(date(2023, 4, 1),1, 6, 7, total_days=50)
# >>> len(py321)
# 50
# >>> py321[28:32]
# ['10/06/2023', '11/06/2023', '12/06/2023', '17/06/2023']
    