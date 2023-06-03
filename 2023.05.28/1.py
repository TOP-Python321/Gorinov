from pathlib import Path

def list_files(path_arg: str) -> tuple | None:
    """Возвращает кортеж с именами файлов в каталоге по пути указанному в аргументе path_arg.Если указан 
       несуществующий каталог возвращает None.
    """
    path_dir = Path(path_arg)
    list_files = ()
    
    if path_dir.is_dir():
        for elem in path_dir.iterdir():
            if elem.is_file():          
                list_files += (elem.name,)
        return list_files
        
>>> list_files(r'C:\Users\ПК\Desktop\TOP\Git\repository\python\дз\Gorinov\2023.05.14')
('# HW 2023.05.14.txt', '1.py', '2.py', '3.py', '4.py', '5.py', '6.py', '7.py')
>>> print(list_files(r'C:\Users\ПК\Desktop\TOP\Git\repository\python\дз\Gorinov\2023.05.144'))
None