from datetime import date
from decimal import Decimal as dec
from json import loads
from pathlib import Path
from random import randrange as rr, choice, sample
from re import compile
from sys import path

import test as model
import test_group as test_gp
import _university_crm_datagen as datagen

datagen.load_data()
datagen.dump_students_list(100)
datagen.dump_teachers_list(100)
datagen.dump_administrator_list(15)

data_students = Path(path[0]) / 'data/students.json'
data_teachers = Path(path[0]) / 'data/teachers.json'
data_administrators = Path(path[0]) / 'data/administrators.json'

data_students = loads(data_students.read_text(encoding='utf-8'))
data_teachers = loads(data_teachers.read_text(encoding='utf-8'))
data_administrators = loads(data_administrators.read_text(encoding='utf-8'))


students, teachers, administrators = [], [], []
for entry in data_students:
    entry['sex'] = model.Person.Sex(entry['sex'])
    entry['contacts'] = model.Contact(mobile=entry['contacts'])
    entry['grade'] = float(entry['grade'])
    if rr(10):
        entry['grant'] = dec(entry['grant'])

    try:
        assert isinstance(entry['grant'], dec)
    except AssertionError:
        ...
        # print()
        # pprint(entry, sort_dicts=False)
    else:
        students.append(model.Student(**entry))

for entry in data_teachers:
    entry['sex'] = model.Person.Sex(entry['sex'])
    entry['contacts'] = model.Contact(mobile=entry['contacts'])
    entry['salary'] = dec(f"{entry['salary']}.0")
    if entry['degree'] is not None:
        entry['degree'] = model.Personnel.Degree(entry['degree'])
    entry['previous_experience'] = dec(entry['previous_experience'])
    teachers.append(model.Teacher(**entry))
    
for entry in data_administrators:
    entry['sex'] = model.Person.Sex(entry['sex'])
    entry['contacts'] = model.Contact(mobile=entry['contacts'])
    entry['salary'] = dec(f"{entry['salary']}.0")
    if entry['degree'] is not None:
        entry['degree'] = model.Personnel.Degree(entry['degree'])
    entry['previous_experience'] = dec(entry['previous_experience'])
    administrators.append(model.Administrator(**entry))


pat_fio = compile(r'\w+ \w+ \w+')

def test_teachers():
    for i, teacher in enumerate(teachers):
        try:
            assert pat_fio.fullmatch(teacher.fio)
        except AssertionError:
            print(teacher.fio)

        work_age = date.today().year - teacher.birthdate.year - 23
        try:
            assert work_age > teacher.exp
        except AssertionError:
            print(f'\n{i=}, {teacher}\n'
                  f'\t{work_age} лет работы, {teacher.exp} лет стажа')


