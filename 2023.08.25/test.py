from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date, datetime as dt, timedelta
from decimal import Decimal as dec
from enum import Enum
from typing import Literal
from random import choice


# вариант с обычным созданием класса
# class Contact():
    # def __init__(self, mobile: str, office: str|None, email: str|None):
        # self.mobile = mobile
        # self.office = office
        # self.email = email

# создание через декоратор @dataclass. Создание объектов с данными
@dataclass
class Contact:
    """Класс Contact представляет контактные данные."""
    mobile: str = None
    office: str = None
    email: str = None    
    
    
class Person(ABC):
    """Класс Person представляет человека с фамилией, именем, отчеством, полом, датой рождения, контактными данными"""
    class Sex(Enum):
        MALE = 'мужской'
        FEMALE = 'женский'

    _default_date_format: str = '%d.%m.%Y'

    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
    ):
        """
        Инициализирует объект класса Person.
        :param last_name: фамилия
        :param first_name: имя
        :param patr_name: отчество
        :param sex: пол
        :param birthdate: дата рождения
        :param contacts: контактные данные(объект класса Contact)
        """
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
        self.__fio: str = f'{self.last_name} {self.first_name} {self.patr_name}'
        self.sex = sex
        if isinstance(birthdate, tuple):
            try:
                date_, format_ = birthdate
                assert isinstance(date_, str)
                assert isinstance(format_, str)
            except (ValueError, AssertionError):
                raise  # собственное исключение
            else:
                birthdate = dt.strptime(*birthdate)
        elif isinstance(birthdate, str):
            birthdate = dt.strptime(birthdate, self._default_date_format)
        self.birthdate: date = birthdate
        self.contacts = contacts

    @property
    def fio(self) -> str:
        """Возвращает строку с фамилией, именем, отчеством человека"""
        return self.__fio

    def change_name(
            self,
            new_name: str,
            name_part: Literal['last', 'first', 'patr']
    ):
        """
        Устанавливает фамилию, имя, отчество человека.
        :param new_name: новое имя
        :param name_part: выборать какой атрибут будет устанавливаться ('last', 'first', 'patr')
        """
        setattr(self, f'{name_part}_name', new_name)
        self.__fio = f'{self.last_name} {self.first_name} {self.patr_name}'

    @abstractmethod
    def __str__(self):
        pass
        
        
class Personnel(Person):
    """
    Класс Person представляет сотрудника с фамилией, именем, отчеством, полом, датой рождения, контактными данными,
    идентификатором, зарплатой, ученой степенью, титулом, и стажем работы.
    """

    class Degree(Enum):
        CANDIDATE = 'кандидат наук'
        DOCTOR = 'доктор наук'

    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Person.Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
            id_: int,
            salary: dec,
            degree: Degree | None = None,
            titles: list[str] = None,
            previous_experience: dec = dec(0),
    ):
        """
        Инициализирует объект класса Personnel.
        :param last_name: фамилия
        :param first_name: имя
        :param patr_name: отчество
        :param sex: пол
        :param birthdate: дата рождения
        :param contacts: контактные данные(объект класса Contact)
        :param id_: идентификатор
        :param salary: зарплата
        :param degree: степень
        :param titles: титул
        :param previous_experience: стаж работы
        """
        super().__init__(
            last_name,
            first_name,
            patr_name,
            sex,
            birthdate,
            contacts
        )
        self.id = id_
        self.salary = salary
        self.degree = degree
        if titles is None:
            titles = []
        self.titles = titles
        self.job_start: date = date.today()
        self._exp = previous_experience

    @property
    def exp(self) -> dec:
        """Вычисляет и возвращает общий стаж работы"""
        return self._exp + dec((date.today() - self.job_start).days / 365.25)
        
        
class Administrator(Personnel):
    """Класс Administrator представляет сотрудника на должности администратора."""
    def __str__(self):
        return f'<Administrator: {self.fio}>'


class Teacher(Personnel):
    """Класс Teacher представляет сотрудника на должности преподавателя"""
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Person.Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
            id_: int,
            salary: dec,
            courses: list[str],
            degree: Personnel.Degree | None = None,
            titles: list[str] = None,
            previous_experience: dec = dec(0)
    ):
        """
        Инициализирует объект класса Teacher.
        :param last_name: фамилия
        :param first_name: имя
        :param patr_name: отчество
        :param sex: пол
        :param birthdate: дата рождения
        :param contacts: контактные данные(объект класса Contact)
        :param id_: идентификатор
        :param salary: зарплата
        :param courses: список преподаваемых курсов
        :param degree: ученая степень
        :param titles: титул
        :param previous_experience: стаж работы до найма
        """
        super().__init__(
            last_name,
            first_name,
            patr_name,
            sex,
            birthdate,
            contacts,
            id_,
            salary,
            degree,
            titles,
            previous_experience
        )
        self.courses = courses

    def __str__(self):
        return f'<Teacher: {self.fio}>'


