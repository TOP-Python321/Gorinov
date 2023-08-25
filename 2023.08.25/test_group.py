from random import randrange as rr, choice, sample
from string import digits, ascii_uppercase, ascii_lowercase
from datetime import date, timedelta

import test


def produce_group(
        teachers: list[test.Teacher, ...],
        students: list[test.Student, ...],
        semester: int = 1,
        qty: int = rr(12, 25)
        ) -> test.Group:
    """
    Создает и возвращает объект класса Group.
    :param teachers: список из объектов Teacher
    :param students: список из объектов Student
    :param semester: номер семестра, по умолчанию - 1
    :param qty: количество студентов в группе
    :return: объект класса Group
    """
    group = test.Group(semester, choice(teachers), *sample(students, k=qty))
    return group


def mobile() -> str:
    """Генерирует номер мобильного телефона."""
    mob_num = ''.join(sample(digits, k=9))
    return f'+79{mob_num}'


def office() -> str:
    """Генерирует номер стационарного телефона."""
    return ''.join(sample(digits, k=9))


def gen_str():
    """Генерирует строку из произвольных символов."""
    return ''.join(sample(ascii_lowercase, k=rr(6, 10)))


def title() -> str:
    """Генерирует названии организации."""
    return choice(ascii_uppercase) + ''.join(sample(ascii_lowercase, k=rr(6, 10)))


def email() -> str:
    """Генерирует электронный адрес"""
    return f"{''.join(sample(ascii_lowercase, k=rr(6,10)))}@{choice(['mail.ru', 'gmail.com'])}" 


def gen_dt() -> date:
    """Генерирует объект date"""
    _dt = date.today() + timedelta(rr(2, 90))
    return _dt


def t_delta() -> timedelta:
    """Генерирует объект timedelta"""
    return timedelta(rr(2, 8))


def gen_con() -> test.Contact:
    """Генерирует и возвращает объект test.Contact."""
    return test.Contact(mobile(), office(), email())
