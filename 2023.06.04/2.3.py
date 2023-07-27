from datetime import datetime, timedelta
from random  import randrange as rr
from random  import choice

names = {'names': [[],[]], 'middle_name': [[],[]], 'surnames': [[],[]]}
def load_data() -> None:
    """Читает данные из файлов и записывает их в словарь names"""
    with open('женские_имена.txt', 'r', encoding='utf-8') as filein:       
        female_name: list = list(map(lambda x: x.rstrip('\n'), filein.readlines()))
        names['names'][1] = female_name       
        
    with open('мужские_имена_отчества.txt', 'r', encoding='utf-8') as filein:        
        male_name_middle_name: list = list(map(lambda x: x.rstrip(')\n').split(' ('), filein.readlines()))
        male_name = list(map(lambda x: x[0], male_name_middle_name))
        middle_name = list(map(lambda x: x[1].split(', '), male_name_middle_name))
       
        new_middle_name: list = [[], []]        
        for elem in middle_name:     
            new_middle_name[0].append(elem[0])
            new_middle_name[1].append(elem[1])        
        names['names'][0] = male_name
        names['middle_name'] = new_middle_name 
        
        
    with open('фамилии.txt', 'r', encoding='utf-8') as filein:
        surnames: list = list(map(lambda x: x.rstrip('\n').split(', '), filein.readlines()))        
        male_surnames: list = []
        female_surnames: list = []
        
        for elem in surnames:            
            if len(elem) == 2:
                male_surnames.append(elem[0])
                female_surnames.append(elem[1])
            else:
                male_surnames.append(elem[0])
                female_surnames.append(elem[0])     
        names['surnames'] = [male_surnames, female_surnames]
 
 
def generate_person() -> dict[
                                str,
                                str,
                                str,
                                str,
                                datetime.date,str
                                ]:
    """Генерирует и возвращает анкету человека со случайными данными в виде словаря"""
    pick = rr(2)
    GENDER: list = ['мужской', 'женский'] 
    out_dict = {
            'имя': choice(names['names'][pick]),
            'отчество': choice(names['middle_name'][pick]),
            'фамилия': choice(names['surnames'][pick]),
            'пол': GENDER[pick],
            'дата рождения': date_generator(),
            'мобильный': generate_phone_number()}
    return out_dict        
        
        
def date_generator() -> datetime.date:
    """Генерирует и возвращаее объект (datetime.date) из диапазона: сегодняшняя дата - 100 лет."""    
    now_day: datetime.datetime = datetime.now()
    # получение строкового представления даты - 100 лет назад.
    start_day = f'{datetime.now().year - 100}, {datetime.now().month}, {datetime.now().day}'
    # получение объекта datetime.date
    start_day = datetime.strptime(start_day, "%Y, %m, %d").date()
    # получение количества дней между стартовой и сегодняшней датой
    delta = now_day.date() - start_day
    out_date = start_day + timedelta(rr(delta.days))
    return out_date    
    
    
def generate_phone_number() -> str:
    """Генерирует и возвращает номер мобильного телефона в строковом представлении."""
    return f'+79' + ''.join(str(rr(10)) for _ in range(9))
    
# >>> from pprint import pprint
# >>> load_data()
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Есения',
 # 'отчество': 'Рудольфовна',
 # 'фамилия': 'Ермолова',
 # 'пол': 'женский',
 # 'дата рождения': datetime.date(2003, 8, 11),
 # 'мобильный': '+79629860950'}
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Исай',
 # 'отчество': 'Варфоломеевич',
 # 'фамилия': 'Смоленский',
 # 'пол': 'мужской',
 # 'дата рождения': datetime.date(2018, 6, 21),
 # 'мобильный': '+79914262333'}
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Всеволод',
 # 'отчество': 'Федосеевич',
 # 'фамилия': 'Пешков',
 # 'пол': 'мужской',
 # 'дата рождения': datetime.date(1971, 12, 6),
 # 'мобильный': '+79021129411'}
# >>>