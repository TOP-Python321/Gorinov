import shutil
from pathlib import Path
from sys import path
from sys import path, modules
from importlib.util import spec_from_file_location, module_from_spec


def important_message(text: str) -> str:
    """Возвращает сгенерированную строку полученную из атрибута text"""
    
    
    col, line = shutil.get_terminal_size()
    str_outer = f"#{'='*(col-3)}#\n"
    str_space = f"#{' '*(col-3)}#\n"
   
    content =''
    while len(text)>0:
        content += f"#{text[:col-7].center(col-3)}#\n"
        text = text[(col-7):]
    
    return str_outer + str_space +content + str_space + str_outer.replace('\n', '')
    
    
def load_file(file_path: Path) -> 'module':
    """Принимает ссылку к файлу в виде объекта Path, копирует найденный файл в текущий каталог, импортирует файл 
       и возвращает обект модуля импортированного файла."""
    shutil.copy2(file_path, Path(path[0]))
    
    
    importing_file_path = Path(path[0]) / file_path.name    
    module_name = file_path.stem   
    spec = spec_from_file_location(module_name, importing_file_path)   
    file_module = module_from_spec(spec)    
    modules[module_name] = file_module
    spec.loader.exec_module(file_module)
    
    return modules[module_name]
    


    
    