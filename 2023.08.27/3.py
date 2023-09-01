from pathlib import Path

from pathlib import Path
from sys import path
from typing import Self


class HTMLTag:
    """
    Описывает HTML тег, который может содержать вложенные теги.
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = '', **kwargs):
        self.name = name
        self.value = value
        self.atr = kwargs
        self.__nested: list[HTMLTag] = []

    def nested(self, html_tag: Self):
        """Добавляет вложенный тег к текущему."""
        self.__nested.append(html_tag)

    def __str(self, indent_level: int) -> str:
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами."""
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        atr = ' '.join(f'{k} = {v}' for k, v in self.atr.items())
        result = f"{margin}<{self.name}{' ' + atr if atr else ''}>{self.value}"
        if self.__nested:
            for tag in self.__nested:
                result += '\n' + tag.__str(indent_level+1)
            eol = f'\n{margin}'
        result += f"{eol}</{self.name}>"
        return result

    def __str__(self):
        return self.__str(0)

    # в данной реализации нецелесообразно "прятать" класс HTMLBuilder
    @staticmethod
    def create(name: str, value: str = '', **kwargs):
        return HTMLBuilder(name, value, **kwargs)


class HTMLBuilder:
    """
    Предоставляет методы для пошаговой инициализации экземпляра HTMLTag.
    """
    def __init__(self, root: HTMLTag | str, value: str = '', *, parent: Self = None, **kwargs):
        if isinstance(root, HTMLTag):
            pass
        elif isinstance(root, str):
            root = HTMLTag(root, value, **kwargs)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')
        self.root: HTMLTag = root
        self.__parent: Self = parent
        

    def nested(self, name: str, value: str = '', **kwargs) -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested(tag)
        return HTMLBuilder(tag, parent=self)
        

    def sibling(self, name: str, value: str = '', **kwargs) -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested(tag)
        return self
        

    def build(self) -> HTMLTag:
        if self.__parent is None:
            return self.root
        else:
            return self.__parent.build()
            
            
    def to_parent(self) -> HTMLTag:
        return self.__parent
        
        
class CVProfiler:
    def __init__(self, name: str, age: int, field_of_work: str):
        root = HTMLTag.create('html')\
                        .nested('head')\
                        .sibling('title', f'{name}: портфолио')\
                        .nested('body')\
                        .nested('div')\
                        .sibling('h2', 'Обо мне')\
                        .sibling('p', name)\
                        .sibling('p', 'возраст : ' + str(age) + 'лет')\
                        .sibling('p', 'сфера деятельности: ' + field_of_work)
                        
                        
        self.root: HTMLTag = root
        self.flag_edu: bool = True
        self.flag_pro: bool = True
        self.flag_con: bool = True
        self.email: bool = False
        
        
    def add_education(self, name_institution: str, course: str, year_end: int) -> Self: 
        if self.flag_edu:
            self.add_edu_parent = self.root.to_parent()\
            .nested('div')\
            .sibling('h2', 'Образование')\
            .sibling('p', 'учебное заведение:')\
            .nested('ul')           
            self.flag_edu = False            
        
        self.add_edu_parent\
        .nested('li', name_institution)\
        .nested('ul')\
        .sibling('li', 'специальность: ' + course)\
        .sibling('li', 'год окончания: ' + str(year_end))        
        return self
        
  
    def add_project(self, project_name, img_path) -> Self:
        if self.flag_pro:
            self.add_pro_parent = self.root.to_parent()\
            .nested('div')\
            .sibling('h2', 'Мои проекты')\
            .nested('ul') 
            self.flag_pro = False
            
        self.add_pro_parent\
        .nested('li')\
        .nested('div')\
        .sibling('p', project_name)\
        .sibling('img', src = img_path , width="400")        
        return self
    
    
    def add_contact(self, **kwargs) -> Self:
        if self.flag_con:
            self.add_con_parent = self.root.to_parent()\
            .nested('div')\
            .sibling('h2', 'Мои контакты')\
            .nested('ul') 
            self.flag_con = False
        for k, v in kwargs.items():
            if k.lower() == 'email':
                self.email = True
            self.add_con_parent\
            .nested('li', f'{k}: {v}')        
        return self
        
    
    def build(self) -> HTMLTag:
        if not self.email:
            raise ValueError('Необходимо ввести поле с email')
        if self.root._HTMLBuilder__parent is None:
            return self.root
        else:
            return self.root._HTMLBuilder__parent.build()
            
    
cv1 = CVProfiler('Иванов Иван Иванович', 26, 'художник-фрилансер')\
        .add_education('Архитектурная Академия1', 'Компьютерный дизайн', 2018)\
        .add_education('Архитектурная Академия2', 'Компьютерный дизайн', 2019)\
        .add_education('Архитектурная Академия3', 'Компьютерный дизайн', 2020)\
        .add_project('Разработка логотипа для компании по производству снеков', 'https://re-sign.ru/storage/app/uploads/public/fd6/ef4/5e5/thumb__785_523_0_0_exact.jpg')\
        .add_project('UI разработка для интернет-магазина Hend Med', 'https://cs1.livemaster.ru/storage/94/f2/98bb7b10de07da19d61e17c0451d--ukrasheniya-muzhskoj-kozhanyj-braslet-volk.jpg')\
        .add_contact(devianart='ivovuvan_in_art', telegram='@ivovuvan')\
        .add_contact(email='ivovuvan_in_art@mail.com').build()

print(cv1)

(Path(path[0]) / '3.html').write_text(str(cv1), encoding='utf-8')

# <html>
  # <head>
    # <title>Иванов Иван Иванович: портфолио</title>
    # <body>
      # <div>
        # <h2>Обо мне</h2>
        # <p>Иванов Иван Иванович</p>
        # <p>возраст : 26лет</p>
        # <p>сфера деятельности: художник-фрилансер</p>
      # </div>
      # <div>
        # <h2>Образование</h2>
        # <p>учебное заведение:</p>
        # <ul>
          # <li>Архитектурная Академия1
            # <ul>
              # <li>специальность: Компьютерный дизайн</li>
              # <li>год окончания: 2018</li>
            # </ul>
          # </li>
          # <li>Архитектурная Академия2
            # <ul>
              # <li>специальность: Компьютерный дизайн</li>
              # <li>год окончания: 2019</li>
            # </ul>
          # </li>
          # <li>Архитектурная Академия3
            # <ul>
              # <li>специальность: Компьютерный дизайн</li>
              # <li>год окончания: 2020</li>
            # </ul>
          # </li>
        # </ul>
      # </div>
      # <div>
        # <h2>Мои проекты</h2>
        # <ul>
          # <li>
            # <div>
              # <p>Разработка логотипа для компании по производству снеков</p>
              # <img src = https://re-sign.ru/storage/app/uploads/public/fd6/ef4/5e5/thumb__785_523_0_0_exact.jpg width = 400></img>
            # </div>
          # </li>
          # <li>
            # <div>
              # <p>UI разработка для интернет-магазина Hend Med</p>
              # <img src = https://cs1.livemaster.ru/storage/94/f2/98bb7b10de07da19d61e17c0451d--ukrasheniya-muzhskoj-kozhanyj-braslet-volk.jpg width = 400></img>
            # </div>
          # </li>
        # </ul>
      # </div>
      # <div>
        # <h2>Мои контакты</h2>
        # <ul>
          # <li>devianart: ivovuvan_in_art</li>
          # <li>telegram: @ivovuvan</li>
          # <li>email: ivovuvan_in_art@mail.com</li>
        # </ul>
      # </div>
    # </body>
  # </head>
# </html>