# создание персонала
personnel = teachers + administrators
personnel_university = sample(personnel, len(personnel) // 2)
personnel_institute = sample(personnel_university, len(personnel_university) // 2)
personnel_department = sample(personnel_institute, len(personnel_institute) // 2)
personnel_laboratory = list(set(personnel_institute) - set(personnel_department))

# создание групп
list_group = [test_gp.produce_group(teachers, students) for _ in range(rr(4, 10))]

# генерирование объектов Laboratory
def gen_lab() -> model.Laboratory:
    """Генерирует и возвращает объект model.Laboratory"""
    lab_equipment = [test_gp.title() for _ in range(rr(5, 15))]
    lab_schedule = [{test_gp.gen_dt(): test_gp.t_delta()} for _ in range(rr(2, 20))]
    return model.Laboratory(test_gp.title(), choice(administrators), test_gp.gen_con(), lab_equipment, lab_schedule, *personnel_laboratory) 

# генерирование объектов Department
def gen_dep() -> model.Departament:
    """Генерирует и возвращает объект model.Departament"""
    return model.Departament(test_gp.title(), choice(administrators), test_gp.gen_con(), list_group, *personnel_department)

# генерирование объектов Institute
def gen_ins() -> model.Institute:
    """Генерирует и возвращает объект model.Institute"""
    inst_departments = [gen_dep() for _ in range(rr(3, 10))]
    inst_labs = [gen_lab() for _ in range(rr(3, 10))]
    return model.Institute(test_gp.title(), choice(administrators), test_gp.gen_con(), inst_departments, inst_labs, *personnel_institute)

# генерирование объектов Univesity
def gen_uni() -> model.University:
    """Генерирует и возвращает объект model.University"""
    list_institute = [gen_ins() for _ in range(rr(3, 10))]
    return model.University(test_gp.title(), choice(administrators), test_gp.gen_con(), list_institute, *personnel_university)
    
# тестирование Group
def test_groups():
    """Функция для тестирования класса Group"""
    for group in list_group:
        print(f'Руководитель группы = {str(group.curator)}\n'
              f'Староста группы = {str(group.head)}')
        print(*(elem for elem in group), sep='\n', end='\n\n')    

    test_group = test_gp.produce_group(teachers, students)
    print(f'\n{len(test_group) = }')
    print(f'{str(test_group.head) = }')
    print(f'{test_group.semester = }')
    print(f'{str(test_group.curator) = }')
    
    print(f'\nПереводим студентов на следующий семестр.')
    test_group.promote()

    print(f'\n{len(test_group) = }')
    print(f'{str(test_group.head) = }')
    print(f'{test_group.semester = }')
    print(f'{str(test_group.curator) = }')


# тестирование Department
def test_deps():
    """Функция для тестирования класса Department"""
    test_dep = gen_dep()

    print(f'\nИмя организации: {test_dep.title}\n'
          f'Руководитель: {test_dep.head}\n'
          f'Контакты: моб - {test_dep.contacts.mobile}, тел. офиса - {test_dep.contacts.office}, email - {test_dep.contacts.email}\n'
          f'Количество групп = {len(test_dep.groups)}\n'
          f'Сотрудники:')
    print(*(f'\t{str(elem)}' for elem in test_dep), sep='\n')


# Тестирование Laboratory
def test_labs():
    """Функция для тестирования класса Laboratory"""
    test_lab = gen_lab()

    print(f'\nИмя организации: {test_lab.title}\n'
          f'Руководитель: {test_lab.head}\n'
          f'Контакты: моб - {test_lab.contacts.mobile}, тел. офиса - {test_lab.contacts.office}, email - {test_lab.contacts.email}\n'
          f'Количество оборудования = {len(test_lab.equipment)}\n'
          f'Количество опытов в графике = {len(test_lab.schedule)}\n'
          f'Сотрудники:')
    print(*(f'\t{str(elem)}' for elem in test_lab), sep='\n')


# Тестирование Institute
def test_insts():
    """Функция для тестирования класса Institute"""

    test_inst = gen_ins()

    print(f'\nИмя организации: {test_inst.title}\n'
          f'Руководитель: {test_inst.head}\n'
          f'Контакты: моб - {test_inst.contacts.mobile}, тел. офиса - {test_inst.contacts.office}, email - {test_inst.contacts.email}\n'
          f"Список факультетов: {', '.join(elem.title for elem in test_inst.departments)}\n"
          f"Список лабораторий: {', '.join(elem.title for elem in test_inst.labs)}\n"
          f'Сотрудники:')
    print(*(f'\t{str(elem)}' for elem in test_inst), sep='\n')


# Тестирование Univesity
def test_unis():
    """Функция для тестирования класса Univesity"""
    test_uni = gen_uni()

    print(f'\nИмя организации: {test_uni.title}\n'
          f'Руководитель: {test_uni.head}\n'
          f'Контакты: моб - {test_uni.contacts.mobile}, тел. офиса - {test_uni.contacts.office}, email - {test_uni.contacts.email}\n'
          f"Список институтов: {', '.join(elem.title for elem in test_uni.institutes)}\n"      
          f'Сотрудники:')
    print(*(f'\t{str(elem)}' for elem in test_uni), sep='\n')


while True:
    list_test = [test_teachers, test_groups, test_deps, test_labs, test_insts, test_unis]
    inp = input(
         f'\nВыберите группу для тестирования'
         f'\n\t1 - вывод списка учителей'
         f'\n\t2 - тестирование класса Group'
         f'\n\t3 - тестирование класса Departament'
         f'\n\t4 - тестирование класса Laboratory'
         f'\n\t5 - тестирование класса Institute'
         f'\n\t6 - тестирование класса University'
         f'\nДля выхода введите пустое "Q": \n'         
         )
         
    if inp.upper() == "Q":
        break
    if '0' < inp < '7':
        list_test[int(inp) - 1]()

