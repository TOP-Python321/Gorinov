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
    mobile: str = None
    office: str = None
    email: str = None    
    
    
class Person(ABC):

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
    def fio(self):
        return self.__fio

    def change_name(
            self,
            new_name: str,
            name_part: Literal['last', 'first', 'patr']
    ):
        setattr(self, f'{name_part}_name', new_name)
        self.__fio = f'{self.last_name} {self.first_name} {self.patr_name}'

    @abstractmethod
    def __str__(self):
        pass
        
        
class Personnel(Person):

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
        return self._exp + dec((date.today() - self.job_start).days / 365.25)
        
        
class Administrator(Personnel):
    def __str__(self):
        return f'<Administrator: {self.fio}>'


class Teacher(Personnel):
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
    def __init__(
                self, 
                title: str, 
                head: Administrator, 
                contacts: Contact,
                *iters
        ):
        super().__init__(*iters)
        self.title = title
        self.head = head
        self.contacts = contacts
    
    def hire(self, obj) -> Personnel:
        if isinstance(obj, Teacher | Administrator):
            self.append(obj)
            return obj
        else:
            raise TypeError
    def fire(self, obj) -> Personnel:
        if isinstance(obj, Teacher | Administrator):            
            if not obj in self:            
                raise NameError("Такого сотрудника нет в списке сотрудников.")           
            self.remove(obj)
            return obj
        else:
            raise TypeError           

class Group(list):
    def __init__(
            self, 
            semester: int, 
            curator: Teacher, 
            *students, 
            head: Student = None,
    ):  
        super().__init__(students)        
        self.semester = semester
        self.curator = curator       
        if isinstance(head, Student):
            self.head = head
        else:        
            self.head = choice(self)        
        
    def promote(self):        
        super().__init__([elem for elem in self if elem.grade > sum([2, 3 ,4 ,5]) / 4])
        self.semester += 1           
        
class Departament(Organization):
    def __init__(
                self,                
                title: str, 
                head: Administrator, 
                contacts: Contact,
                groups: list[Group],
                *personnel
        ):
        super().__init__(
                        title,
                        head,
                        contacts,
                        personnel
                        )        
        self.groups = groups
        
        
class Laboratory(Organization):
    def __init__(
                self,                
                title: str, 
                head: Administrator, 
                contacts: Contact,
                equipment: list[str],
                schedule: list[dict[dt, timedelta]],
                *personnel
        ):
        super().__init__(
                    title,
                    head,
                    contacts,
                    personnel
                    )     
        self.equipment = equipment
        self.schedule = schedule
        
        
class Institute(Organization):
     def __init__(
                self,                
                title: str, 
                head: Administrator, 
                contacts: Contact,
                departments: list[Departament],
                labs: list[Laboratory],
                *personnel
        ):
        super().__init__(
                    title,
                    head,
                    contacts,
                    personnel
                    )    
        self.departments = departments
        self.labs = labs
        
        
class University(Organization):
    def __init__(
                self,                
                title: str, 
                head: Administrator, 
                contacts: Contact,
                institutes: list[Institute],
                *personnel
        ):
        super().__init__(
                    title,
                    head,
                    contacts,
                    personnel
                    )            
        self.institutes = institutes
        
        