class Student(Person):
    """Класс Student представляет описание студента."""
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Person.Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
            student_id: str,
            grant: dec = dec(0),
            grade: float = float(0)
    ):
        """
        Инициализирует объект класса Student.
        :param last_name: фамилия
        :param first_name: имя
        :param patr_name: отчество
        :param sex: пол
        :param birthdate: дата рождения
        :param contacts: контактные данные(объект класса Contact)
        :param student_id: идентификатор
        :param grant: стипендия
        :param grade: средняя оценка успеваемости
        """
        super().__init__(
            last_name,
            first_name,
            patr_name,
            sex,
            birthdate,
            contacts
        )
        self.student_id = student_id
        self.grant = grant
        self.grade = grade

    def __str__(self):
        return f'<Student: {self.fio}>'
        
        
class Organization(ABC, list):
    """Класс Organization представляет описание организации,"""
    def __init__(
                self, 
                title: str, 
                head: Administrator, 
                contacts: Contact,
                *iters
    ):
        """
        Инициализация объекта Organization
        :param title: название организации
        :param head: управляющий организацией (объект класса Administrator)
        :param contacts: контактные данные(объект класса Contact)
        :param iters: итерируемый объект из сотрудников организации
        """
        super().__init__(*iters)
        self.title = title
        self.head = head
        self.contacts = contacts
    
    def hire(self, obj) -> Personnel:
        """Добавляет новых сотрудников в список организации."""
        if isinstance(obj, Teacher | Administrator):
            self.append(obj)
            return obj
        else:
            raise TypeError

    def fire(self, obj) -> Personnel:
        """Удаляет сотрудника из списка организации."""
        if isinstance(obj, Teacher | Administrator):            
            if obj not in self:
                raise NameError("Такого сотрудника нет в списке сотрудников.")           
            self.remove(obj)
            return obj
        else:
            raise TypeError


class Group(list):
    """Класс Group представляет описание учебной группы."""
    def __init__(
            self, 
            semester: int, 
            curator: Teacher, 
            *students, 
            head: Student = None,
    ):
        """
        Инициализация объекта класса Group,
        :param semester: семестр
        :param curator: куратор группы
        :param students: итерируемый объект из студентов
        :param head: староста группы
        """
        super().__init__(students)        
        self.semester = semester
        self.curator = curator       
        if isinstance(head, Student):
            self.head = head
        else:        
            self.head = choice(self)        
        
    def promote(self):
        """
        Переводит студентов у которых средний бал успеваемости
        выше среднего. И переопределяет список группы этими студентами.
        """
        super().__init__([elem for elem in self if elem.grade > sum([2, 3, 4, 5]) / 4])
        self.semester += 1

        
class Departament(Organization):
    """Класс Departament представляет описание факультета."""
    def __init__(
                self,                
                title: str, 
                head: Administrator, 
                contacts: Contact,
                groups: list[Group],
                *personnel
    ):
        """
        Инициализирует объект класса Departament.
        :param title: название факультета
        :param head: управляющий факультетом
        :param contacts: контактные данные(объект класса Contact)
        :param groups: список состоящий из групп факультета
        :param personnel: итерируемый объект из сотрудников факультета
        """
        super().__init__(
                        title,
                        head,
                        contacts,
                        personnel
                        )        
        self.groups = groups
        
        
class Laboratory(Organization):
    """Класс Laboratory представляет описание лаборатории."""
    def __init__(
                self,                
                title: str, 
                head: Administrator, 
                contacts: Contact,
                equipment: list[str],
                schedule: list[dict[dt, timedelta]],
                *personnel
    ):
        """
        Инициализация объекта класса Laboratory.
        :param title: название лаборатории
        :param head: управляющий лабораторией
        :param contacts: контактные данные(объект класса Contact)
        :param equipment: список оборудования
        :param schedule: список из словаря с графиком опытов
        :param personnel: итерируемый объект из сотрудников лаборатории
        """
        super().__init__(
                    title,
                    head,
                    contacts,
                    personnel
                    )     
        self.equipment = equipment
        self.schedule = schedule
        
        
class Institute(Organization):
    """Класс Institute представляет описание института."""
    def __init__(
                self,                
                title: str, 
                head: Administrator, 
                contacts: Contact,
                departments: list[Departament],
                labs: list[Laboratory],
                *personnel
    ):
        """
        Инициализация объекта класса Institute.
        :param title: название института
        :param head: управляющий институтом
        :param contacts: контактные данные(объект класса Contact)
        :param departments: список факультктов
        :param labs: список лаборторий
        :param personnel: итерируемый объект из сотрудников института
        """
        super().__init__(
                    title,
                    head,
                    contacts,
                    personnel
                    )    
        self.departments = departments
        self.labs = labs
        
        
class University(Organization):
    """Класс University представляет описание университета."""
    def __init__(
                self,                
                title: str, 
                head: Administrator, 
                contacts: Contact,
                institutes: list[Institute],
                *personnel
    ):
        """
        Инициализация объекта класса University.
        :param title: название университета
        :param head: управляющий университетом
        :param contacts: контактные данные(объект класса Contact)
        :param institutes: список институтов
        :param personnel: итерируемый объект из сотрудников университета
        """
        super().__init__(
                    title,
                    head,
                    contacts,
                    personnel
                    )            
        self.institutes = institutes
        
        