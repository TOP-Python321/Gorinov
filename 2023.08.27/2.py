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


div = HTMLTag.create('div')\
             .sibling('p', 'Menu', align='right', style="color:#00FF00")\
             .nested('ul', style="color:#0000FF")\
             .sibling('li', 'File')\
             .sibling('li', 'Edit')\
             .sibling('li', 'View')\
             .build()
print(div)

# <div>
  # <p align = right style = color:#00FF00>Menu</p>
  # <ul style = color:#0000FF>
    # <li>File</li>
    # <li>Edit</li>
    # <li>View</li>
  # </ul>
# </div>

(Path(path[0]) / '2.html').write_text(str(div), encoding='utf-8')
