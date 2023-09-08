from dataclasses import dataclass
from os import name as os_name
from typing import Self


if os_name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir_path: str
    
    @property
    def extension(self) -> str:
        return ''.join(self.name.rsplit('.', 1)[1:])
    
    def ls(self) -> str:
        return self.dir_path + PATH_SEP + self.name


class Folder(list):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    def __init__(self,  name: str, dir_path: str = 'c:'):
        super().__init__()
        self.name = name
        self.dir_path = dir_path

    def add_element(self, name: File | Self) -> Self:
        """Добавляет объекты класса File или Folder в список экземпляра Folder."""
        if isinstance(name, File | Folder):
            name.dir_path = self.dir_path + PATH_SEP + self.name
            self.append(name)
        else:
            raise TypeError
        return self

    def ls(self) -> str:
        # !Доработать с рекурсией!
        """Возвращает путь расположения экземпляра в файловой системе в виде строки."""
        return self.dir_path + PATH_SEP + self.name


def ls(*objects: File | Folder) -> str:
    for obj in objects:
        print(obj.ls())


f1 = File('Test1.txt', '')
p1 = Folder('Test_folder1')
p2 = Folder('Test_folder2')
p3 = Folder('Test_folder3')

p1.add_element(f1).add_element(p2)
p2.add_element(p3)
ls(p1, f1, p2, p3)

# c:\Test_folder1
# c:\Test_folder1\Test1.txt
# c:\Test_folder1\Test_folder2
# c:\Test_folder1\Test_folder2\Test_folder3
