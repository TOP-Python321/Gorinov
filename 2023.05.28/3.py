from pathlib import Path
from utils import load_file

def ask_for_file() -> 'module':

    """Запрашивает путь к файлу и передает этот путь в функцию load_file, которая копирует файл в текущий каталог и импортирует его.
       load_file возвращает объект модуля импортируемого файла. ask_for_file возврашает объект модуля полученный из load_file"""
       
    while True:
    
        file_path = Path(input('Введите путь к файлу: '))
        
        if file_path.is_file():            
            return load_file(file_path)                
        else:    
            print('! по указанному пути отсутствует необходимый файл !')
            
# >>> config_module = ask_for_file()
# Введите путь к файлу: C:\Users\ПК\Desktop\TOP\Git\repository\самостоятельная работа\i_work\dreft 2023.05.28\data\conf.py
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}