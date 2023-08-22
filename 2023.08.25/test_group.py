from random import randrange as rr, choice, sample
from string import digits, ascii_uppercase, ascii_lowercase
from datetime import date, datetime as dt, timedelta

import test

def produce_group(teachers: list[test.Teacher, ...], students: list[test.Student, ...], semester: int = 1, qty: int = rr(12, 25)):
    group = test.Group(semester, choice(teachers), *sample(students, k=qty))
    return group
    
def mobile() -> str:        
    mob_num = ''.join(sample(digits, k=9))
    return f'+79{mob_num}'
    
def office() -> str:
    return ''.join(sample(digits, k=9))
    
def gen_str():
    return ''.join(sample(ascii_lowercase, k=rr(6,10)))
   
def title() -> str:
    return choice(ascii_uppercase) + ''.join(sample(ascii_lowercase, k=rr(6,10)))
      
def email() -> str:
    return f"{''.join(sample(ascii_lowercase, k=rr(6,10)))}@{choice(['mail.ru', 'gmail.com'])}" 

def gen_dt():
    _dt = date.today() + timedelta(rr(2, 90))
    return _dt

def t_delta():
    return timedelta(rr(2, 8))
    
def gen_con():
    return test.Contact(mobile(), office(), email())


    