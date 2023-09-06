from typing import Self


class ClassBuilder:
    """Представляет методы для формирования строкового представленя создаваемого класса."""
    def __init__(self, class_name):
        """
        Инициализирует экземпляр класса ClassBuilder.

        :param class_name: имя класса
        """
        self.name = f'class {class_name}:'
        self.cls_field: dict = {}
        self.inst_attr: dict = {}
        
    def add_cls_field(self, cls_field, values) -> Self:
        """
        Добавляет  поля класса

        :param cls_field: название поля
        :param values: значение поля
        """
        self.cls_field |= {cls_field: values}
        return self
        
    def add_inst_attr(self, inst_attr, values) -> Self:
        """
        Добавляет атрибут экземпляра.

        :param inst_attr: Название поля
        :param values: значение поля
        """
        self.inst_attr |= {inst_attr: values}
        return self
        
    def __str__(self): 
        str_cls_field = ''.join(f'\t{k} = {v!r}\n' for k, v in self.cls_field.items())
        str_inst_attr = '\n'.join(f'\t\tself.{k} = {v!r}' for k, v in self.inst_attr.items())
        str_res = (f'{self.name}\n' +
                   (((f'{str_cls_field}\n' if self.cls_field else '') +
                   f'\tdef __init__(self):\n' +
                   f'{str_inst_attr}') if self.inst_attr else f'\tpass'))
        return str_res
        
# >>> cb = ClassBuilder('Person').add_inst_attr('name', '').add_inst_attr('age', 0)
# >>> print(cb)
# class Person:
        # def __init__(self):
                # self.name = ''
                # self.age = 0
# >>> cb.add_cls_field('__protected', [])
# >>> print(cb)
# class Person:
        # __protected = []

        # def __init__(self):
                # self.name = ''
                # self.age = 0
# >>> cb = ClassBuilder('Test').add_cls_field('__protected', []).add_inst_attr('foo', 'bar').add_cls_field('__protected12', [])
# >>> print(cb)
# class Test:
        # __protected = []
        # __protected12 = []

        # def __init__(self):
                # self.foo = 'bar'
# >>> cb = ClassBuilder('Foo')
# >>> print(cb)
# class Foo:
        # pass
# >>>
