def important_message(text: str) -> str:

    """Возвращает сгенерированную строку полученную из атрибута text"""
    
    import shutil
    
    col, line = shutil.get_terminal_size()
    str_outer = f"#{'='*(col-3)}#\n"
    str_space = f"#{' '*(col-3)}#\n"
   
    content =''
    while len(text)>0:
        content += f"#{text[:col-7].center(col-3)}#\n"
        text = text[(col-7):]
    
    return str_outer + str_space +content + str_space + str_outer